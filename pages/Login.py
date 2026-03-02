import streamlit as st

from backend.auth import login_user
from utils.helpers import apply_global_styles, init_session_state

init_session_state()
apply_global_styles()

if st.session_state.logged_in:
    st.info("You are already logged in.")
    st.page_link("pages/Dashboard.py", label="Open Dashboard")

st.markdown(
    """
    <div class="hero">
        <h2>Sign In</h2>
        <p>Access your account and continue crafting your cartoon-style image collection.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("login_form"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

if submitted:
    user = login_user(email, password)
    if user:
        st.session_state.logged_in = True
        st.session_state.user = user
        st.success("Login successful.")
        st.switch_page("pages/Dashboard.py")
    else:
        st.error("Invalid email or password.")

st.page_link("pages/Register.py", label="Need an account? Register")
