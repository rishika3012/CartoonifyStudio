import streamlit as st

from utils.helpers import apply_global_styles, logout_user, require_login

require_login()
apply_global_styles()

user = st.session_state.user

st.markdown(
    f"""
    <div class="hero">
        <h2>Dashboard</h2>
        <p>Welcome back, {user['name']}. Your funky cartoon art pipeline is ready.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

main_col, side_col = st.columns([2, 1])
with main_col:
    with st.container(border=True):
        st.subheader("Account Details")
        st.write(f"User ID: {user['id']}")
        st.write(f"Name: {user['name']}")
        st.write(f"Email: {user['email']}")
        st.write(f"Created At: {user['created_at']}")

with side_col:
    with st.container(border=True):
        st.subheader("Actions")
        st.page_link("pages/Image_Transform.py", label="Open Cartoonify Workspace")
        st.page_link("app.py", label="Back to Home")

if st.button("Logout"):
    logout_user()
    st.success("Logged out successfully.")
    st.switch_page("pages/Login.py")
