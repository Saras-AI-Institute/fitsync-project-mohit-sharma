import pandas as pd
from datetime import datetime


def load_data():
    """
    This function loads and cleans the data from 'health_data.csv'.
    Missing values are handled intelligently based on the column context.
    """
    # Load the CSV file
    df = pd.read_csv('data/health_data.csv')
    
    # Fill missing 'Steps' with the median value of the column
    df['Steps'] = df['Steps'].fillna(df['Steps'].median())

    # Fill missing 'Sleep_Hours' with a fixed value of 7.0
    df['Sleep_Hours'] = df['Sleep_Hours'].fillna(7.0)

    # Fill missing 'Heart_Rate_bpm' with a fixed value of 68
    df['Heart_Rate_bpm'] = df['Heart_Rate_bpm'].fillna(68)

    # Fill missing values in all other columns with their median values
    for column in df.columns:
        if df[column].isnull().any():
            df[column].fillna(df[column].median(), inplace=True)

    # Convert 'Date' column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    return df


def calculate_recovery_score(df):
    """
    This function calculates a 'Recovery_Score' for each entry in the DataFrame,
    based on sleep, resting heart rate, and steps.
    The score ranges from 0 to 100, where a higher score indicates better recovery.
    """
    # Initialize the Recovery_Score column with a base score
    df['Recovery_Score'] = 50  # Start with a neutral score of 50

    # Adjusting the score based on Sleep_Hours
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20  # Good sleep enhances recovery
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_Score'] -= 20  # Poor sleep reduces recovery

    # Adjusting the score based on Heart_Rate_bpm
    df['Recovery_Score'] -= (df['Heart_Rate_bpm'] - 60) * 0.5  # Lower heart rate is better

    # Adjusting the score based on Steps
    df['Recovery_Score'] -= (df['Steps'] - 10000) / 1000  # Very high steps may reduce recovery

    # Ensuring the Recovery_Score is capped between 0 and 100
    df['Recovery_Score'] = df['Recovery_Score'].clip(0, 100)

    return df

