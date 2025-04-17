# File: modules/theming.py
import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="AI Data Explainer",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def inject_custom_css():
    st.markdown("""
        <style>
            /* Make it pop */
            .main { background-color: #f9fafb; }
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
            }
            h1, h2, h3, h4, h5, h6 {
                font-family: 'Segoe UI', sans-serif;
                color: #1f2937;
            }
            .stButton > button {
                background-color: #3b82f6;
                color: white;
                border: none;
                padding: 0.5rem 1rem;
                border-radius: 8px;
                transition: background-color 0.3s;
            }
            .stButton > button:hover {
                background-color: #2563eb;
            }
        </style>
    """, unsafe_allow_html=True)

