import streamlit as st
from modules.processor import process_data
import plotly.express as px
import pandas as pd

# Configure the page layout and title
st.set_page_config(layout="wide", page_title="Trends & Insights")

st.title("Trends & Insights")

# Sidebar for time range selection
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2  # Default to 'All Time'
)

# Load and process the data
df = process_data()

# Filter the DataFrame based on selected time range
filtered_df = df
if time_range == "Last 7 Days":
    filtered_df = df.sort_values(by='Date', ascending=False).head(7)
elif time_range == "Last 30 Days":
    filtered_df = df.sort_values(by='Date', ascending=False).head(30)

# Calculate summary statistics
summary_stats = filtered_df.agg({
    'Recovery_Score': ['mean', 'min', 'max'],
    'Sleep_Hours': ['mean', 'min', 'max'],
    'Steps': ['mean', 'min', 'max'],
    'Calories_Burned': ['mean', 'min', 'max']
})

st.subheader("Summary Statistics")
st.dataframe(summary_stats)

# Line Chart: Average Recovery Score month-wise
filtered_df['Month'] = pd.to_datetime(filtered_df['Date']).dt.to_period('M')
monthly_avg_recovery = filtered_df.groupby('Month')['Recovery_Score'].mean().reset_index()
monthly_avg_recovery['Month'] = monthly_avg_recovery['Month'].dt.to_timestamp()

st.subheader("Average Recovery Score Month-wise")
line_fig = px.line(monthly_avg_recovery, x='Month', y='Recovery_Score',
                   title='Average Recovery Score by Month')
st.plotly_chart(line_fig, use_container_width=True)

# Histograms
st.subheader("Histograms: Distribution of Key Metrics")
metric_columns = ['Steps', 'Calories_Burned', 'Recovery_Score', 'Sleep_Hours']

def plot_histograms(columns):
    for column in columns:
        hist_fig = px.histogram(filtered_df, x=column, title=f'Distribution of {column}')
        st.plotly_chart(hist_fig, use_container_width=True)

plot_histograms(metric_columns)
