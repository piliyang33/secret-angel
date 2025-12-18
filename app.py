import streamlit as st
import random

# --- 1. Initialize Global Shared Pool ---
# We use cache_resource to ensure all users accessing the URL share the same data
@st.cache_resource
def get_global_data():
    return {
        # Replace these names with your actual 12 names
        "pool": [
            "Pili", "Benny Hoa Bang", "Kieu Hanh Luong", "Madhav", 
            "Michael", "Ha Linh", "Nguyen Lan Huong", "Nhan Vat Gia Lap", 
            "Phuong Linh", "Trung Nguyen", "Do Khanh Linh", "Tran Mai Huong"
        ],
        "results": {}  # Stores: { "Participant Name": "Drawn Name" }
    }

data = get_global_data()

st.set_page_config(page_title="Secret Name Draw", page_icon="🎯")
st.title("🎯 Secret Name Draw")
st.write("Each person can draw only once. Your result will be kept secret!")

# --- 2. Identity Verification ---
# Users enter their own name to "lock" their draw result
user_id = st.text_input("Enter YOUR name (to identify yourself):").strip()

if user_id:
    # Check if this person has already drawn a name
    if user_id in data["results"]:
        st.warning(f"Hello {user_id}, you have already drawn a name.")
        st.success(f"The name you drew is: **{data['results'][user_id]}**")
        st.info("Please keep this secret from others!")
    else:
        # Check if there are names left in the pool
        remaining_count = len(data["pool"])
        if remaining_count > 0:
            st.info(f"Names remaining in the pool: **{remaining_count}**")
            
            if st.button("Draw a Name", type="primary"):
                # Core logic: Randomly pick and remove from the shared pool
                picked = random.choice(data["pool"])
                data["pool"].remove(picked)
                
                # Record the result to prevent re-drawing
                data["results"][user_id] = picked
                
                st.balloons()
                st.success(f"Draw Successful! You picked: **{picked}**")
                st.warning("Take a screenshot or memorize it. Do not share your result!")
        else:
            st.error("Sorry, all names have already been drawn!")

# --- 3. Admin Tools (Sidebar) ---
with st.sidebar:
    st.header("Admin Controls")
    if st.button("Reset Entire Draw"):
        # Reset everything back to the start
        data["pool"] = [
            "Alice", "Bob", "Charlie", "David", 
            "Eve", "Frank", "Grace", "Heidi", 
            "Ivan", "Judy", "Karl", "Linda"
        ]
        data["results"] = {}
        st.rerun()
