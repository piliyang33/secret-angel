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

# --- 2. 页面配置 ---
st.set_page_config(page_title="圣诞外卖抽签", page_icon="🎄")

st.markdown("""
<style>
.stApp { background-color: #F8F4E3; }
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
    box-shadow: 8px 8px 0px #165B33;
}
</style>
""", unsafe_allow_html=True)

st.title("🎄 圣诞特别派送计划")

if "my_pick" not in st.session_state:
    st.session_state.my_pick = None

# --- 3. 抽签结果显示 ---
if st.session_state.my_pick:
    picked_name = st.session_state.my_pick
    info = PARTICIPANTS_DATA[picked_name]
    st.balloons()
    
    # 使用简单拼接避免 f-string 语法错误
    html_content = '<div class="receipt">'
    html_content += '<h3 style="text-align:center; color:#D42426; border-bottom:1px solid #333; padding-bottom:10px;">🔔 订单已锁定</h3>'
    html_content += '<p style="font-size: 20px; text-align: center;"><b>收件人：' + picked_name + '</b></p>'
    html_content += '<p>----------------------------</p>'
    html_content += '<p>📍 ' + info['address'] + '</p>'
    html_content += '<p>👤 ' + info['contact'] + '</p>'
    html_content += '<p>' + info['time'] + '</p>'
    html_content += '<p>🥤 ' + info['preference'] + '</p>'
    html_content += '<p style="text-align: center; font-size: 12px; color: #666;">--- 请复制下方地址点餐 ---</p>'
    html_content += '</div>'
    
    st.markdown(html_content, unsafe_allow_html=True)
    
    st.write("👇 点击下方灰色区域一键复制：")
    st.code(info['copy_text'], language="text")
    
    if st.button("✅ 朕知道了，去点外卖"):
        st.session_state.my_pick = None
        st.rerun()
    st.write("---")

# --- 4. 按钮界面 ---
st.write("### 🎁 点击你的名字领取订单：")
cols = st.columns(2)
for i, name in enumerate(NAMES):
    with cols[i % 2]:
        is_done = name in data["results"]
        label = "🦌 " + name + " (派送中
