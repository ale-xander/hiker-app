# app.py
import streamlit as st
from datetime import date, timedelta
import asyncio
from camp_data import CAMP_KNOWLEDGE
from utils.components import render_camp_card

# Pull in our backend engines!
from utils.scrapers import check_san_mateo, check_santa_clara

# --- DATE LOGIC ---
def get_upcoming_months(num_months=8):
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
    weekends = {}
    curr = target_date
    while curr.weekday() != 4:
        curr += timedelta(days=1)
    while curr.month == target_date.month:
        weekends[curr.strftime("%a, %b %d")] = curr
        curr += timedelta(days=7)
    return weekends

# --- UI FRONTEND ---
st.set_page_config(page_title="Hiker Radar", page_icon="🌲", layout="wide")

# --- SIDEBAR FILTERS ---
with st.sidebar:
    st.header("🎯 Smart Filters")
    st.markdown("Leave blank to see all available sites.")
    
    group_filter = st.multiselect(
        "Who are you camping with?", 
        ["Solo / Couple", "Single Family", "Multi-Family / Group"]
    )
    vibe_filter = st.multiselect(
        "Setting / Vibe", 
        ["Waterfalls & Creeks", "Redwoods & Quiet", "Views & Sun"]
    )

active_target_tags = set()
if "Multi-Family / Group" in group_filter: active_target_tags.update(["group-friendly", "family-hub"])
if "Single Family" in group_filter: active_target_tags.update(["family-friendly", "kid-bike-loop"])
if "Solo / Couple" in group_filter: active_target_tags.update(["quieter-loop"])
if "Waterfalls & Creeks" in vibe_filter: active_target_tags.update(["waterfall-hikes", "creekside"])
if "Redwoods & Quiet" in vibe_filter: active_target_tags.update(["redwood-forest", "quieter-loop"])
if "Views & Sun" in vibe_filter: active_target_tags.update(["view-potential", "partial-shade"])

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
                approved_sites = []
                for site in sites_found:
                    site_data = park_knowledge.get(site)
                    if not active_target_tags:
                        approved_sites.append(site)
                        continue
                    if not site_data:
                        continue
                    site_tags = set(site_data.get("tags", []))
                    if active_target_tags.intersection(site_tags):
                        approved_sites.append(site)

                if len(approved_sites) > 0:
                    status.update(label=f"✅ Found {len(approved_sites)} matching sites at {park}!", state="complete", expanded=True)
                    st.link_button(f"🏕️ Jump to Booking Page", link)
                    st.divider()
                    
                    # --- RENDER FIGMA CARDS ---
                    for site in approved_sites:
                        site_data = park_knowledge.get(site)
                        if not site_data:
                            # Pass a minimal dict for unverified sites
                            render_camp_card(site, {"vibe": "Researching..."}, is_unverified=True)
                        else:
                            render_camp_card(site, site_data)
                else:
                    status.update(label=f"❌ {park} has openings, but none matched your filters.", state="error", expanded=False)
            else:
                status.update(label=f"❌ {park} is fully booked.", state="error", expanded=False)