import streamlit as st
import random

# --- 1. 数据配置 (已去掉提示词，方便直接粘贴) ---
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

# --- 2. 深度 UI 定制 ---
st.set_page_config(page_title="圣诞外卖抽签", page_icon="🎄")

st.markdown("""
    <style>
    .stApp { background-color: #F8F4E3; }
    h1 { color: #D42426 !important; font-family: 'Courier New', Courier, monospace; }
    .stButton>button {
        border-radius: 12px;
        border: 2px solid #165B33;
        background-color: #D42426;
        color: white;
        font-weight: bold;
    }
    .receipt {
        background-color: #FFFFFF;
        padding: 20px;
        border: 2px dashed #333;
        border-radius: 5px;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: 8px 8px 0px #165B33;
    }
    .receipt-title {
        text-align: center;
        border-bottom: 2px solid #333;
        padding-bottom: 10px;
        color: #D42426;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎄 圣诞特别派送计划")
st.markdown("### 🎅 谁是今日的幸运骑手？")

if "my_pick" not in st.session_state:
    st.session_state.my_pick = None

# --- 3. 抽签结果显示 ---
if st.session_state.my_pick:
    picked_name = st.session_state.my_pick
    info = PARTICIPANTS_DATA[picked_name]
    st.balloons()
    
    st.markdown(f"""
