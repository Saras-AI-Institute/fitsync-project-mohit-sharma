# st.set_page_config should be the first Streamlit command.

import streamlit as st
from modules.processor import process_data
import plotly.express as px

# Configure the page layout and title
st.set_page_config(layout="wide", page_title="FitSync")

# Set the title of the dashboard
st.title("FitSync - Personal Health Analytics")

# Sidebar for time range selection
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2  # Default to 'All Time'
)

# Load and process the data
@st.cache_data
def process_data_cached():
    return process_data()

# Use the cached data processing function
df = process_data_cached()

# Filter the DataFrame based on selected time range
filtered_df = df
if time_range == "Last 7 Days":
    filtered_df = df.sort_values(by='Date', ascending=False).head(7)
elif time_range == "Last 30 Days":
    filtered_df = df.sort_values(by='Date', ascending=False).head(30)

# Calculate metrics from the filtered DataFrame
average_steps = filtered_df['Steps'].mean()
average_sleep_hours = filtered_df['Sleep_Hours'].mean()
average_recovery_score = filtered_df['Recovery_Score'].mean()

# Set up a 3-column layout for displaying metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Average Steps", value=f"{average_steps:.0f}", delta=None)

with col2:
    st.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}", delta=None)

with col3:
    st.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}", delta=None)

# Create two columns for charts
chart_col1, chart_col2 = st.columns(2)

# Left Column: Dual Line Chart
with chart_col1:
    st.subheader("Recovery Score & Sleep Trend")
    fig1 = px.line(filtered_df, x='Date', y=['Recovery_Score', 'Sleep_Hours'],
                   labels={'value': 'Scores'}, title="")
    st.plotly_chart(fig1, use_container_width=True)

# Right Column: Scatter Plot
with chart_col2:
    st.subheader("Recovery Score vs Daily Steps")
    fig2 = px.scatter(filtered_df, x='Steps', y='Recovery_Score', color='Sleep_Hours',
                      labels={'color': 'Sleep Hours'}, title="")
    st.plotly_chart(fig2, use_container_width=True)

# Below the first set of charts, create another two-column layout
chart_col3, chart_col4 = st.columns(2)

# Left Column: Scatter Plot - Recovery Score vs Heart Rate
with chart_col3:
    st.subheader("Recovery Score vs Resting Heart Rate")
    fig3 = px.scatter(filtered_df, x='Heart_Rate_bpm', y='Recovery_Score',
                      labels={'x': 'Heart Rate', 'y': 'Recovery Score'},
                      title="")
    st.plotly_chart(fig3, use_container_width=True)

# Right Column: Line Chart - Calories Burned Trend
with chart_col4:
    st.subheader("Daily Calories Burned Trend")
    fig4 = px.line(filtered_df, x='Date', y='Calories_Burned',
                   labels={'y': 'Calories Burned'}, title="")
    st.plotly_chart(fig4, use_container_width=True)

# The DataFrame display can be updated here if needed
# Example: st.dataframe(df)

st.write("Explore your health metrics in depth with FitSync")

