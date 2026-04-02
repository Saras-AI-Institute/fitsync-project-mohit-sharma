import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Constants
days = 365
start_date = datetime(2025, 1, 1)
date_list = [start_date + timedelta(days=i) for i in range(days)]  # Generate dates
data = {
    "Date": date_list,
    "Steps": np.random.normal(8500, 3000, days).clip(3000, 18000),  # Normal distribution around 8500
    "Sleep_Hours": np.random.normal(7.2, 0.7, days).clip(4.5, 9.5),  # Normal distribution around 7.2
    "Heart_Rate_bpm": np.random.normal(68, 10, days).clip(48, 110),  # Normal distribution around 68
    "Active_Minutes": np.random.randint(20, 180, days)  # Random integers between 20 and 180
}

# Calories Burned derived from Steps and Active Minutes (simple model)
data["Calories_Burned"] = data["Steps"] * 0.04 + data["Active_Minutes"] * 3.5

# Create DataFrame
df = pd.DataFrame(data)

# Introduce 5% missing values randomly in each column
for column in df.columns[1:]:  # Skip 'Date' column
    df.loc[df.sample(frac=0.05).index, column] = np.nan

# Save to CSV
df.to_csv('data/health_data.csv', index=False)