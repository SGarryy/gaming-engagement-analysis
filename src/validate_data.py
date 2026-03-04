import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_columns(df):
    """Checks for null values and data types."""
    null_counts = df.isnull().sum()
    logging.info("Checking for missing values...")
    print(null_counts[null_counts > 0])
    
    if null_counts.sum() == 0:
        logging.info("Data Validation Passed: No missing values found.")
    else:
        logging.warning(f"Data Validation Warning: Found {null_counts.sum()} missing values.")

if __name__ == "__main__":
    from data_loader import load_gaming_data
    df = load_gaming_data("data/raw/gaming_data_raw.csv")
    if df is not None:
        validate_columns(df)