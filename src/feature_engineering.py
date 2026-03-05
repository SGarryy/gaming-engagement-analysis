import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

COLUMN_MAPPING = {
    'PlayTimeHours': 'session_duration_hr',
    'SessionsPerWeek': 'weekly_frequency',
    'AvgSessionDurationMinutes': 'avg_session_min',
    'AchievementsUnlocked': 'milestones_reached'
}

def rename_columns(df):
    try:
        missing_cols = [col for col in COLUMN_MAPPING.keys() if col not in df.columns]
        if missing_cols:
            logging.warning(f"Expected columns not found: {missing_cols}")
        
        df = df.rename(columns=COLUMN_MAPPING)
        logging.info("Column renaming completed.")
        return df
    except Exception as e:
        logging.error(f"Failed to rename columns: {str(e)}")
        raise

if __name__ == "__main__":
    from data_loader import load_gaming_data
    
    df = load_gaming_data("data/raw/gaming_data_raw.csv")
    df_cleaned = rename_columns(df)
    
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / "gaming_data_cleaned.csv"
    df_cleaned.to_csv(output_path, index=False)
    logging.info(f"Cleaned data saved to {output_path}")