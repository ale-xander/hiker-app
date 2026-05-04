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
        browser = await p.chromium.launch(headless=True) # Set to True for speed
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
                # Clean up the text to just get the site name/number
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
        # We can finally set headless=True now that the logic is bulletproof
        browser = await p.chromium.launch(headless=True, slow_mo=300) 
        context = await browser.new_context()
        page = await context.new_page()
        
        url = "https://gooutsideandplay.org/reservation/camping/index.asp"
        
        try:
            await page.goto(url, wait_until="domcontentloaded")
            await asyncio.sleep(4) 

            # 1. KILL MODAL
            await page.evaluate("document.querySelectorAll('.ui-dialog, .ui-widget-overlay').forEach(el => el.remove())")

            # 2. SELECT PARK
            park_values = {"Sanborn": "9", "Uvas Canyon Park": "10", "Mt Madonna Park": "6"}
            val = park_values.get(park_name, "9")
            await page.evaluate(f"""(v) => {{
                const sel = Array.from(document.querySelectorAll('select')).find(s => 
                    Array.from(s.options).some(o => o.value === v)
                );
                if (sel) {{ sel.value = v; sel.dispatchEvent(new Event('change')); }}
            }}""", val)

            await asyncio.sleep(3) 

            # 3. SELECT TENT
            await page.evaluate("""() => {
                const sel = Array.from(document.querySelectorAll('select')).find(s => 
                    Array.from(s.options).some(o => o.text.includes('Tent'))
                );
                if (sel) {
                    const opt = Array.from(sel.options).find(o => o.text.includes('Tent'));
                    sel.value = opt.value;
                    sel.dispatchEvent(new Event('change'));
                }
            }""")
            
            await asyncio.sleep(2)

            # 4. SYNCHRONIZED DATE INJECTION
            arrival_str = arrival_date.strftime("%m-%d-%Y")
            departure_date = arrival_date + timedelta(days=2)
            departure_str = departure_date.strftime("%m-%d-%Y")
            
            date_args = {"arr": arrival_str, "dep": departure_str}

            await page.evaluate("""(args) => {
                const arrInput = document.getElementById('camping_arrive_date');
                const depInput = document.getElementById('camping_depart_date');
                
                if (arrInput) {
                    arrInput.value = args.arr;
                    arrInput.dispatchEvent(new Event('change'));
                }
                if (depInput) {
                    depInput.value = args.dep;
                    depInput.dispatchEvent(new Event('change'));
                }
                
                const altArr = document.getElementById('Arrival_Date');
                if (altArr) altArr.value = args.arr.replace(/-/g, '/');
                const nights = document.getElementById('Nights');
                if (nights) nights.value = '2';
            }""", date_args)

            # 5. CLICK SEARCH
            await asyncio.sleep(1)
            await page.click("button.BigBtn.AlphaBtn")
            
            # 6. RESULTS EXTRACTION (The Upgrade)
            await asyncio.sleep(8) 
            
            # We now return an Array of strings instead of a number
            available_sites = await page.evaluate("""() => {
                const cards = Array.from(document.querySelectorAll('#SiteCards .card-col'));
                const sites = [];
                
                cards.forEach(card => {
                    // Check if this specific card has an active Reserve button
                    const btn = Array.from(card.querySelectorAll('button')).find(b => b.innerText.includes('Reserve') && b.style.display !== 'none');
                    
                    if (btn) {
                        // Extract the site number from the ghost_title_lg span
                        const titleEl = card.querySelector('.ghost_title_lg');
                        if (titleEl) {
                            const text = titleEl.innerText;
                            // Uses regex to pull the number after 'Site:'
                            const match = text.match(/Site:\\s*([A-Za-z0-9]+)/i);
                            if (match) {
                                sites.push(match[1]);
                            } else {
                                sites.push("Unknown Site");
                            }
                        }
                    }
                });
                return sites;
            }""")
            
            return available_sites, url

        except Exception as e:
            print(f"SCRAPER ERROR: {e}")
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
            
            # --- FRONT-END DISPLAY LOGIC ---
            if len(sites_found) > 0:
                status.update(label=f"✅ Success at {park}!", state="complete", expanded=True)
                st.success(f"### Found {len(sites_found)} sites at {park}")
                
                # Format the list of sites into nice Markdown 'Code' chips
                site_chips = " ".join([f"` Site {site} `" for site in sites_found])
                st.markdown(f"**Available Spots:**\n\n{site_chips}")
                
                # Booking button
                st.link_button(f"🏕️ Jump to Booking Page", link)
                st.divider()
            else:
                status.update(label=f"❌ {park} is fully booked.", state="error", expanded=False)

st.caption("MacBook Pro 2020 Intel • Python 3.14.4 • Radar v2.0")