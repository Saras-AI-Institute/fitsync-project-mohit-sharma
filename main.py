import streamlit as st
from modules.processor import process_data

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
df = process_data()

# Filter the DataFrame based on selected time range
if time_range == "Last 7 Days":
    df = df.sort_values(by='Date', ascending=False).head(7)
elif time_range == "Last 30 Days":
    df = df.sort_values(by='Date', ascending=False).head(30)
# 'All Time' uses the full DataFrame without filtering

# Displaying the DataFrame
# st.dataframe(df)
st.write("Explore your health metrics in depth with FitSync")

# Calculate metrics from the filtered DataFrame
average_steps = df['Steps'].mean()
average_sleep_hours = df['Sleep_Hours'].mean()
average_recovery_score = df['Recovery_Score'].mean()

# Set up a 3-column layout for displaying metrics
col1, col2, col3 = st.columns(3)
# Display filtered metrics in respective columns
with col1:
    st.metric(label="Average Steps", value=f"{average_steps:.0f}", delta=None)

with col2:
    st.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}", delta=None)

with col3:
    st.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}", delta=None)

# The DataFrame display can be updated here if needed
# Example: st.dataframe(df)

# Additional sections could be added here for more analytics and visualizations

