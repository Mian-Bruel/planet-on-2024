import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide",
)

st.write("# Welcome to Oborniki Forest! 🌲")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This is a demo of the Oborniki route planner and social hub for your local foresters.
    """
)
