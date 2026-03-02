import streamlit as st

from backend.db import create_table
from utils.config import APP_TITLE
from utils.helpers import apply_global_styles, init_session_state

st.set_page_config(page_title=APP_TITLE, layout="wide")

apply_global_styles()
create_table()
init_session_state()

st.markdown(
    """
    <div class="hero">
        <h2>Cartoonify Studio</h2>
        <p>Funky creative lab for transforming portraits and photos into vibrant cartoon-style art.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([2, 1])
with left:
    st.subheader("Workspace")
    st.write("Use the sidebar menu for Home, Register, Login, Dashboard, and Image Transform.")

with right:
    st.subheader("Session")
    if st.session_state.logged_in and st.session_state.user:
        st.success(f"Signed in as {st.session_state.user['name']}")
    else:
        st.info("No active session")

st.markdown(
    "<p class='small-muted'>Sign in and start building stylized cartoon renders from your images.</p>",
    unsafe_allow_html=True,
)
