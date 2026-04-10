# sample_data.py

import pandas as pd
from datetime import datetime

def load_data(file_path='data/health_data.csv'):
    """
    Load and clean the health data from CSV file.
    Handles missing values and converts date strings into datetime objects.
    Returns a cleaned pandas DataFrame.
    """

    # Load dataset
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

    # Fill missing values safely (avoid inplace warnings)
    data['Steps'] = data['Steps'].fillna(data['Steps'].median())
    data['Sleep_Hours'] = data['Sleep_Hours'].fillna(7)
    data['Heart_Rate_bpm'] = data['Heart_Rate_bpm'].fillna(68)

    # Handle other numeric columns dynamically
    for column in ['Calories_Burned', 'Active_Minutes']:
        if column in data.columns:
            data[column] = data[column].fillna(data[column].median())

    # Convert Date column (more robust)
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

    return data


def calculate_recovery_score(df):
    """
    Adds a 'Recovery_Score' (0–100) based on sleep, heart rate, and activity.
    """

    if df is None:
        return None

    # Start with base score
    df['Recovery_Score'] = 50

    # Sleep impact
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_Score'] -= 20

    # Heart rate impact
    df.loc[df['Heart_Rate_bpm'] < 60, 'Recovery_Score'] += 10
    df.loc[df['Heart_Rate_bpm'] > 80, 'Recovery_Score'] -= 10

    # Steps impact
    df.loc[(df['Steps'].between(8000, 12000)), 'Recovery_Score'] += 10
    df.loc[df['Steps'] < 4000, 'Recovery_Score'] -= 5
    df.loc[df['Steps'] > 16000, 'Recovery_Score'] -= 5

    # Clamp values between 0 and 100
    df['Recovery_Score'] = df['Recovery_Score'].clip(0, 100)

    return df


def main():
    df = load_data()
    df = calculate_recovery_score(df)

    if df is not None:
        print("First 5 rows:")
        print(df.head())

        print("\nMissing values:")
        print(df.isnull().sum())


if __name__ == "__main__":
    main()