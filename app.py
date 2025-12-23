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

# --- 2. 页面设置 ---
st.set_page_config(page_title="圣诞抽签", page_icon="🎄")

st.markdown("""
<style>
.stApp { background-color: #F8F4E3; }
.stButton>button { border-radius: 12px; background-color: #D42426; color: white; font-weight: bold; }
.receipt { background-color: #FFFFFF; padding: 20px; border: 2px dashed #333; border-radius: 5px; }
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
    res_html += '<h3 style="text-align:center;color:#D42426;">🔔 订单锁定</h3>'
    res_html += '<p style="text-align:center;"><b>收件人：' + str(user) + '</b></p>'
    res_html += '<p>----------------------------</p>'
    res_html += '<p>📍 ' + str(info["address"]) + '</p>'
    res_html += '<p>👤 ' + str(info["contact"]) + '</p>'
    res_html += '<p>⏰ ' + str(info["time"]) + '</p>'
    res_html += '<p>🥤 ' + str(info["preference"]) + '</p>'
    res_html += '</div>'
    
    st.markdown(res_html, unsafe_allow_html=True)
    st.code(info["copy_text"], language="text")
    
    if st.button("✅ 朕知道了"):
        st.session_state.my_pick = None
        st.rerun()

# --- 4. 按钮矩阵 ---
st.write("### 🎁 点击你的名字领取订单：")
cols = st.columns(2)
for i, n in enumerate(NAMES):
    with cols[i % 2]:
        done = n in data["results"]
        lbl = "🦌 " + n + "(派送中)" if done else "🍲 " + n
        if st.button(lbl, key=n, disabled=done, use_container_width=True):
            if n not in data["results"]:
                pool = [p for p in data["pool"] if p != n]
                if pool:
                    pick = random.choice(pool)
                    data["results"][n] = pick
                    data["pool"].remove(pick)
                    st.session_state.my_pick = pick
                    st.rerun()
                else:
                    st.error("池子错误，请联系管理员")

# --- 5. 管理员 ---
with st.sidebar:
    pwd = st.text_input("暗号", type="password")
    if pwd == "8888":
        if st.button("重置系统"):
            data["pool"] = list(NAMES)
            data["results"] = {}
            st.session_state.my_pick = None
            st.rerun()
        if st.checkbox("清单"):
            st.write(data["results"])
