import streamlit as st
import random

# --- 1. 配置数据 ---
D = {
    "王子": {"addr": "泰康集团大厦地下B1M夹层1号柜美团柜", "name": "王先生", "tel": "13683376136", "time": "随时", "pref": "不加奶，冷热均可"},
    "Linda": {"addr": "朝阳区将台路甲2号金尚丽外卖柜", "name": "刘酸梨", "tel": "17601619523", "time": "中午前", "pref": "不加糖，去冰或热"},
    "斌斌": {"addr": "大兴区亦城财富中心1号楼", "name": "李欧森", "tel": "15764500934", "time": "上午", "pref": "水果味，不甜，不要奶茶"},
    "蚂蚁": {"addr": "西城区北京坊东区E11 PAGEONE书店", "name": "蚂先生", "tel": "13161374399", "time": "13:00-14:30", "pref": "3分糖少冰，不要纯美式/茶百道/一点点"},
    "梦寒": {"addr": "西城区炭儿胡同1号和智互动", "name": "吕先生", "tel": "17600729618", "time": "10:00左右", "pref": "热拿铁不加糖"},
    "修源": {"addr": "待补", "name": "待补", "tel": "待补", "time": "待补", "pref": "待补"}
}
NAMES = list(D.keys())

@st.cache_resource
def get_data(): return {"p": list(NAMES), "r": {}}
data = get_data()

# --- 2. UI适配 ---
st.set_page_config(page_title="圣诞抽签")
st.markdown("""<style>
.stApp { background-color: #F8F4E3 !important; }
.stApp * { color: #333 !important; }
.stButton>button { border-radius:12px; background:#D42426!important; color:#FFF!important; font-weight:bold; border:none; }
.rcp { background:#FFF; padding:15px; border:2px dashed #333; border-radius:5px; margin-bottom:10px; }
</style>""", unsafe_allow_html=True)

st.title("🎄 圣诞特别派送")

if "pick" not in st.session_state: st.session_state.pick = None

# --- 3. 抽签结果 ---
if st.session_state.pick:
    u = st.session_state.pick
    item = D[u]
    st.balloons()
    txt = f"{item['addr']} {item['name']} {item['tel']}"
    st.markdown(f"""<div class="rcp">
    <h3 style="text-align:center;color:#D42426!important;">🔔 订单锁定</h3>
    <p style="text-align:center;"><b>收件人：{u}</b></p>
    <p>📍 {item['addr']}</p>
    <p>👤 {item['name']} {item['tel']}</p>
    <p>⏰ {item['time']}</p>
    <p>🥤 {item['pref']}</p>
    </div>""", unsafe_allow_html=True)
    st.code(txt, language="text")
    if st.button("✅ 朕知道了"):
        st.session_state.pick = None
        st.rerun()

# --- 4. 按钮界面 ---
st.write("### 🎁 点击名字领取订单：")
cols = st.columns(2)
for i, n in enumerate(NAMES):
    with
