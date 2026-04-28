import streamlit as st
from PIL import Image

# Set a more attractive page configuration
st.set_page_config(
    layout="wide",
    page_title="FitSync",
    page_icon="💪"
)

# Use custom CSS and HTML for styling
st.markdown(
    """
    <style>
    .main-container {
        background-color: #f0f2f6;
        padding: 30px;
    }
    .title {
        color: #FF4B4B;
        font-family: 'Arial Black', Gadget, sans-serif;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        color: #333333;
        margin-bottom: 40px;
        text-align: center;
    }
    .description {
        font-size: 16px;
        margin-top: 0px;
        margin-bottom: 20px;
        color: #555555;
    }
    </style>
    <div class="main-container">
        <h1 class="title">Welcome to FitSync</h1>
        <h3 class="subtitle">Your Personal Health Analytics Dashboard</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Provide a brief introductory text with enhanced styling
description = """
FitSync helps you seamlessly monitor and analyze your key health metrics.
Navigate through our intuitive interface using the sidebar and gain insights
into your daily activities and health scores.
"""
st.markdown(f'<p class="description">{description}</p>', unsafe_allow_html=True)

# Encourage navigation through the app
st.markdown(
    "<h3 style='text-align: center;'>*Use the sidebar to navigate between pages*</h3>",
    unsafe_allow_html=True
)

