import pandas as pd
import logging
import os
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

COLUMN_MAPPING = {
    'PlayTimeHours': 'session_duration_hr',
    'SessionsPerWeek': 'weekly_frequency',
    'AvgSessionDurationMinutes': 'avg_session_min',
    'AchievementsUnlocked': 'milestones_reached'
}

def rename_columns(df):
    """Standardize column names in raw gaming data.
    
    Args:
        df: DataFrame with raw column names
    
    Returns:
        DataFrame with standardized column names
    """
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

def load_and_process_data(input_path):
    """Load and process raw gaming data.
    
    Args:
        input_path: Path to raw CSV file
    
    Returns:
        Processed DataFrame
    """
    try:
        # Import here to avoid circular imports
        sys.path.insert(0, os.path.dirname(__file__))
        from data_loader import load_gaming_data
        
        df = load_gaming_data(input_path)
        df_cleaned = rename_columns(df)
        
        return df_cleaned
    except ImportError:
        logging.error("Could not import data_loader. Ensure you're running from project root.")
        raise

if __name__ == "__main__":
    RAW_DATA_PATH = Path(__file__).parent.parent / "data" / "raw" / "gaming_data_raw.csv"
    
    try:
        df_processed = load_and_process_data(str(RAW_DATA_PATH))
        
        output_dir = Path(__file__).parent.parent / "data" / "processed"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_path = output_dir / "gaming_data_cleaned.csv"
        df_processed.to_csv(output_path, index=False)
        logging.info(f"Cleaned data saved to {output_path}")
        print(f"✅ Data cleaning complete: {output_path}")
    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
        print(f"❌ {e}")
        exit(1)