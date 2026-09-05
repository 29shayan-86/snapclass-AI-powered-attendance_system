import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
        .stApp {
            background-color: #585FF9 !important;
        }

        /* Targets column card backgrounds and sets flexbox layout */
        div[data-testid="column"],
        div[data-testid="stColumn"] {
            background-color: #E0E3FF !important;
            padding: 2.5rem 2rem !important;
            border-radius: 4rem !important;
            display: flex !important;
            flex-direction: column !important;
        }

        div[data-testid="column"] > div:first-child,
        div[data-testid="stColumn"] > div:first-child {
            display: flex !important;
            flex-direction: column !important;
            height: 100% !important;
        }

        /* Standardize image container heights */
        div[data-testid="stImage"] {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            height: 140px !important;
            margin-bottom: 1.5rem !important;
        }

        div[data-testid="stImage"] > img {
            max-height: 120px !important;
            object-fit: contain !important;
            margin: 0 auto !important;
        }

        /* Push button container to the bottom of the card */
        div[data-testid="stButton"] {
            margin-top: auto !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_background_dashboard():
    st.markdown("""
        <style>
        .stApp {
            background: #E0E3FF !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_base_layout():
    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Top Bar of Streamlit */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
            max-width: 900px !important;
        }

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            text-align: center !important;
        }

        h2, h3 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 1.7rem !important;
            line-height: 1.1 !important;
            text-align: center !important;
            margin-bottom: 1rem !important;
        }

        h4, p {
            font-family: 'Outfit', sans-serif !important;
        }

        /* Base styling for all buttons */
        div[data-testid="stButton"] > button {
            border-radius: 1.5rem !important;
            padding: 10px 24px !important;
            border: none !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 500 !important;
            width: 100% !important;
            transition: transform 0.25s ease-in-out !important;
        }

        /* =========================================
           SELECTED BUTTON - PINK
           ========================================= */
        div[data-testid="stButton"] > button[kind="primary"] {
            background-color: #ff2a75 !important;
            color: white !important;
        }

        div[data-testid="stButton"] > button[kind="primary"]:hover {
            background-color: #e02467 !important;
            color: white !important;
        }

        /* =========================================
           NORMAL / UNSELECTED BUTTON - BLACK
           ========================================= */
        div[data-testid="stButton"] > button[kind="tertiary"] {
            background-color: #000000 !important;
            color: white !important;
        }

        div[data-testid="stButton"] > button[kind="tertiary"]:hover {
            background-color: #222222 !important;
            color: white !important;
        }

        /* =========================================
           SECONDARY BUTTONS - BLUE
           ========================================= */
        div[data-testid="stButton"] > button[kind="secondary"] {
            background-color: #5865F2 !important;
            color: white !important;
        }

        div[data-testid="stButton"] > button[kind="secondary"]:hover {
            background-color: #4752C4 !important;
            color: white !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )