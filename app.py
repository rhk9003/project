import streamlit as st
import plotly.graph_objects as go

# ============================================
# 頁面設定
# ============================================
st.set_page_config(
    page_title="Dennis's Strategic Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# 設計系統 (Design System)
# ============================================
COLORS = {
    "primary": "#1e40af",       # 深藍主色
    "primary_light": "#3b82f6", # 亮藍
    "accent": "#0ea5e9",        # 天藍強調
    "success": "#059669",       # 綠色
    "warning": "#d97706",       # 橙色
    "danger": "#dc2626",        # 紅色
    "text": "#1e293b",          # 主文字
    "text_muted": "#64748b",    # 次要文字
    "bg": "#f8fafc",            # 背景
    "card": "#ffffff",          # 卡片背景
    "border": "#e2e8f0",        # 邊框
}

st.markdown(f"""
<style>
    /* ===== 全域設定 ===== */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;600;700&display=swap');
    
    .stApp {{
        background: linear-gradient(135deg, {COLORS["bg"]} 0%, #e0e7ff 100%);
        font-family: 'Noto Sans TC', sans-serif;
    }}
    
    /* ===== 卡片系統 ===== */
    .card {{
        background: {COLORS["card"]};
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 24px;
        border: 1px solid {COLORS["border"]};
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        transition: all 0.3s ease;
    }}
    .card:hover {{
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        transform: translateY(-2px);
    }}
    
    /* ===== 標題系統 ===== */
    .section-title {{
        color: {COLORS["primary"]};
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0 0 20px 0;
        padding-left: 16px;
        border-left: 4px solid {COLORS["accent"]};
        line-height: 1.4;
    }}
    .section-subtitle {{
        color: {COLORS["text"]};
        font-size: 1.15rem;
        font-weight: 600;
        margin: 16px 0 12px 0;
    }}
    
    /* ===== 標籤系統 ===== */
    .tag {{
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 2px 4px 2px 0;
    }}
    .tag-primary {{ background: #dbeafe; color: {COLORS["primary"]}; }}
    .tag-success {{ background: #d1fae5; color: {COLORS["success"]}; }}
    .tag-warning {{ background: #fef3c7; color: {COLORS["warning"]}; }}
    .tag-danger {{ background: #fee2e2; color: {COLORS["danger"]}; }}
    
    /* ===== KPI 卡片 ===== */
    div[data-testid="metric-container"] {{
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 1px solid {COLORS["border"]};
        padding: 16px 20px;
        border-radius: 12px;
        text-align: center;
    }}
    div[data-testid="metric-container"] label {{
        color: {COLORS["text_muted"]} !important;
        font-weight: 500 !important;
    }}
    div[data-testid="metric-container"] [data-testid="stMetricValue"] {{
        color: {COLORS["primary"]} !important;
        font-weight: 700 !important;
    }}
    
    /* ===== 流程箭頭 ===== */
    .flow-arrow {{
        text-align: center;
        font-size: 28px;
        color: {COLORS["accent"]};
        margin: 8px 0;
        opacity: 0.7;
    }}
    
    /* ===== 階段卡片 ===== */
    .phase-card {{
        background: {COLORS["card"]};
        border-radius: 12px;
        padding: 20px 24px;
        margin: 12px 0;
        border-left: 5px solid;
    }}
    .phase-validation {{ border-color: {COLORS["primary"]}; background: linear-gradient(90deg, #eff6ff 0%, white 20%); }}
    .phase-positioning {{ border-color: {COLORS["warning"]}; background: linear-gradient(90deg, #fffbeb 0%, white 20%); }}
    .phase-harvest {{ border-color: {COLORS["success"]}; background: linear-gradient(90deg, #ecfdf5 0%, white 20%); }}
    
    .phase-title {{
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 8px;
    }}
    .phase-validation .phase-title {{ color: {COLORS["primary"]}; }}
    .phase-positioning .phase-title {{ color: {COLORS["warning"]}; }}
    .phase-harvest .phase-title {{ color: {COLORS["success"]}; }}
    
    /* ===== 資訊區塊 ===== */
    .info-block {{
        background: #f0f9ff;
        border: 1px solid #bae6fd;
        border-radius: 10px;
        padding: 16px 20px;
        margin: 12px 0;
    }}
    .success-block {{
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        border-radius: 10px;
        padding: 16px 20px;
        margin: 12px 0;
    }}
    .warning-block {{
        background: #fefce8;
        border: 1px solid #fde047;
        border-radius: 10px;
        padding: 16px 20px;
        margin: 12px 0;
    }}
    .danger-block {{
        background: #fef2f2;
        border: 1px solid #fecaca;
        border-radius: 10px;
        padding: 16px 20px;
        margin: 12px 0;
    }}
    
    /* ===== 側邊欄 ===== */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {COLORS["primary"]} 0%, #1e3a8a 100%);
    }}
    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}
    section[data-testid="stSidebar"] .stRadio label {{
        background: rgba(255,255,255,0.1);
        padding: 10px 14px;
        border-radius: 8px;
        margin: 4px 0;
        transition: all 0.2s;
    }}
    section[data-testid="stSidebar"] .stRadio label:hover {{
        background: rgba(255,255,255,0.2);
    }}
    
    /* ===== 連結樣式 ===== */
    a {{
        color: {COLORS["accent"]} !important;
        text-decoration: none;
        font-weight: 500;
    }}
    a:hover {{
        text-decoration: underline;
    }}
</style>
""", unsafe_allow_html=True)


# ============================================
# 元件函數 (Reusable Components)
# ============================================

def card_start():
    """開始一個卡片區塊"""
    st.markdown('<div class="card">', unsafe_allow_html=True)

def card_end():
    """結束一個卡片區塊"""
    st.markdown('</div>', unsafe_allow_html=True)

def section_title(text: str, icon: str = ""):
    """統一的區塊標題"""
    display = f"{icon} {text}" if icon else text
    st.markdown(f'<h2 class="section-title">{display}</h2>', unsafe_allow_html=True)

def section_subtitle(text: str):
    """統一的次標題"""
    st.markdown(f'<p class="section-subtitle">{text}</p>', unsafe_allow_html=True)

def tag(text: str, variant: str = "primary"):
    """標籤元件，variant: primary/success/warning/danger"""
    return f'<span class="tag tag-{variant}">{text}</span>'

def kpi_row(items: list):
    """
    統一的 KPI 列表
    items: [{"label": str, "value": str, "delta": str|None, "caption": str|None}, ...]
    """
    cols = st.columns(len(items))
    for col, item in zip(cols, items):
        with col:
            st.metric(
                label=item.get("label", ""),
                value=item.get("value", ""),
                delta=item.get("delta")
            )
            if item.get("caption"):
                st.caption(item["caption"])

def info_block(content: str, variant: str = "info"):
    """資訊區塊，variant: info/success/warning/danger"""
    st.markdown(f'<div class="{variant}-block">{content}</div>', unsafe_allow_html=True)

def phase_card(title: str, content: str, variant: str = "validation"):
    """階段卡片，variant: validation/positioning/harvest"""
    st.markdown(f'''
    <div class="phase-card phase-{variant}">
        <div class="phase-title">{title}</div>
        <div>{content}</div>
    </div>
    ''', unsafe_allow_html=True)

def flow_arrow():
    """流程箭頭"""
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)


