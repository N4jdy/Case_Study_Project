import streamlit as st

def add_custom_css():
    st.markdown(
        """
        <style>
        header {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )
