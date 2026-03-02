import streamlit as st

from utils.helpers import apply_global_styles, require_login

require_login()
apply_global_styles()

st.markdown(
    """
    <div class="hero">
        <h2>Cartoonify Workspace</h2>
        <p>Upload images and shape them into energetic, high-contrast cartoon renders with artistic control.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.info("Image cartoonifying controls will be added in the next task.")
st.page_link("pages/Dashboard.py", label="Back to Dashboard")
