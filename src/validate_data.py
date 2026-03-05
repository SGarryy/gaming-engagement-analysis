import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_columns(df):
    try:
        null_counts = df.isnull().sum()
        logging.info("Validating data integrity...")
        
        null_values = null_counts[null_counts > 0]
        if len(null_values) > 0:
            logging.warning(f"Missing values found:\n{null_values}")
            return False
        
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) == 0:
            logging.warning("No numeric columns detected in data")
            return False
        
        logging.info(f"Data Validation: All {len(df)} records intact, no missing values")
        return True
    except Exception as e:
        logging.error(f"Validation failed: {str(e)}")
        return False

if __name__ == "__main__":
    from data_loader import load_gaming_data
    df = load_gaming_data("data/raw/gaming_data_raw.csv")
    validate_columns(df)