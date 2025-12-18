import streamlit as st
import random

# --- 1. 名单初始化 ---
PARTICIPANTS = [
    "Pili", "Benny Hoa Bang", "Kieu Hanh Luong", "Madhav", 
    "Michael", "Ha Linh", "Nguyen Lan Huong", "Nhan Vat Gia Lap", 
    "Phuong Linh", "Trung Nguyen", "Do Khanh Linh", "Tran Mai Huong"
]

@st.cache_resource
def get_global_data():
    return {"pool": list(PARTICIPANTS), "results": {}}

data = get_global_data()

st.set_page_config(page_title="Secret Draw", page_icon="🎁")
st.title("🎁 Secret Angel Draw")

# --- 2. 核心逻辑：处理点击 ---
# 使用 session_state 来记录当前用户点击后要显示的结果
if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "current_result" not in st.session_state:
    st.session_state.current_result = None

# --- 3. 显示抽签结果 (如果有) ---
if st.session_state.current_result:
    st.success(f"### {st.session_state.current_user}, your result is:")
    st.balloons()
    st.code(st.session_state.current_result, language="text") # 用代码框包裹，字更大且显眼
    st.warning("⚠️ Take a screenshot now! This message will disappear if the page refreshes.")
    if st.button("I have memorized it (Clear Screen)"):
        st.session_state.current_result = None
        st.session_state.current_user = None
        st.rerun()
    st.write("---")

st.info("Click YOUR NAME below to draw:")

# --- 4. 按钮矩阵 ---
cols = st.columns(2)
for i, name in enumerate(PARTICIPANTS):
    with cols[i % 2]:
        is_done = name in data["results"]
        btn_label = f"✅ {name}" if is_done else name
        
        if st.button(btn_label, key=name, disabled=is_done, use_container_width=True):
            # 再次确认没抽过
            if name not in data["results"]:
                temp_pool = [n for n in data["pool"] if n != name]
                
                if not temp_pool:
                    st.error("Logic Error: Deadlock! Contact Admin.")
                else:
                    picked = random.choice(temp_pool)
                    data["results"][name] = picked
                    data["pool"].remove(picked)
                    # 存入 session_state 用于当前页面显示
                    st.session_state.current_user = name
                    st.session_state.current_result = picked
                    st.rerun()
            else:
                # 即使被禁用了，万一穿透，直接显示已有结果
                st.session_state.current_user = name
                st.session_state.current_result = data["results"][name]
                st.rerun()

# --- 5. 管理员控制台 ---
with st.sidebar:
    st.header("Admin Settings")
    pwd = st.text_input("Password", type="password")
    if pwd == "7453":
        st.write(f"Remaining names: {len(data['pool'])}")
        if st.button("Reset Everything"):
            data["pool"] = list(PARTICIPANTS)
            data["results"] = {}
            st.session_state.current_result = None
            st.rerun()
        if st.checkbox("Check all results"):
            st.write(data["results"])
