import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def rename_columns(df):
    """Standardizes column names for internal reporting."""
    mapping = {
        'PlayTimeHours': 'session_duration_hr',
        'SessionsPerWeek': 'weekly_frequency',
        'AvgSessionDurationMinutes': 'avg_session_min',
        'AchievementsUnlocked': 'milestones_reached'
    }
    df = df.rename(columns=mapping)
    logging.info("Column renaming completed.")
    return df

if __name__ == "__main__":
    from data_loader import load_gaming_data
    df = load_gaming_data("data/raw/gaming_data_raw.csv")
    if df is not None:
        df_cleaned = rename_columns(df)
        print(df_cleaned.columns)