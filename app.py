import streamlit as st
import random

PARTICIPANTS = [
    "Pili", "Benny Hoa Bang", "Kieu Hanh Luong", "Madhav", 
    "Michael", "Ha Linh", "Nguyen Lan Huong", "Nhan Vat Gia Lap", 
    "Phuong Linh", "Trung Nguyen", "Do Khanh Linh", "Tran Mai Huong"
]

@st.cache_resource
def get_global_data():
    return {"pool": list(PARTICIPANTS), "results": {}}

data = get_global_data()

st.title("🎁 Secret Angel Draw")
st.info("Find your name and click it. Only you will see the result!")

@st.dialog("YOUR SECRET RESULT")
def result_dialog(user, picked):
    st.write(f"Hi {user}, you are the Secret Santa for:")
    st.title(f"✨ {picked}")
    st.write("---")
    st.warning("Please memorize it or take a screenshot. This window will close!")

# 按钮布局
cols = st.columns(2)
for i, name in enumerate(PARTICIPANTS):
    with cols[i % 2]:
        is_done = name in data["results"]
        if st.button(f"{name}", key=name, disabled=is_done, use_container_width=True):
            temp_pool = [n for n in data["pool"] if n != name]
            if not temp_pool:
                st.error("Deadlock! The last person left is you. Admin must Reset.")
            else:
                picked = random.choice(temp_pool)
                data["pool"].remove(picked)
                data["results"][name] = picked
                result_dialog(name, picked)

# 管理员区域
with st.sidebar:
    pwd = st.text_input("Admin Password", type="password")
    if pwd == "8888":
        if st.button("Reset Everything"):
            data["pool"] = list(PARTICIPANTS)
            data["results"] = {}
            st.rerun()
