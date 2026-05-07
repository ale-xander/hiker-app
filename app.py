import streamlit as st
from datetime import date, timedelta
import asyncio
from playwright.async_api import async_playwright
import re
from camp_data import CAMP_KNOWLEDGE

# --- 1. DATE LOGIC (Upgraded for Cascading Selection) ---
def get_upcoming_months(num_months=8):
    """Generates a dictionary of the next X months."""
    months = {}
    today = date.today()
    for i in range(num_months):
        m = today.month + i
        y = today.year + ((m - 1) // 12)
        m = ((m - 1) % 12) + 1
        dt = date(y, m, 1)
        months[dt.strftime("%B %Y")] = dt
    return months

def get_weekends_for_month(target_date):
    """Gets all Fridays for a specific month."""
    weekends = {}
    curr = target_date
    # Find the first Friday of the month
    while curr.weekday() != 4:
        curr += timedelta(days=1)
    # Collect all Fridays in that specific month
    while curr.month == target_date.month:
        weekends[curr.strftime("%a, %b %d")] = curr
        curr += timedelta(days=7)
    return weekends


# --- 2. SAN MATEO DRIVER ---
async def check_san_mateo(arrival_date, park_name):
    park_slugs = {
        "Memorial County Park": "memorial-park",
        "Sam McDonald Park": "sam-mcdonald-park"
    }
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        date_str = arrival_date.strftime("%m/%d/%Y")
        url = f"https://secure.itinio.com/sanmateo/{park_slugs[park_name]}?site_type_id=1&arrival={date_str}&nights=2"
        
        available_sites = []
        try:
            await page.goto(url)
            await page.wait_for_selector(".site-list", timeout=7000)
            sites = await page.query_selector_all(".site-item.available")
            
            for site in sites:
                text = await site.inner_text()
                site_name = text.split('\n')[0].strip() if text else "Available"
                available_sites.append(site_name)
                
            return available_sites, url
        except:
            return [], url
        finally:
            await browser.close()


# --- 3. SANTA CLARA DRIVER ---
async def check_santa_clara(arrival_date, park_name):
    async with async_playwright() as p:
        # Keep headless=False if you still want to watch it work, or change to True to hide it
        browser = await p.chromium.launch(headless=False, slow_mo=300) 
        context = await browser.new_context()
        page = await context.new_page()
        
        url = "https://gooutsideandplay.org/reservation/camping/index.asp"
        
        try:
            await page.goto(url, wait_until="domcontentloaded")
            await asyncio.sleep(5) 

            # 1. CLOSE MODAL
            try:
                await page.locator('.ui-dialog-titlebar-close').click(force=True, timeout=2000)
            except:
                pass 

            # 2. SELECT PARK (By exact text)
            await page.evaluate(f"""(name) => {{
                const selects = document.querySelectorAll('select');
                for (let sel of selects) {{
                    for (let opt of sel.options) {{
                        if (opt.text.toUpperCase().includes(name.toUpperCase())) {{
                            sel.value = opt.value;
                            sel.dispatchEvent(new Event('change'));
                            return;
                        }}
                    }}
                }}
            }}""", park_name)

            await asyncio.sleep(4) 

            # 3. SELECT TENT (By text)
            await page.evaluate("""() => {
                const selects = document.querySelectorAll('select');
                for (let sel of selects) {
                    for (let opt of sel.options) {
                        if (opt.text.includes('Tent')) {
                            sel.value = opt.value;
                            sel.dispatchEvent(new Event('change'));
                            return;
                        }
                    }
                }
            }""")
            
            await asyncio.sleep(4)

            # 4. INJECT ARRIVAL DATE
            arrival_str = arrival_date.strftime("%m-%d-%Y")
            await page.evaluate("""(arrArgs) => {
                const aHidden = document.getElementById('camping_arrive_date');
                if (aHidden) { 
                    aHidden.value = arrArgs.date; 
                    aHidden.dispatchEvent(new Event('change')); 
                }
                const monthSpan = document.getElementById('camp_arrive_month');
                const daySpan = document.getElementById('camp_arrive_day');
                if (monthSpan) monthSpan.innerText = arrArgs.m;
                if (daySpan) daySpan.innerText = arrArgs.d;
            }""", {
                "date": arrival_str, 
                "m": arrival_date.strftime("%b"), 
                "d": str(int(arrival_date.strftime("%d")))
            })

            await asyncio.sleep(4)

            # 5. INJECT DEPARTURE DATE
            departure_str = (arrival_date + timedelta(days=2)).strftime("%m-%d-%Y")
            await page.evaluate("""(depArgs) => {
                const dHidden = document.getElementById('camping_depart_date');
                if (dHidden) { 
                    dHidden.value = depArgs.date; 
                    dHidden.dispatchEvent(new Event('change')); 
                }
                const n = document.getElementById('res_nites');
                if (n) n.innerText = '2';
            }""", {"date": departure_str})

            await asyncio.sleep(3)

            # 6. CLICK SEARCH
            await page.evaluate("const btn = document.querySelector('button.BigBtn.AlphaBtn'); if(btn) btn.click();")
            
            # 7. TAB DETECTION & EXTRACTION
            await asyncio.sleep(8) 
            
            tab_locator = page.locator(".tab-allpark")
            if await tab_locator.count() > 0:
                await page.evaluate("const tab = document.querySelector('.tab-allpark'); if(tab) tab.click();")
                await asyncio.sleep(3) 
            
            available_sites = await page.evaluate(r"""() => {
                const cards = Array.from(document.querySelectorAll('.card-col'));
                const sites = [];
                
                cards.forEach(card => {
                    const btn = Array.from(card.querySelectorAll('button'))
                                     .find(b => {
                                         const txt = (b.textContent || "").toUpperCase();
                                         return txt.includes('RESERVE') && b.style.display !== 'none';
                                     });
                    
                    if (btn) {
                        const text = card.innerText || "";
                        const match = text.match(/Site:\s*([^\n\r|]+)/i);
                        
                        let siteName = "";
                        if (match && match[1]) {
                            siteName = match[1].split('Area:')[0].split('Park:')[0].trim();
                        } else {
                            const ghost = card.querySelector('.ghost_title_lg');
                            if (ghost) siteName = ghost.innerText.replace(/Site:/i, '').trim();
                        }
                        
                        if (siteName && !siteName.toUpperCase().includes('ADA')) {
                            sites.push(siteName);
                        }
                    }
                });
                return [...new Set(sites)];
            }""")
            
            return available_sites, url

        except Exception as e:
            print(f"SCRAPER ERROR at {park_name}: {e}")
            return [], url
        finally:
            await browser.close()


# --- 4. THE UI FRONTEND (The Concierge Update) ---
st.set_page_config(page_title="Hiker Radar", page_icon="🌲", layout="wide") # Changed to wide for better cards

# --- SIDEBAR FILTERS ---
with st.sidebar:
    st.header("🎯 Smart Filters")
    st.markdown("Leave blank to see all available sites.")
    
    # Filter 1: Group Size
    group_filter = st.multiselect(
        "Who are you camping with?", 
        ["Solo / Couple", "Single Family", "Multi-Family / Group"]
    )
    
    # Filter 2: Setting / Vibe
    vibe_filter = st.multiselect(
        "Setting / Vibe", 
        ["Waterfalls & Creeks", "Redwoods & Quiet", "Views & Sun"]
    )

# --- MAP UI SELECTIONS TO JSON TAGS ---
# This converts what you click in the UI to the tags hidden in your camp_data
active_target_tags = set()

if "Multi-Family / Group" in group_filter:
    active_target_tags.update(["group-friendly", "family-hub"])
if "Single Family" in group_filter:
    active_target_tags.update(["family-friendly", "kid-bike-loop"])
if "Solo / Couple" in group_filter:
    active_target_tags.update(["quieter-loop"]) # Assuming smaller parties prefer quiet

if "Waterfalls & Creeks" in vibe_filter:
    active_target_tags.update(["waterfall-hikes", "creekside"])
if "Redwoods & Quiet" in vibe_filter:
    active_target_tags.update(["redwood-forest", "quieter-loop"])
if "Views & Sun" in vibe_filter:
    active_target_tags.update(["view-potential", "partial-shade"])


# --- MAIN PAGE UI ---
st.title("🌲 Campsite Radar Concierge")
st.markdown("Automatically hunt down weekend availability and match it to your vibe.")

with st.container(border=True):
    col_month, col_weekend, col_parks = st.columns([1, 1, 2])
    
    with col_month:
        month_options = get_upcoming_months(8)
        selected_month_label = st.selectbox("🗓️ Select Month", list(month_options.keys()))
        selected_month_date = month_options[selected_month_label]
        
    with col_weekend:
        weekend_options = get_weekends_for_month(selected_month_date)
        selected_weekend_label = st.selectbox("📅 Select Weekend", list(weekend_options.keys()))
        selected_weekend = weekend_options[selected_weekend_label]

    with col_parks:
        target_parks = st.multiselect("📍 Select Parks", 
                                     ["Sanborn", "Uvas Canyon Park", "Mt Madonna Park", "Memorial County Park", "Sam McDonald Park"],
                                     default=["Sanborn"])

if st.button("🚀 Run Radar Scan", use_container_width=True, type="primary"):
    for park in target_parks:
        with st.status(f"📡 Scanning **{park}** backend...", expanded=True) as status:
            if "Memorial" in park or "McDonald" in park:
                sites_found, link = asyncio.run(check_san_mateo(selected_weekend, park))
            else:
                sites_found, link = asyncio.run(check_santa_clara(selected_weekend, park))
            
            if len(sites_found) > 0:
                park_knowledge = CAMP_KNOWLEDGE.get(park, {})
                
                # --- APPLY FILTERS ---
                approved_sites = []
                for site in sites_found:
                    site_data = park_knowledge.get(site)
                    
                    # If we have no filters active, show everything
                    if not active_target_tags:
                        approved_sites.append(site)
                        continue
                        
                    # If site is unverified but filters are ON, skip it (we can't verify if it matches)
                    if not site_data:
                        continue
                        
                    # Check if the site has ANY of the target tags
                    site_tags = set(site_data.get("tags", []))
                    if active_target_tags.intersection(site_tags):
                        approved_sites.append(site)

                # --- RENDER RESULTS ---
                if len(approved_sites) > 0:
                    status.update(label=f"✅ Found {len(approved_sites)} matching sites at {park}!", state="complete", expanded=True)
                    st.link_button(f"🏕️ Jump to Booking Page", link)
                    st.divider()
                    
                    # Render the beautiful site cards
                    for site in approved_sites:
                        site_data = park_knowledge.get(site)
                        
                        if not site_data:
                            # The "Unknown" Site Warning Box
                            st.warning(f"### ⚠️ Site {site} is available!\n*This site is unverified. Research needed.*", icon="⚠️")
                        else:
                            # The Vetted Site Card
                            with st.container(border=True):
                                # Build the header with privacy rating (default to 3 if missing)
                                privacy_stars = "🛡️" * site_data.get("privacy", 3)
                                st.markdown(f"### Site {site}  |  {privacy_stars}")
                                st.caption(f"**Vibe:** {site_data.get('vibe', 'Standard')}")
                                
                                # Pros & Cons columns
                                col_pro, col_con = st.columns(2)
                                with col_pro:
                                    st.success(f"**Best For:** {site_data.get('best_for', 'General Camping')}\n\n**Pros:** {site_data.get('pros', 'N/A')}")
                                with col_con:
                                    st.error(f"**Cons:** {site_data.get('cons', 'N/A')}")
                                
                                # Render the tags as little code blocks at the bottom
                                tags = site_data.get("tags", [])
                                st.markdown(" ".join([f"`{t}`" for t in tags]))
                else:
                    status.update(label=f"❌ {park} has openings, but none matched your filters.", state="error", expanded=False)
            else:
                status.update(label=f"❌ {park} is fully booked.", state="error", expanded=False)