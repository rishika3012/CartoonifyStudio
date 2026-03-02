import streamlit as st

from utils.helpers import apply_global_styles, init_session_state

init_session_state()
apply_global_styles()

st.markdown(
    """
    <div class="hero">
        <h2>Welcome</h2>
        <p>Jump into a bold cartoonifying workflow and turn ordinary photos into expressive art.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/Register.py", label="Create Account")
with col2:
    if st.session_state.logged_in:
        st.page_link("pages/Dashboard.py", label="Go to Dashboard")
    else:
        st.page_link("pages/Login.py", label="Login")
