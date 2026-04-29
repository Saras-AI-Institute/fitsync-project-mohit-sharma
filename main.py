import streamlit as st
from PIL import Image

st.set_page_config(
    layout="wide",
    page_title="FitSync",
    page_icon="💪"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
body {
    background-color: #f7f9fc;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #FF4B4B;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #555;
    margin-bottom: 30px;
}

.section-title {
    font-size: 32px;
    font-weight: bold;
    color: #333;
    margin-top: 40px;
}

.card {
    background-color: black;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    text-align: center;
}

.description {
    font-size: 18px;
    color: #444;
    text-align: center;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HERO SECTION --------------------
st.markdown('<div class="title">💪 FitSync</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Smart Health Analytics Companion</div>', unsafe_allow_html=True)

st.markdown(
"""
<div class="description">
Track your fitness journey, analyze your health data, and stay motivated with real-time insights.
FitSync transforms your raw activity data into meaningful health intelligence.
</div>
""",
unsafe_allow_html=True
)

# -------------------- HERO IMAGE / GIF --------------------
# st.image(
#     "https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif",
#     use_column_width=True
# )

# -------------------- FEATURES SECTION --------------------
st.markdown('<div class="section-title">🔥 What FitSync Offers</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📊 Activity Tracking</h3>
        <p>Monitor your daily steps, calories burned, and workout performance with precision.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>❤️ Health Insights</h3>
        <p>Analyze heart rate, sleep quality, and overall wellness using intelligent metrics.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📈 Progress Analytics</h3>
        <p>Visualize your progress over time with interactive charts and personalized reports.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------- SECOND IMAGE --------------------
st.image(
    "https://images.unsplash.com/photo-1554284126-aa88f22d8b74",
    use_column_width=True
)

# -------------------- WHY USE SECTION --------------------
st.markdown('<div class="section-title">💡 Why Choose FitSync?</div>', unsafe_allow_html=True)

st.markdown("""
- 🎯 Personalized health insights tailored to your lifestyle  
- ⚡ Fast, clean, and intuitive interface  
- 📊 Data-driven decisions for better fitness outcomes  
- 🔄 Continuous tracking to keep you consistent  
- 🧠 Smart analytics to improve your performance  
""")

# -------------------- CALL TO ACTION --------------------
st.markdown("""
<h2 style='text-align:center; margin-top:40px; color:#FF4B4B;'>
🚀 Start your fitness journey today!
</h2>
""", unsafe_allow_html=True)

st.markdown(
"<h4 style='text-align: center;'>👉 Use the sidebar to explore your dashboard</h4>",
unsafe_allow_html=True
)