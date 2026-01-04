import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- 1. 頁面設定與 CSS ---
st.set_page_config(
    page_title="Dennis's Strategic Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定義 CSS：統一使用您提供的簡報卡片風格
st.markdown("""
<style>
    /* 核心背景色 */
    .stApp { background-color: #f1f5f9; }
    
    /* 簡報卡片容器 */
    .slide-card {
        background-color: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 30px;
        border: 1px solid #e2e8f0;
    }
    
    /* 統一標題樣式 */
    h2 { color: #1e3a8a; font-weight: 700; border-left: 6px solid #3b82f6; padding-left: 15px; margin-top: 0px; margin-bottom: 20px; }
    h3 { color: #334155; margin-top: 10px; font-size: 1.3rem; font-weight: 600; }
    h4 { color: #475569; margin-top: 5px; font-weight: 600; }
    
    /* 關鍵指標樣式 */
    div[data-testid="metric-container"] {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        transition: transform 0.2s;
    }
    div[data-testid="metric-container"]:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    
    /* 標籤裝飾 */
    .tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: 600;
        margin-right: 5px;
        margin-bottom: 5px;
    }
    .tag-blue { background-color: #e0f2fe; color: #0369a1; }
    .tag-green { background-color: #dcfce7; color: #15803d; }
    .tag-red { background-color: #fee2e2; color: #b91c1c; }
    .tag-purple { background-color: #f3e8ff; color: #7e22ce; }

</style>
""", unsafe_allow_html=True)

# --- 輔助函數 ---

def render_kpi_card(title, value, delta=None, subtext=None):
    st.metric(label=title, value=value, delta=delta)
    if subtext:
        st.caption(subtext)

# --- 側邊欄導航 ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    st.title("Dennis")
    st.markdown("**資深數位轉型與全通路行銷顧問**")
    st.markdown("---")
    
    page = st.radio(
        "專案經歷導覽",
        [
            "🏠 戰略總覽 (Summary)", 
            "🏢 SaaS 解決方案 (B2B)", 
            "👠 鞋業品牌 & 小白鞋專案", 
            "👗 女裝品牌 (OMO)", 
            "📱 3C/Apple 全通路 & SEO", 
            "💊 保健食品 (受規管產業)"
        ]
    )
    
    st.markdown("---")
    st.info("💡 建議使用電腦瀏覽以獲得最佳體驗")

# ==========================================
# 頁面 1: 戰略總覽
# ==========================================
if page == "🏠 戰略總覽 (Summary)":
    st.title("戰略總覽 Executive Summary")
    
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("個人定位")
    st.markdown("""
    #### 資深數位轉型與全通路行銷顧問
    擅長結合**「商業策略邏輯」**與**「數據驅動行銷」**，在 SaaS、零售、時尚、3C 與保健食品等多個領域均有從 0 到 1 或轉虧為盈的成功實戰經驗。
    專精於 **OMO 虛實整合**、**複雜進銷存管理**、以及**高投報率 (High ROAS) 的廣告與 SEO 內容佈局**。
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="slide-card" style="height:250px">', unsafe_allow_html=True)
        st.subheader("📊 數據驅動")
        st.markdown("- ROAS 優化操盤")
        st.markdown("- CPA 成本控制")
        st.markdown("- 庫存迴轉率分析")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="slide-card" style="height:250px">', unsafe_allow_html=True)
        st.subheader("🎯 策略佈局")
        st.markdown("- SEO 關鍵字霸榜")
        st.markdown("- OMO 虛實整合")
        st.markdown("- 內容生態系建構")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="slide-card" style="height:250px">', unsafe_allow_html=True)
        st.subheader("⚡ 逆境突圍")
        st.markdown("- 法規受限突破 (保健)")
        st.markdown("- 資源匱乏運營 (3C)")
        st.markdown("- 組織衝突協調 (傳產)")
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 頁面 2: SaaS
# ==========================================
elif page == "🏢 SaaS 解決方案 (B2B)":
    st.title("SaaS 解決方案 (B2B)")
    
    # 任務與挑戰
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("1. 任務與挑戰")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🎯 主要任務")
        st.write("在多元廣告管道成本上升的風險下，維持獲客平衡與增長。")
    with c2:
        st.markdown("### ⚠️ 核心挑戰")
        st.markdown("""
        * **信任門檻高**：B2B 商業模式屬性，難以讓意見領袖 (KOL) 願意選邊站進行背書推薦。
        * **廣告成本飆升**：傳統投放效益遞減。
        """)
    st.markdown('</div>', unsafe_allow_html=True)

    # 策略與作為
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("2. 關鍵作為：內容生態系建構")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("**🤝 內容共創 (Content Co-creation)**")
        st.markdown("邀請電商圈意見領袖「共筆」，產出**「網路開店前應準備事項」**等高價值內容，降低直接背書的門檻，建立專業連結。")
    with col_b:
        st.success("**📢 第三方授權 (Whitelisting Ads)**")
        st.markdown("邀約 D2C 部落客撰寫真實試用清單，並取得**「廣告主權限」**以第三方名義投放廣告，建立信任背書。")
    st.markdown('</div>', unsafe_allow_html=True)

    # 成果
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("3. 關鍵成就")
    k1, k2, k3 = st.columns(3)
    with k1:
        render_kpi_card("CPA 成本", "-50%", "iOS14 衝擊下逆勢降低", "名單獲取成本砍半")
    with k2:
        render_kpi_card("SEO 霸榜", "Top 1", "搜尋版面壟斷", "拿下 KOL 姓名搜尋結果")
    with k3:
        render_kpi_card("自主擴散", "Viral", "KOL 主動分享", "於個人頁面與社團轉發")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 頁面 3: 鞋業品牌 (包含小白鞋專案)
# ==========================================
elif page == "👠 鞋業品牌 & 小白鞋專案":
    st.title("鞋業品牌：品牌年輕化與轉型")
    st.caption("含重點專案：小白鞋上市計畫")

    # Part 1: 整體運營
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("1. 品牌整體運營 (General Operations)")
    
    st.markdown("#### ⚠️ 結構性挑戰")
    st.markdown("""
    <span class="tag tag-red">客群老化</span> 基本盤嚴重老化且持續衰退。
    <span class="tag tag-red">網購門檻</span> 鞋碼尺寸問題導致決策困難。
    <span class="tag tag-red">定價僵固</span> 全通路均一價，無法差別定價。
    <span class="tag tag-red">組織衝突</span> **線上線下通路敵對意識**，利益分配困難。
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("#### ⚔️ 運營作為")
    st.markdown("""
    1. **場景化導購**：重構官網分類（上班鞋、護士鞋、電商限定），解決選鞋焦慮。
    2. **全通路波段**：在均一價限制下，設計精密的「全通路折扣波段」，平衡各通路利益。
    """)
    
    st.markdown("#### 🏆 品牌整體績效")
    pk1, pk2, pk3 = st.columns(3)
    with pk1:
        render_kpi_card("常態 ROAS", "5.0", "非大檔期間", "80% 新客結構下達成")
    with pk2:
        render_kpi_card("大檔 ROAS", "10.0", "促銷期間", "爆發力驗證")
    with pk3:
        render_kpi_card("常態月營收", "100萬", "穩定貢獻", "達成百萬級營收")
    st.markdown('</div>', unsafe_allow_html=True)

    # Part 2: 小白鞋專案 (獨立區塊，視覺加強)
    st.markdown("---")
    st.subheader("🚀 重點專案：小白鞋上市計畫")
    
    st.markdown('<div class="slide-card" style="border-left: 10px solid #2563eb;">', unsafe_allow_html=True)
    st.header("2. 小白鞋專案：從 0 到市場冠軍")
    st.subheader("策略核心：以「市場上最好穿好走的小白鞋」切入")
    
    # 專案三階段
    tab1, tab2, tab3 = st.tabs(["階段一：MVP 驗證", "階段二：雙軌定調", "階段三：收割爆發"])
    with tab1:
        st.info("**導入前期 (Validation)**：舉辦會員專屬試穿與心得分享活動。目的為市場可行性驗證，並預先累積真實好評 (Social Proof)。")
    with tab2:
        st.warning("**導入期 (Positioning)**：\n\n1. **感性面**：與《美麗佳人》合作，賦予時尚屬性。\n2. **理性面**：與部落客、**空姐**合作，詳述「好穿耐走」理由。")
    with tab3:
        st.success("**收割期 (Conversion)**：搭配團購波段操作，在聲量高點創造銷量高峰。")
    
    st.markdown("#### 📈 專案專屬績效 (Project KPIs)")
    spk1, spk2, spk3 = st.columns(3)
    with spk1:
        render_kpi_card("月銷量", "400雙", "Top 3", "全通路暢銷前三")
    with spk2:
        render_kpi_card("搜尋量", "No.1", "超越競品", "兩個月內反超")
    with spk3:
        render_kpi_card("市佔率", "High", "快速滲透", "成功打入年輕市場")
        
    # 模擬趨勢圖 (Plotly)
    st.markdown("#### 📊 搜尋聲量趨勢模擬")
    dates = ['M1', 'M2', 'M3', 'M4 (Launch)', 'M5', 'M6']
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=[20, 22, 18, 15, 12, 10], name='競品 A', line=dict(color='gray', dash='dot')))
    fig.add_trace(go.Scatter(x=dates, y=[30, 28, 25, 22, 20, 18], name='競品 B', line=dict(color='lightgray', dash='dot')))
    fig.add_trace(go.Scatter(x=dates, y=[5, 8, 12, 50, 85, 120], name='DK 小白鞋', line=dict(color='#2563eb', width=4)))
    fig.update_layout(title="品牌關鍵字搜尋趨勢", height=300, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 頁面 4: 女裝
# ==========================================
elif page == "👗 女裝品牌 (OMO)":
    st.title("女裝品牌：OMO 轉型與內容資產")

    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("1. 嚴峻現況")
    st.markdown("""
    * **數據斷層**：除 VIP 外，一般消費皆為「未登入結帳」，**無法累積會員數據**。
    * **零留存**：官網回購率接近 **0%**。
    * **庫存災難**：線上線下庫存未同步，導致大量訂單被迫取消、退貨。
    * **資源匱乏**：常態業績不足 1 萬/月，且廣告預算極限，**無任何網紅預算**。
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("2. 關鍵作為")
    st.subheader("基礎建設 & 內容企劃")
    
    st.markdown("**🛠️ 營運重整**")
    st.markdown("- 導入 OMO 系統與進銷存報表，解決庫存不同步。")
    st.markdown("- 重建會員制度，強制/引導綁定 LineOA。")
    
    st.markdown("**📖 OH! HER Story 主題企劃**")
    st.info("策略：一次專訪，多元應用。專訪素人/職人轉化為女性職涯與穿搭內容，同步作為廣告素材與 SEO 佈局。")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("3. 轉型成果")
    gk1, gk2, gk3 = st.columns(3)
    with gk1:
        render_kpi_card("月營收", "20萬", "20x Growth", "從 <1萬 成長至 20萬")
    with gk2:
        render_kpi_card("回購佔比", "25%", "Up form 0%", "成功建立會員忠誠度")
    with gk3:
        render_kpi_card("SEO", "SERP", "人名霸榜", "拿下受訪者關鍵字")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 頁面 5: 3C
# ==========================================
elif page == "📱 3C/Apple 全通路 & SEO":
    st.title("3C & Apple：複雜通路運營")
    
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("1. 資源與環境限制")
    st.markdown("""
    * **錯失紅利**：入職時已過 iPhone 新機發布熱度期，且多數商品尚未上架。
    * **人力極簡**：電商 2 人需維護 7 個線上通路；行銷 3 人需負責全通路、二手主機、自有/代理品牌。
    * **非標品控管**：二手主機規格非標準化，進銷存管理、定價與上架難度極高。
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("2. 關鍵作為：精準 SEO 與整合")
    col3c_1, col3c_2 = st.columns(2)
    with col3c_1:
        st.markdown("### 🔍 SEO 佈局")
        st.write("針對 **二手 Mac** 建立完整的「價格」、「年份」、「型號規格」資料庫，攔截高意圖流量。")
        st.markdown("[範例連結：Second-hand Mac Prices](#)")
    with col3c_2:
        st.markdown("### 🔄 全通路整合")
        st.write("優化多平台營運流程，克服非標品上架難題。")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("3. 逆勢成長績效")
    ck1, ck2, ck3, ck4 = st.columns(4)
    with ck1:
        render_kpi_card("全通路", "達標", "Jan 2025", "淡季逆勢達成")
    with ck2:
        render_kpi_card("Shopee", "89萬", "YoY +324%", "單月營收爆發")
    with ck3:
        render_kpi_card("ROAS", "3.0", "From 1.0", "廣告成效優化")
    with ck4:
        render_kpi_card("關鍵字", "Top 1", "SEO", "二手 Mac 價格/規格")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 頁面 6: 保健食品
# ==========================================
elif page == "💊 保健食品 (受規管產業)":
    st.title("保健食品：法規突圍與痛點行銷")
    
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("1. 法規挑戰")
    st.error("""
    **⛔ 無法使用 PAS 銷售公式**
    受限於法規，不能直接將產品宣稱為病痛的解決方案 (Solution)，亦不可涉及療效宣稱 (Medical Claims)。
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("2. 解法：Non-branding 內容漏斗")
    st.markdown("""
    * **漏斗重構**：重建 B 群行銷漏斗，以衛教知識為入口。
    * **利基痛點**：鎖定具體痛點（如「嘴破」、「肌醇」）進行內容佈局，避開法規紅線但滿足搜尋意圖。
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.header("3. 執行成效")
    hk1, hk2, hk3 = st.columns(3)
    with hk1:
        render_kpi_card("常態 ROAS", "3.0+", "優於業界", "穩定獲利")
    with hk2:
        render_kpi_card("非大檔 ROAS", "5.0", "成效顯著", "精準流量變現")
    with hk3:
        render_kpi_card("關鍵字", "Top 5", "嘴破/肌醇", "自然流量主要入口")
        
    st.caption("文章至今仍是全站自然流量前三高的 Landing Page")
    st.markdown('</div>', unsafe_allow_html=True)

# 頁尾
st.markdown("---")
st.caption("© 2025 Dennis | Strategic Portfolio | Built with Streamlit")
