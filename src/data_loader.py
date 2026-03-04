import pandas as pd
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_gaming_data(file_path):
    """Loads gaming data and performs initial shape validation."""
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return None
    
    df = pd.read_csv(file_path)
    logging.info(f"Successfully loaded data. Shape: {df.shape}")
    return df

if __name__ == "__main__":
    RAW_DATA_PATH = "data/raw/gaming_data_raw.csv"
    data = load_gaming_data(RAW_DATA_PATH)
    if data is not None:
        print(data.head())