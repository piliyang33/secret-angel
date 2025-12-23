import streamlit as st
import random

# --- 1. 数据配置 ---
PARTICIPANTS_DATA = {
    "王子": {
        "address": "泰康集团大厦地下B1M夹层1号柜美团外卖柜",
        "contact": "王先生，13683376136",
        "time": "⏰ 明天没会，随时都可以！",
        "preference": "🥤 最好是不加奶的，冷热都行，谢谢！",
        "copy_text": "泰康集团大厦地下B1M夹层1号柜美团外卖柜 王先生 13683376136"
    },
    "Linda": {
        "address": "北京市朝阳区将台路甲2号金尚丽外卖柜",
        "contact": "刘酸梨，17601619523",
        "time": "⏰ 中午之前，下午好多会[可怜]",
        "preference": "🥤 暂无具体口味偏好",
        "copy_text": "北京市朝阳区将台路甲2号金尚丽外卖柜 刘酸梨 17601619523"
    },
    "斌斌": {
        "address": "北京市大兴区亦城财富中心1号楼",
        "contact": "李欧森，15764500934",
        "time": "⏰ 时间：上午",
        "preference": "🥤 水果都可，不要太甜，冷，不要奶茶",
        "copy_text": "北京市大兴区亦城财富中心1号楼 李欧森 15764500934"
    },
    "蚂蚁": {"address": "待补充", "contact": "待补充", "time": "待补充", "preference": "待补充", "copy_text": "待补充"},
    "修源": {"address": "待补充", "contact": "待补充", "time": "待补充", "preference": "待补充", "copy_text": "待补充"},
    "梦寒": {"address": "待补充", "contact": "待补充", "time": "待补充", "preference": "待补充", "copy_text": "待补充"}
}

NAMES = list(PARTICIPANTS_DATA.keys())

@st.cache_resource
def get_global_data():
    return {"pool": list(NAMES), "results": {}}

data = get_global_data()

# --- 2. 页面设置 & 微信黑夜模式适配 ---
st.set_page_config(page_title="圣诞抽签", page_icon="🎄")

st.markdown("""
<style>
/* 强制背景为浅色，防止黑夜模式反转 */
.stApp { 
    background-color: #F8F4E3 !important; 
}

/* 强制所有文字颜色为深灰色，防止黑夜模式下变白看不到 */
.stApp p, .stApp span, .stApp label, .stApp div, .stApp h1, .stApp h2, .stApp h3 {
    color: #333333 !important; 
}

/* 按钮样式：红色背景，白色文字 */
.stButton>button { 
    border-radius: 12px !important; 
    background-color: #D42426 !important; 
    color: #FFFFFF !important; 
    font-weight: bold !important;
    border: none !important;
}

/* 小票样式：纯白底黑字 */
.receipt { 
    background-color: #FFFFFF !important; 
    padding: 20px; 
    border: 2px dashed #333333 !important; 
    border-radius: 5px; 
}
</style>
""", unsafe_allow_html=True)

st.title("🎄 圣诞外卖派送计划")

if "my_pick" not in st.session_state:
    st.session_state.my_pick = None

# --- 3. 抽签结果 ---
if st.session_state.my_pick:
    user = st.session_state.my_pick
    info = PARTICIPANTS_DATA[user]
    st.balloons()
    
    res_html = '<div class="receipt">'
    res_html += '<h3 style="text-align:center;color:#D42
