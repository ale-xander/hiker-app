import streamlit as st
from datetime import date, timedelta
import asyncio
from playwright.async_api import async_playwright
import re

# --- 1. DATE LOGIC ---
def get_weekends():
    weekends = []
    curr = date.today()
    for _ in range(120):
        if curr.weekday() == 4: # Friday
            weekends.append(curr)
        curr += timedelta(days=1)
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
# --- 3. SANTA CLARA DRIVER ---
# --- 3. SANTA CLARA DRIVER ---
# --- 3. SANTA CLARA DRIVER ---
async def check_santa_clara(arrival_date, park_name):
    async with async_playwright() as p:
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
                print("DEBUG: Closed alert modal.")
            except:
                pass 

            # 2. SELECT PARK (By exact text, immune to the "Nights" bug)
            print(f"DEBUG: Selecting Park: {park_name}...")
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

            # Wait for the ASP.NET server to process the park change
            await asyncio.sleep(4) 

            # 3. SELECT TENT (By text)
            print("DEBUG: Selecting Site Type: Tent...")
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
            
            # Wait for the ASP.NET server to process the Tent change
            await asyncio.sleep(4)

            # 4. INJECT ARRIVAL DATE
            arrival_str = arrival_date.strftime("%m-%d-%Y")
            departure_str = (arrival_date + timedelta(days=2)).strftime("%m-%d-%Y")
            
            print(f"DEBUG: Setting Arrival Date: {arrival_str}...")
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

            # Wait for date background validation
            await asyncio.sleep(4)

            # 5. INJECT DEPARTURE DATE & NIGHTS
            print(f"DEBUG: Setting Departure Date: {departure_str}...")
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
            print("DEBUG: Triggering Search...")
            await page.evaluate("const btn = document.querySelector('button.BigBtn.AlphaBtn'); if(btn) btn.click();")
            
            # 7. TAB DETECTION & EXTRACTION (With ADA Filter)
            print("DEBUG: Waiting for page to render results...")
            await asyncio.sleep(8) 
            
            tab_locator = page.locator(".tab-allpark")
            if await tab_locator.count() > 0:
                print("DEBUG: Tabbed layout detected! Clicking 'All Park Areas'...")
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
            
            print(f"DEBUG: Found {len(available_sites)} sites at {park_name}")
            return available_sites, url

        except Exception as e:
            print(f"SCRAPER ERROR at {park_name}: {e}")
            return [], url
        finally:
            await browser.close()




# --- 4. THE UI FRONTEND ---
st.set_page_config(page_title="Hiker Radar", page_icon="🌲", layout="centered")

st.title("🌲 Campsite Radar")
st.markdown("Automatically bypass legacy booking systems to hunt down weekend availability.")

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        selected_weekend = st.selectbox("📅 Select Weekend", get_weekends())
    with col2:
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
                status.update(label=f"✅ Success at {park}!", state="complete", expanded=True)
                st.success(f"### Found {len(sites_found)} sites at {park}")
                site_chips = " ".join([f"` Site {site} `" for site in sites_found])
                st.markdown(f"**Available Spots:**\n\n{site_chips}")
                st.link_button(f"🏕️ Jump to Booking Page", link)
                st.divider()
            else:
                status.update(label=f"❌ {park} is fully booked.", state="error", expanded=False)

st.caption("MacBook Pro 2020 Intel • Python 3.14.4 • Radar v2.0")