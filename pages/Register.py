import streamlit as st

from backend.auth import is_strong_password, is_valid_email, register_user
from utils.helpers import apply_global_styles, init_session_state

init_session_state()
apply_global_styles()

st.markdown(
    """
    <div class="hero">
        <h2>Create Your Account</h2>
        <p>Join the studio and unlock a premium cartoonifying experience for your photos.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("register_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    submitted = st.form_submit_button("Register")

if submitted:
    clean_name = name.strip()
    clean_email = email.strip().lower()

    if not clean_name:
        st.error("Name is required.")
    elif not is_valid_email(clean_email):
        st.error("Invalid email format.")
    else:
        strong, strength_message = is_strong_password(password)
        if not strong:
            st.error(strength_message)
        elif password != confirm:
            st.error("Password and Confirm Password do not match.")
        else:
            success, message = register_user(clean_name, clean_email, password)
            if success:
                st.success(message)
                st.page_link("pages/Login.py", label="Proceed to Login")
            else:
                st.error(message)
