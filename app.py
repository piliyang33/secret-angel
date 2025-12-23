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
        "time": "⏰ 中午之前 下午好多会[可怜]",
        "preference": "🥤 不另外加糖（最好不是甜的）、去冰or热饮都可",
        "copy_text": "北京市朝阳区将台路甲2号金尚丽外卖柜 刘酸梨 17601619523"
    },
    "斌斌": {
        "address": "北京市大兴区亦城财富中心1号楼",
        "contact": "李欧森，15764500934",
        "time": "⏰ 时间：上午",
        "preference": "🥤 水果都可，不要太甜，冷，不要奶茶",
        "copy_text": "北京市大兴区亦城财富中心1号楼 李欧森 15764500934"
    },
    "蚂蚁": {
        "address": "北京市西城区大栅栏街道北京坊东区E11 PAGEONE书店（一层收银台）",
        "contact": "蚂先生，13161374399",
        "time": "⏰ 倾向于中午一点到两点半之间拿到",
        "preference": "🥤 不要纯美式/茶百道/一点点；茶姬不要万里木兰；三分糖，少冰，爱您！",
        "copy_text": "北京市西城区大栅栏街道北京坊东区E11 PAGEONE书店 蚂先生 13161374399"
    },
    "梦寒": {
        "address": "北京市西城区炭儿胡同1号和智互动",
        "contact": "吕先生，17600729618",
        "time": "⏰ 上午10点左右",
        "preference": "🥤 热拿铁不加糖",
        "copy_text": "北京市西城区炭儿胡同1号和智互动 吕先生 17600729618"
    },
    "修源": {
        "address": "待补充",
        "contact": "待补充",
        "time": "待补充",
        "preference": "待补充",
        "copy_text": "待补充"
    }
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
.stApp { background-color: #F8F4E3 !important; }
.stApp p, .stApp span, .stApp label, .stApp div, .stApp h1, .stApp h2, .stApp h3 {
    color: #333333 !important; 
}
.stButton>button { 
    border-radius: 12px !important; 
    background-color: #D42426 !important; 
    color: #FFFFFF !important; 
    font-weight: bold !important;
}
.receipt { 
    background-color: #FFFFFF !important; 
    padding: 20px; 
    border: 2px dashed #333333 !important; 
    border-radius: 5px; 
}
</style>
""", unsafe_allow_html=True)

st.title("🎄 圣诞外卖派送计划")

if "
