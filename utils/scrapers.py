# utils/scrapers.py
import asyncio
from datetime import timedelta
from playwright.async_api import async_playwright

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

async def check_santa_clara(arrival_date, park_name):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300) 
        context = await browser.new_context()
        page = await context.new_page()
        
        url = "https://gooutsideandplay.org/reservation/camping/index.asp"
        
        try:
            await page.goto(url, wait_until="domcontentloaded")
            await asyncio.sleep(5) 

            try:
                await page.locator('.ui-dialog-titlebar-close').click(force=True, timeout=2000)
            except:
                pass 

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

            await page.evaluate("const btn = document.querySelector('button.BigBtn.AlphaBtn'); if(btn) btn.click();")
            
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