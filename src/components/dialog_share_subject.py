import streamlit as st
from src.database.db import create_subject
import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "snapclass-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")

    qr = segno.make(join_url)

    out = io.BytesIO()

    qr.save(out, kind="png", scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div style="font-size: 1.25rem; font-weight: normal; color: #1e293b; margin-bottom: 0.5rem;">Copy Link</div>',
            unsafe_allow_html=True
        )
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info("Copy this link to share on Whatsapp or Email")

    with col2:
        st.markdown(
            '<div style="font-size: 1.25rem; font-weight: normal; color: #1e293b; margin-bottom: 0.5rem;">Scan to Join</div>',
            unsafe_allow_html=True
        )
        st.image(out.getvalue(), use_container_width=True, caption="QRCODE for class journey")