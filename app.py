import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():

    st.set_page_config(

        page_title= "SnapClass - Making Attendance faster using AI",
        page_icon= "https://snapclass-landing-page-theta.vercel.app/static/img/logo.png"

    )



    # 1. Initialize session state defaults first
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None
    if "is_logged_in" not in st.session_state:
        st.session_state["is_logged_in"] = False
    if "user_role" not in st.session_state:
        st.session_state["user_role"] = None

    # 2. Handle join-code query parameter
    join_code = st.query_params.get("join-code")
    if join_code:
        if st.session_state["login_type"] != "student":
            st.session_state["login_type"] = "student"
            st.rerun()

    # 3. Screen routing
    match st.session_state["login_type"]:
        case "teacher":
            teacher_screen()
        case "student":
            student_screen()
            # Trigger enrollment dialog inside student view
            if join_code and st.session_state.get("student_data"):
                auto_enroll_dialog(join_code)
        case None:
            home_screen()

if __name__ == "__main__":
    main()