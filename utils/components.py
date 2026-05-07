# utils/components.py
import streamlit as st

def render_camp_card(site_id, data, is_unverified=False):
    # Dynamic accents based on vibe
    accent_color = "#FFC107" if is_unverified else "#4F46E5" # Yellow for unverified, Indigo default
    if "Social" in data.get('privacy_label', ''): accent_color = "#F59E0B" # Orange
    if "Balanced" in data.get('privacy_label', ''): accent_color = "#10B981" # Green
    if "Secluded" in data.get('privacy_label', ''): accent_color = "#06B6D4" # Cyan/Teal

    # Build the Tags HTML
    tags_html = "".join([f'<span class="tag"> 🌲 {t}</span>' for t in data.get('tags', [])])
    
    # Build Pros/Cons HTML (handling strings or lists safely)
    pros_data = data.get('pros', 'N/A')
    cons_data = data.get('cons', 'N/A')
    
    # If your JSON has them as lists, join them. If strings, just use them.
    if isinstance(pros_data, list): pros_html = "".join([f'<div class="pro-item">{p}</div>' for p in pros_data])
    else: pros_html = f'<div class="pro-item">{pros_data}</div>'
        
    if isinstance(cons_data, list): cons_html = "".join([f'<div class="con-item">{c}</div>' for c in cons_data])
    else: cons_html = f'<div class="con-item">{cons_data}</div>'

    html_code = f"""
    <style>
        .camp-card {{
            background: white;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
            border-top: 6px solid {accent_color};
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            position: relative;
        }}
        .unverified-badge {{
            position: absolute;
            top: 20px; right: 20px;
            background: #FEF3C7; color: #B45309;
            padding: 6px 14px; border-radius: 20px;
            font-size: 13px; font-weight: 700;
        }}
        .site-title {{ font-size: 26px; font-weight: 800; color: #111827; margin: 0 0 4px 0; }}
        .vibe-text {{ color: #6B7280; font-size: 15px; font-weight: 500; }}
        
        .privacy-row {{ display: flex; align-items: center; margin: 24px 0; }}
        .privacy-circle {{
            width: 48px; height: 48px;
            background: {accent_color};
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            color: white; font-weight: 800; font-size: 16px; margin-right: 14px;
        }}
        .privacy-label-small {{ font-size: 11px; color: #9CA3AF; font-weight: 700; letter-spacing: 1px; margin-bottom: 2px; text-transform: uppercase; }}
        .privacy-label-big {{ font-weight: 700; color: #374151; font-size: 15px; }}
        
        .grid-container {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px; }}
        .section-label {{ font-size: 12px; font-weight: 700; letter-spacing: 1px; margin-bottom: 12px; display: flex; align-items: center; }}
        .label-pro {{ color: #059669; }}
        .label-con {{ color: #DC2626; }}
        
        .pro-item {{ border-left: 3px solid #34D399; padding-left: 12px; margin-bottom: 8px; font-size: 14px; color: #4B5563; line-height: 1.5; }}
        .con-item {{ border-left: 3px solid #F87171; padding-left: 12px; margin-bottom: 8px; font-size: 14px; color: #4B5563; line-height: 1.5; }}
        
        .tag-container {{ border-top: 1px solid #F3F4F6; padding-top: 16px; display: flex; gap: 8px; flex-wrap: wrap; }}
        .tag {{ background: #F3F4F6; padding: 6px 14px; border-radius: 20px; font-size: 13px; color: #4B5563; font-weight: 500; }}
    </style>

    <div class="camp-card">
        {f'<div class="unverified-badge">⚠️ Unverified</div>' if is_unverified else ''}
        
        <div>
            <h2 class="site-title">Site {site_id} ✨</h2>
            <div class="vibe-text">{data.get('vibe', 'Standard Site')}</div>
        </div>

        <div class="privacy-row">
            <div class="privacy-circle">{data.get('privacy', '?')}/5</div>
            <div>
                <div class="privacy-label-small">PRIVACY</div>
                <div class="privacy-label-big">{data.get('privacy_label', 'Unknown')}</div>
            </div>
        </div>

        <div class="grid-container">
            <div>
                <div class="section-label label-pro">✅ PROS</div>
                {pros_html}
            </div>
            <div>
                <div class="section-label label-con">❌ CONS</div>
                {cons_html}
            </div>
        </div>

        <div class="tag-container">
            {tags_html}
        </div>
    </div>
    """
    # st.markdown(html_code, unsafe_allow_html=True)
    st.html(html_code)