# ============================================
# 側邊欄
# ============================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    st.title("Dennis")
    st.markdown("**資深數位轉型與全通路行銷顧問**")
    st.markdown("---")
    
    page = st.radio(
        "專案經歷導覽",
        [
            "🏠 戰略總覽",
            "🏢 SaaS 解決方案 (B2B)",
            "👠 鞋業品牌 & 小白鞋專案",
            "👗 女裝品牌 (OMO)",
            "📱 3C/Apple 全通路 & SEO",
            "💊 保健食品 (受規管產業)"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.info("💡 建議使用電腦瀏覽以獲得最佳體驗")


# ============================================
# 頁面 1: 戰略總覽
# ============================================
if page == "🏠 戰略總覽":
    st.title("🚀 戰略總覽 Executive Summary")
    
    # 個人定位卡片
    card_start()
    section_title("個人定位", "👤")
    st.markdown("""
    **資深數位轉型與全通路行銷顧問**
    
    擅長結合「商業策略邏輯」與「數據驅動行銷」，在 SaaS、零售、時尚、3C 與保健食品等多個領域均有從 0 到 1 或轉虧為盈的成功實戰經驗。
    
    專精於 **OMO 虛實整合**、**複雜進銷存管理**、以及 **高投報率 (High ROAS) 的廣告與 SEO 內容佈局**。
    """)
    card_end()
    
    # 三大核心能力
    cols = st.columns(3)
    
    with cols[0]:
        card_start()
        section_title("數據驅動", "📊")
        st.markdown("""
        - ROAS 優化操盤
        - CPA 成本控制
        - 庫存迴轉率分析
        """)
        card_end()
    
    with cols[1]:
        card_start()
        section_title("策略佈局", "🎯")
        st.markdown("""
        - SEO 關鍵字霸榜
        - OMO 虛實整合
        - 內容生態系建構
        """)
        card_end()
    
    with cols[2]:
        card_start()
        section_title("逆境突圍", "⚡")
        st.markdown("""
        - 法規受限突破 (保健)
        - 資源匱乏營運 (3C)
        - 組織衝突協調 (傳產)
        """)
        card_end()


# ============================================
# 頁面 2: SaaS
# ============================================
elif page == "🏢 SaaS 解決方案 (B2B)":
    st.title("🏢 SaaS 解決方案 (B2B)")
    
    # 任務與挑戰
    card_start()
    section_title("任務與挑戰", "1️⃣")
    
    col1, col2 = st.columns(2)
    with col1:
        section_subtitle("🎯 主要任務")
        st.write("在多元廣告管道成本上升的風險下，維持獲客平衡與增長。")
    
    with col2:
        section_subtitle("⚠️ 核心挑戰")
        st.markdown(f"""
        {tag("信任門檻高", "danger")} B2B 商業模式屬性，難以讓 KOL 願意選邊站進行背書推薦。
        
        {tag("廣告成本飆升", "danger")} 傳統投放效益遞減。
        """, unsafe_allow_html=True)
    card_end()
    
    # 關鍵作為
    card_start()
    section_title("關鍵作為：內容生態系建構", "2️⃣")
    
    col1, col2 = st.columns(2)
    with col1:
        info_block("""
        <strong>🤝 內容共創 (Content Co-creation)</strong><br><br>
        邀請電商圈意見領袖「共筆」，產出「網路開店前應準備事項」等高價值內容，降低直接背書的門檻，建立專業連結。
        """, "info")
    
    with col2:
        info_block("""
        <strong>📢 第三方授權 (Whitelisting Ads)</strong><br><br>
        邀約 D2C 部落客撰寫真實試用清單，並取得「廣告主權限」以第三方名義投放廣告，建立信任背書。
        """, "success")
    card_end()
    
    # 關鍵成就
    card_start()
    section_title("關鍵成就", "3️⃣")
    kpi_row([
        {"label": "CPA 成本", "value": "-50%", "delta": "iOS14 衝擊下逆勢降低", "caption": "名單獲取成本砍半"},
        {"label": "SEO 霸榜", "value": "Top 1", "delta": "搜尋版面壟斷", "caption": "拿下 KOL 姓名搜尋結果"},
        {"label": "自主擴散", "value": "Viral", "delta": "KOL 主動分享", "caption": "於個人頁面與社團轉發"},
    ])
    card_end()


# ============================================
# 頁面 3: 鞋業品牌
# ============================================
elif page == "👠 鞋業品牌 & 小白鞋專案":
    st.title("👠 鞋業品牌：品牌年輕化與轉型")
    st.caption("含重點專案：小白鞋上市計畫")
    
    # Part 1: 整體營運
    card_start()
    section_title("品牌整體營運", "1️⃣")
    
    col1, col2 = st.columns(2)
    with col1:
        section_subtitle("⚠️ 結構性挑戰")
        st.markdown(f"""
        {tag("客群老化", "danger")} 基本盤嚴重老化且持續衰退
        
        {tag("網購門檻", "danger")} 鞋碼尺寸問題導致決策困難
        
        {tag("定價僵固", "danger")} 全通路均一價，無法差別定價
        
        {tag("組織衝突", "danger")} 線上線下通路敵對意識
        """, unsafe_allow_html=True)
    
    with col2:
        section_subtitle("⚔️ 營運作為")
        st.markdown("""
        1. **場景化導購**：重構官網分類（上班鞋、護士鞋、電商限定），解決選鞋焦慮
        2. **全通路波段**：在均一價限制下，設計精密的「全通路折扣波段」，平衡各通路利益
        """)
    
    st.divider()
    
    section_subtitle("🏆 品牌整體績效")
    kpi_row([
        {"label": "常態 ROAS", "value": "5.0", "delta": "非大檔期間", "caption": "80% 新客結構下達成"},
        {"label": "大檔 ROAS", "value": "10.0", "delta": "促銷期間", "caption": "爆發力驗證"},
        {"label": "常態月營收", "value": "100萬", "delta": "穩定貢獻", "caption": "達成百萬級營收"},
    ])
    card_end()
    
    # Part 2: 小白鞋專案
    st.markdown("---")
    
    card_start()
    section_title("小白鞋專案：從 0 到市場冠軍", "2️⃣")
    st.markdown("**核心策略**：以「市場上最好穿好走的小白鞋」為價值主張，透過三階段波段堆疊聲量與銷量。")
    
    # Wave 1
    phase_card(
        "🌊 第一波：導入前期 (Validation)",
        """
        <strong>目標：</strong>市場可行性驗證 (MVP) + 累積真實評價 (Social Proof)<br>
        <strong>戰術：</strong>舉辦會員專屬試穿活動，邀請舊客體驗並分享心得<br>
        <strong>成效：</strong>在正式廣告投放前，官網已累積數十則真實好評，降低新客信任門檻
        """,
        "validation"
    )
    
    flow_arrow()
    
    # Wave 2
    phase_card(
        "🔥 第二波：導入期 (Positioning & Dual Strategy)",
        """
        <strong>目標：</strong>雙軌定調，擴大受眾池
        """,
        "positioning"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        info_block("""
        <strong>💄 感性/時尚面</strong><br>
        合作對象：《美麗佳人 Marie Claire》<br>
        訴求：打破機能鞋醜板印象，賦予時尚、好看屬性
        """, "warning")
    with col2:
        info_block("""
        <strong>🛠️ 理性/功能面</strong><br>
        合作對象：部落客、空姐 (久站族群)<br>
        訴求：詳述「好穿、耐走、不累」的具體理由
        """, "info")
    
    flow_arrow()
    
    # Wave 3
    phase_card(
        "💰 第三波：收割期 (Conversion & Harvest)",
        """
        <strong>目標：</strong>流量變現，創造銷量高峰<br>
        <strong>戰術：</strong>在聲量與信任感堆疊至高點時，搭配團購主波段操作<br>
        <strong>成效：</strong>收割前期鋪墊的聲量，創造瞬間高銷量 (Spike)
        """,
        "harvest"
    )
    
    st.divider()
    
    section_subtitle("📈 專案專屬績效")
    kpi_row([
        {"label": "月銷量", "value": "400雙", "delta": "Top 3", "caption": "全通路暢銷前三"},
        {"label": "搜尋量", "value": "No.1", "delta": "超越競品", "caption": "兩個月內反超"},
        {"label": "市佔率", "value": "High", "delta": "快速滲透", "caption": "成功打入年輕市場"},
    ])
    
    # 趨勢圖
    section_subtitle("📊 搜尋聲量與波段關聯圖")
    dates = ['M1 驗證', 'M2 鋪墊', 'M3 美麗佳人', 'M4 空姐', 'M5 團購', 'M6 續航']
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates, y=[20, 22, 18, 15, 12, 10],
        name='競品 A',
        line=dict(color='#94a3b8', dash='dot', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=dates, y=[30, 28, 25, 22, 20, 18],
        name='競品 B',
        line=dict(color='#cbd5e1', dash='dot', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=dates, y=[5, 15, 35, 60, 120, 90],
        name='DK 小白鞋',
        line=dict(color=COLORS["primary"], width=4),
        fill='tozeroy',
        fillcolor='rgba(30, 64, 175, 0.1)'
    ))
    
    fig.add_annotation(x='M3 美麗佳人', y=35, text="定調期", showarrow=True, arrowhead=2, arrowcolor=COLORS["warning"])
    fig.add_annotation(x='M5 團購', y=120, text="收割期", showarrow=True, arrowhead=2, arrowcolor=COLORS["success"])
    
    fig.update_layout(
        title=None,
        height=350,
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='#e2e8f0')
    
    st.plotly_chart(fig, use_container_width=True)
    card_end()


# ============================================
# 頁面 4: 女裝品牌
# ============================================
elif page == "👗 女裝品牌 (OMO)":
    st.title("👗 女裝品牌：OMO 轉型與內容資產")
    
    # 嚴峻現況
    card_start()
    section_title("嚴峻現況", "1️⃣")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        {tag("數據斷層", "danger")} 除 VIP 外，一般消費皆為「未登入結帳」，無法累積會員數據
        
        {tag("零留存", "danger")} 官網回購率接近 0%
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        {tag("庫存災難", "danger")} 線上線下庫存未同步，導致大量訂單被迫取消、退貨
        
        {tag("資源匱乏", "danger")} 常態業績不足 1 萬/月，且無任何網紅預算
        """, unsafe_allow_html=True)
    card_end()
    
    # 關鍵作為
    card_start()
    section_title("關鍵作為", "2️⃣")
    
    section_subtitle("🛠️ 營運重整")
    st.markdown("""
    - 導入 OMO 系統與進銷存報表，解決庫存不同步
    - 重建會員制度，強制/引導綁定 LineOA
    """)
    
    section_subtitle("📖 OH! HER Story 主題企劃")
    info_block("""
    <strong>策略：一次專訪，多元應用</strong><br><br>
    專訪素人/職人轉化為女性職涯與穿搭內容，同步作為廣告素材與 SEO 佈局。
    """, "info")
    card_end()
    
    # 轉型成果
    card_start()
    section_title("轉型成果", "3️⃣")
    kpi_row([
        {"label": "月營收", "value": "20萬", "delta": "20x Growth", "caption": "從 <1萬 成長至 20萬"},
        {"label": "回購佔比", "value": "25%", "delta": "Up from 0%", "caption": "成功建立會員忠誠度"},
        {"label": "SEO", "value": "SERP", "delta": "人名霸榜", "caption": "拿下受訪者關鍵字"},
    ])
    card_end()


# ============================================
# 頁面 5: 3C/Apple
# ============================================
elif page == "📱 3C/Apple 全通路 & SEO":
    st.title("📱 3C & Apple：複雜通路營運")
    
    # 資源與環境限制
    card_start()
    section_title("資源與環境限制", "1️⃣")
    st.markdown(f"""
    {tag("錯失紅利", "danger")} 入職時已過 iPhone 新機發布熱度期，且多數商品尚未上架
    
    {tag("人力極簡", "danger")} 電商 2 人需維護 7 個線上通路；行銷 3 人需負責全通路、二手主機、自有/代理品牌
    
    {tag("非標品控管", "danger")} 二手主機規格非標準化，進銷存管理、定價與上架難度極高
    """, unsafe_allow_html=True)
    card_end()
    
    # 關鍵作為
    card_start()
    section_title("關鍵作為：精準 SEO 與整合", "2️⃣")
    
    col1, col2 = st.columns(2)
    with col1:
        info_block("""
        <strong>🔍 SEO 佈局</strong><br><br>
        針對「二手 Mac 價格」、「二手 Mac 年份」、「二手 Mac 規格」等高購買意圖關鍵字，佔據搜尋結果第一名。
        """, "info")
    with col2:
        info_block("""
        <strong>🔄 全通路整合</strong><br><br>
        優化多平台營運流程，克服非標品上架難題。
        """, "success")
    card_end()
    
    # 逆勢成長績效
    card_start()
    section_title("逆勢成長績效", "3️⃣")
    kpi_row([
        {"label": "全通路", "value": "達標", "delta": "Jan 2025", "caption": "淡季逆勢達成"},
        {"label": "Shopee", "value": "89萬", "delta": "YoY +324%", "caption": "單月營收爆發"},
        {"label": "ROAS", "value": "3.0", "delta": "From 1.0", "caption": "廣告成效優化"},
        {"label": "關鍵字", "value": "Top 1", "delta": "SEO", "caption": "二手 Mac 價格/規格"},
    ])
    card_end()


# ============================================
# 頁面 6: 保健食品
# ============================================
elif page == "💊 保健食品 (受規管產業)":
    st.title("💊 保健食品：法規突圍與痛點行銷")
    
    # 法規挑戰
    card_start()
    section_title("法規挑戰", "1️⃣")
    info_block("""
    <strong>⛔ 無法使用 PAS 銷售公式</strong><br><br>
    受限於法規，不能直接將產品宣稱為病痛的解決方案 (Solution)，亦不可涉及療效宣稱 (Medical Claims)。
    """, "danger")
    card_end()
    
    # 解法
    card_start()
    section_title("解法：Non-branding 內容漏斗", "2️⃣")
    st.markdown("""
    - **漏斗重構**：重建 B 群行銷漏斗，以衛教知識為入口
    - **利基痛點**：鎖定具體痛點（如「嘴破」、「肌醇」）進行內容佈局，避開法規紅線但滿足搜尋意圖
    """)
    card_end()
    
    # 執行成效
    card_start()
    section_title("執行成效", "3️⃣")
    kpi_row([
        {"label": "常態 ROAS", "value": "3.0+", "delta": "優於業界", "caption": "穩定獲利"},
        {"label": "非大檔 ROAS", "value": "5.0", "delta": "成效顯著", "caption": "精準流量變現"},
        {"label": "關鍵字", "value": "Top 5", "delta": "嘴破/肌醇", "caption": "自然流量主要入口"},
    ])
    st.caption("文章至今仍是全站自然流量前三高的 Landing Page")
    card_end()
    
    # 實績連結
    card_start()
    section_title("實績連結", "🔗")
    st.markdown("""
    - [嘴破很煩？6 個你該知道的舒緩與預防方法](https://www.lovitafood.com.tw/blog/posts/mouth-ulcer-relief-and-prevention-6-tips)
    - [肌醇是什麼？10 個關於肌醇大家都在問的問題](https://www.lovitafood.com.tw/blog/posts/inositol-10-faqs)
    - [嘴破常補 B 群還是不好？破解營養補充迷思](https://www.lovitafood.com.tw/blog/posts/mouth-ulcers-b-complex-supplement-myths)
    """)
    card_end()


# ============================================
# 頁尾
# ============================================
st.markdown("---")
st.caption("© 2025 Dennis | Strategic Portfolio | Built with Streamlit")
