import streamlit as st
import random

# --- 1. 初始化全局共享池 ---
@st.cache_resource
def get_global_data():
    return {
        # 已经填入您提供的 12 个名字
        "pool": [
            "Pili", "Benny Hoa Bang", "Kieu Hanh Luong", "Madhav", 
            "Michael", "Ha Linh", "Nguyen Lan Huong", "Nhan Vat Gia Lap", 
            "Phuong Linh", "Trung Nguyen", "Do Khanh Linh", "Tran Mai Huong"
        ],
        "results": {}
    }

data = get_global_data()

st.set_page_config(page_title="Secret Name Draw", page_icon="🎯")
st.title("🎯 Secret Name Draw")
st.write("Each person can draw only once. Your result will be kept secret!")

# --- 2. 身份识别 ---
user_id = st.text_input("Enter YOUR name (to identify yourself):").strip()

if user_id:
    # 检查此人是否已抽过
    if user_id in data["results"]:
        st.warning(f"Hello {user_id}, you have already drawn a name.")
        st.success(f"The name you drew is: **{data['results'][user_id]}**")
        st.info("Please keep this secret from others!")
    else:
        # 检查池子是否还有名字
        remaining_count = len(data["pool"])
        if remaining_count > 0:
            st.info(f"Names remaining in the pool: **{remaining_count}**")
            if st.button("Draw a Name", type="primary"):
                # 随机抽取并移除
                picked = random.choice(data["pool"])
                data["pool"].remove(picked)
                
                # 记录结果
                data["results"][user_id] = picked
                
                st.balloons()
                st.success(f"Draw Successful! You picked: **{picked}**")
                st.warning("Take a screenshot or memorize it. Do not share your result!")
        else:
            st.error("Sorry, all names have already been drawn!")

# --- 3. 管理员控制台 (密码保护) ---
with st.sidebar:
    st.header("Admin Settings")
    # 您可以在这里修改密码，目前默认为 "8888"
    admin_password = st.text_input("Admin Password", type="password")
    
    if admin_password == "7453": 
        st.success("Authenticated")
        if st.button("Reset Entire Draw"):
            # 重置时重新填入这 12 个名字
            data["pool"] = [
                "Pili", "Benny Hoa Bang", "Kieu Hanh Luong", "Madhav", 
                "Michael", "Ha Linh", "Nguyen Lan Huong", "Nhan Vat Gia Lap", 
                "Phuong Linh", "Trung Nguyen", "Do Khanh Linh", "Tran Mai Huong"
            ]
            data["results"] = {}
            st.rerun()
    elif admin_password != "":
        st.error("Incorrect Password")
