from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def apply_global_styles() -> None:
    css_file = PROJECT_ROOT / "assets" / "style.css"
    if css_file.exists():
        st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)


def init_session_state() -> None:
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user" not in st.session_state:
        st.session_state.user = None


def require_login() -> None:
    init_session_state()
    if not st.session_state.logged_in:
        st.warning("Please log in to access this page.")
        st.switch_page("pages/Login.py")


def logout_user() -> None:
    st.session_state.logged_in = False
    st.session_state.user = None
