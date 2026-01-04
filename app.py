import streamlit as st

# 設定頁面配置
st.set_page_config(
    page_title="Dennis's Strategic Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自訂 CSS 讓介面更乾淨專業
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stExpander {
        background-color: white;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .highlight-box {
        background-color: #e8f4f8;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3498db;
        margin-bottom: 20px;
    }
    .metric-box {
        text-align: center;
        padding: 10px;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 側邊欄導航
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # 示意圖示
    st.title("Dennis's Portfolio")
    st.markdown("**資深數位轉型與全通路行銷顧問**")
    st.markdown("---")
    
    selected_page = st.radio(
        "專案經歷導覽",
        ["戰略總覽 (Summary)", 
         "SaaS 解決方案 (B2B)", 
         "鞋業品牌 & 小白鞋專案", 
         "女裝品牌 (OMO)", 
         "3C/Apple 全通路 & SEO", 
         "保健食品 (受規管產業)"]
    )
    
    st.markdown("---")
    st.caption("Designed with Streamlit")

# --- 頁面內容邏輯 ---

def render_metric(label, value, delta=None, help_text=None):
    st.metric(label=label, value=value, delta=delta, help=help_text)

# 1. 戰略總覽
if selected_page == "戰略總覽 (Summary)":
    st.title("戰略總覽 Executive Summary")
    st.markdown("""
    > **擅長結合「商業策略邏輯」與「數據驅動行銷」**
    > 
    > 在 SaaS、零售、時尚、3C 與保健食品等多個領域均有從 0 到 1 或轉虧為盈的成功實戰經驗。
    > 專精於 **OMO 虛實整合**、**複雜進銷存管理**、以及**高投報率 (High ROAS) 的廣告與 SEO 內容佈局**。
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📊 **數據驅動**\n\nROAS 優化、CPA 減半、庫存迴轉率分析")
    with col2:
        st.success("🎯 **策略佈局**\n\nSEO 霸榜、OMO 轉型、內容生態系建構")
    with col3:
        st.warning("⚡ **逆境突圍**\n\n法規受限突破、資源匱乏運營、組織衝突協調")

# 2. SaaS
elif selected_page == "SaaS 解決方案 (B2B)":
    st.title("🏢 SaaS 解決方案 (B2B)")
    st.subheader("核心任務：多元管道平衡廣告成本上升之風險")
    
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.error("### 主要挑戰")
            st.markdown("""
            * **信任門檻高**：B2B 型態難以讓意見領袖願意站邊推薦。
            * **成本上升**：廣告流量成本持續攀升。
            """)
        with col2:
            st.success("### 關鍵作為 (Solution)")
            st.markdown("""
            1. **內容共創 (Co-creation)**：邀請電商圈意見領袖共筆「網路開店前應該準備的事情」，降低背書門檻，創造高價值內容。
            2. **第三方授權 (Whitelisting)**：邀約 D2C 部落客撰寫真實試用清單，並取得廣告主權限投放廣告，建立信任背書。
            """)

    st.markdown("### 🏆 關鍵成就")
    c1, c2, c3 = st.columns(3)
    c1.metric("自主擴散", "KOL 主動分享", "內容行銷")
    c2.metric("搜尋版面", "SERP 霸榜", "意見領袖姓名")
    c3.metric("CPA 成本", "-50%", "iOS14 衝擊下逆勢降低")

# 3. 鞋業品牌
elif selected_page == "鞋業品牌 & 小白鞋專案":
    st.title("👠 鞋業品牌：年輕化與全通路轉型")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 主要挑戰")
        st.warning("""
        * **客群老化**：基本盤衰退。
        * **網購門檻**：鞋碼尺寸導致決策難。
        * **定價僵固**：全通路均一價，無法差別定價。
        * **組織衝突**：**線上線下通路敵對意識**。
        """)
    with col2:
        st.markdown("#### 關鍵作為")
        st.info("""
        * **場景化導購**：重構官網分類（上班鞋、護士鞋、電商限定）。
        * **全通路波段**：設計精密的折扣波段，平衡利益。
        * **新品策略**：啟動小白鞋上市專案。
        """)

    st.markdown("---")
    
    # 小白鞋專案獨立區塊
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.header("✨ 重點專案：小白鞋上市計畫")
    st.markdown("**核心策略：以「市場上最好穿好走的小白鞋」切入市場**")
    
    tab1, tab2, tab3 = st.tabs(["🚀 階段一：導入前期", "🔥 階段二：導入期 (雙軌)", "💰 階段三：收割期"])
    
    with tab1:
        st.subheader("MVP 驗證與口碑累積")
        st.markdown("- **會員專屬活動**：邀請會員試穿與心得分享。")
        st.markdown("- **目的**：市場可行性驗證 + 累積真實評價 (Social Proof)。")
        
    with tab2:
        st.subheader("雙軌定調策略")
        c_a, c_b = st.columns(2)
        with c_a:
            st.markdown("#### 💄 感性/時尚面")
            st.markdown("- **合作對象**：《美麗佳人》")
            st.markdown("- **訴求**：賦予時尚、好看屬性。")
        with c_b:
            st.markdown("#### 🛠️ 理性/功能面")
            st.markdown("- **合作對象**：部落客、**空姐** (久站族群)")
            st.markdown("- **訴求**：詳述「好穿、耐走」的具體理由。")
            
    with tab3:
        st.subheader("銷量爆發")
        st.markdown("- **戰術**：搭配團購波段。")
        st.markdown("- **結果**：創造銷量與聲量雙高峰。")
    
    st.markdown("#### 📈 專案績效")
    cols = st.columns(4)
    cols[0].metric("月銷量", "400 雙", "全通路 Top 3")
    cols[1].metric("新客佔比", "80%", "成功年輕化")
    cols[2].metric("常態 ROAS", "5.0", "非大檔期間")
    cols[3].metric("大檔 ROAS", "10.0", "促銷期間")
    
    st.markdown('</div>', unsafe_allow_html=True)

# 4. 女裝品牌
elif selected_page == "女裝品牌 (OMO)":
    st.title("👗 女裝品牌：OMO 轉型與內容資產")
    
    with st.expander("查看嚴峻的初始挑戰", expanded=True):
        st.markdown("""
        * **數據斷層**：購物未登入，零會員數據。
        * **零留存**：官網回購率接近 0%。
        * **庫存災難**：線上線下庫存不同步，導致大量取消與退貨。
        * **資源匱乏**：月營收不到 1 萬，**無網紅預算**。
        """)
        
    st.markdown("### 💡 破局關鍵：OH! HER Story 主題企劃")
    st.markdown("""
    * **策略**：一次專訪，多元應用（文章、貼文、廣告素材、SEO）。
    * **內容**：女性職涯議題 + 人物導向穿搭。
    * **成效**：同步拿下人名 SERP，創造免費流量。
    """)
    
    st.divider()
    
    st.subheader("轉型成果")
    m1, m2, m3 = st.columns(3)
    m1.metric("非檔期月營收", "20 萬", "20倍成長 (YoY)")
    m2.metric("回購佔比", "25%", "從 0% 提升")
    m3.metric("系統導入", "OMO/進銷存", "解決庫存問題")

# 5. 3C/Apple
elif selected_page == "3C/Apple 全通路 & SEO":
    st.title("📱 3C & Apple：複雜運營與 SEO 霸榜")
    
    st.info("背景：人力極簡 (行銷3人/電商2人) 維護 7 個通路 + 自有/代理品牌 + 二手非標品")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🛡️ 挑戰")
        st.markdown("- **錯失紅利**：入職時已過 iPhone 新機熱度期。")
        st.markdown("- **非標品控管**：二手主機規格/定價/上架難度高。")
    
    with col2:
        st.markdown("### ⚔️ 作為")
        st.markdown("- **精準 SEO**：針對二手 Mac 價格、年份、規格建立完整資料庫。")
        st.markdown("- **全通路整合**：優化多平台營運流程。")
    
    st.markdown("### 🏆 逆勢成長")
    st.markdown("""
    * **業績達標**：2025 年 1 月 (iPhone 16 衰退期) 首度達成全線上通路目標。
    * **Shopee 爆發**：單月 89 萬 (**YoY +324%**)。
    * **廣告優化**：平均 ROAS 1 → 3。
    """)
    
    st.success("🔗 **SEO 實證**：二手 Mac 價格、規格關鍵字長期霸榜 (搜尋結果第一頁)")
    st.markdown("[查看頁面範例：Second-hand Mac Prices](https://www.maclove.co/pages/second-hand-mac-prices)")

# 6. 保健食品
elif selected_page == "保健食品 (受規管產業)":
    st.title("💊 保健食品：法規突圍與痛點行銷")
    
    st.error("#### 🛑 核心挑戰：法規限制")
    st.markdown("**不能直接套用 PAS (Problem-Agitate-Solution) 銷售公式，將產品直接宣稱為病痛解決方案（醫療效能）。**")
    
    st.markdown("### ✅ 解法：Non-branding 內容漏斗")
    st.markdown("""
    1. **重建行銷漏斗**：以衛教知識為入口。
    2. **鎖定利基痛點**：針對「嘴破」、「肌醇」撰寫深度內容，避開法規紅線但滿足搜尋意圖。
    """)
    
    st.divider()
    
    st.subheader("執行成效")
    c1, c2 = st.columns(2)
    with c1:
        st.metric("ROAS (常態)", "3.0+", "優於業界平均")
        st.metric("ROAS (非大檔)", "5.0", "成效顯著")
    with c2:
        st.write("#### 🔍 SEO 關鍵字霸榜 (Top 5)")
        st.markdown("- 嘴破")
        st.markdown("- 嘴破 B 群")
        st.markdown("- 肌醇")
        st.caption("文章至今仍是全站自然流量前三高的 Landing Page")
        
    st.markdown("##### 🔗 實績連結")
    st.markdown("- [嘴破與 B 群迷思](https://www.lovitafood.com.tw/blog/posts/mouth-ulcers-b-complex-supplement-myths)")
    st.markdown("- [肌醇 10 FAQs](https://www.lovitafood.com.tw/blog/posts/inositol-10-faqs)")

# 頁尾
st.markdown("---")
st.caption("© 2025 Dennis | Strategic Portfolio")
