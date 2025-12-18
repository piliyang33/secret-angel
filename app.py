import streamlit as st
import random

# --- 1. 初始化名单 ---
PARTICIPANTS = [
    "Pili", "Benny Hoa Bang", "Kieu Hanh Luong", "Madhav", 
    "Michael", "Ha Linh", "Nguyen Lan Huong", "Nhan Vat Gia Lap", 
    "Phuong Linh", "Trung Nguyen", "Do Khanh Linh", "Tran Mai Huong"
]

@st.cache_resource
def get_global_data():
    # 使用共享字典存储数据
    return {"pool": list(PARTICIPANTS), "results": {}}

data = get_global_data()

st.title("🎁 Secret Angel Draw")
st.info("Find your name and click it. Each person can only draw once!")

# 弹窗组件：显示抽签结果
@st.dialog("YOUR SECRET RESULT")
def result_dialog(user, picked):
    st.write(f"Hi {user}, you are the Secret Angel for:")
    st.title(f"✨ {picked}")
    st.write("---")
    st.warning("Please memorize it and prepare a small but creative gift for this person. Keep it a secret and close this window! Don't click on anything else please!!!")

# --- 2. 名字按钮界面 ---
cols = st.columns(2)
for i, name in enumerate(PARTICIPANTS):
    with cols[i % 2]:
        # 核心改进：检查此人是否已经存在于结果字典中
        is_done = name in data["results"]
        
        button_label = f"{name} (Done)" if is_done else name
        
        if st.button(button_label, key=name, disabled=is_done, use_container_width=True):
            # 再次双重检查，防止双击穿透
            if name not in data["results"]:
                # 排除掉自己
                temp_pool = [n for n in data["pool"] if n != name]
                
                if not temp_pool:
                    st.error("Logic Error: Only your own name is left. Admin must Reset.")
                else:
                    picked = random.choice(temp_pool)
                    # 关键操作顺序：先记录结果，再从池中移除
                    data["results"][name] = picked
                    data["pool"].remove(picked)
                    # 弹出结果
                    result_dialog(name, picked)
                    # 强制重刷新，让按钮立刻变灰禁用
                    st.rerun()
            else:
                # 如果点太快，第二次点击会进入这里，直接显示第一次的结果
                result_dialog(name, data["results"][name])

# --- 3. 管理员控制台 ---
with st.sidebar:
    st.header("Admin Controls")
    pwd = st.text_input("Admin Password", type="password")
    if pwd == "8888":
        st.write(f"Remaining in pool: {len(data['pool'])}")
        if st.button("Reset Everything"):
            data["pool"] = list(PARTICIPANTS)
            data["results"] = {}
            st.success("System Reset!")
            st.rerun()
        
        # 调试功能：管理员可以看到谁抽了谁（防止有人忘了）
        if st.checkbox("Show all assignments (Secret!)"):
            st.write(data["results"])
