import streamlit as st
import random

# --- 1. 数据配置：姓名与备注 ---
PARTICIPANTS_DATA = {
    "王子": {
        "address": "泰康集团大厦地下B1M夹层1号柜美团外卖柜",
        "contact": "王先生，13683376136",
        "time": "明天没会，随时都可以！",
        "preference": "最好是不加奶的，冷热都行，谢谢！"
    },
    "Linda": {
        "address": "北京市朝阳区将台路甲2号金尚丽外卖柜",
        "contact": "刘酸梨，17601619523",
        "time": "中午之前，下午好多会[可怜]",
        "preference": "暂无具体口味偏好"
    },
    "斌斌": {
        "address": "北京市大兴区亦城财富中心1号楼",
        "contact": "李欧森，15764500934",
        "time": "时间：上午",
        "preference": "水果都可，不要太甜，冷，不要奶茶"
    },
    "蚂蚁": {"address": "待补充", "contact": "待补充", "time": "待补充", "preference": "待补充"},
    "修源": {"address": "待补充", "contact": "待补充", "time": "待补充", "preference": "待补充"},
    "梦寒": {"address": "待补充", "contact": "待补充", "time": "待补充", "preference": "待补充"}
}

NAMES = list(PARTICIPANTS_DATA.keys())

@st.cache_resource
def get_global_data():
    return {"pool": list(NAMES), "results": {}}

data = get_global_data()

# --- 2. 页面样式设置 ---
st.set_page_config(page_title="圣诞饮料外卖抽签", page_icon="🥤")

# 圣诞风格的 CSS
st.markdown("""
    <style>
    .main { background-color: #fcfaf2; }
    .stButton>button { border-radius: 20px; height: 3em; border: 2px solid #e74c3c; font-weight: bold; }
    .order-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 10px solid #2ecc71;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎄 圣诞惊喜外卖抽签")
st.subheader("看看你要为哪位小伙伴点奶茶？")

# --- 3. 核心逻辑 ---
if "my_pick" not in st.session_state:
    st.session_state.my_pick = None

# 如果已经抽过，显示“订单详情”
if st.session_state.my_pick:
    picked_name = st.session_state.my_pick
    info = PARTICIPANTS_DATA[picked_name]
    
    st.balloons()
    st.markdown(f"""
    <div class="order-box">
        <h2 style='color: #e74c3c;'>📍 你的外卖派送任务已生成！</h2>
        <p><b>你抽中的小伙伴：</b> <span style='font-size: 24px;'>{picked_name}</span></p>
        <hr>
        <p><b>收货地址：</b> {info['address']}</p>
        <p><b>联系人：</b> {info['contact']}</p>
        <p><b>期望时间：</b> {info['time']}</p>
        <p><b>口味偏好：</b> {info['preference']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("我已截图，关闭信息"):
        st.session_state.my_pick = None
        st.rerun()
    st.write("---")

# --- 4. 按钮矩阵 ---
st.write("### 🎁 请点击你的名字开始抽签：")
cols = st.columns(2)
for i, name in enumerate(NAMES):
    with cols[i % 2]:
        is_done = name in data["results"]
        btn_label = f"✅ {name} (已参与)" if is_done else f"🥤 {name}"
        
        if st.button(btn_label, key=name, disabled=is_done, use_container_width=True):
            if name not in data["results"]:
                # 排除自己
                temp_pool = [n for n in data["pool"] if n != name]
                if not temp_pool:
                    st.error("池子空了或只剩你自己
