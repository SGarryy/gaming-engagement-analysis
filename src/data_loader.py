import pandas as pd
import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_gaming_data(file_path):
    """Load raw gaming data from CSV file with error handling.
    
    Args:
        file_path: Path to the raw CSV data file
    
    Returns:
        Pandas DataFrame with gaming data
    
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is empty
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file not found: {file_path}")
        
        df = pd.read_csv(file_path)
        
        if df.empty:
            raise ValueError("Data file is empty")
        
        logging.info(f"Successfully loaded data. Shape: {df.shape}")
        return df
    except Exception as e:
        logging.error(f"Failed to load data: {str(e)}")
        raise

if __name__ == "__main__":
    RAW_DATA_PATH = Path(__file__).parent.parent / "data" / "raw" / "gaming_data_raw.csv"
    
    try:
        data = load_gaming_data(str(RAW_DATA_PATH))
        print(f"✅ Data loaded successfully. Shape: {data.shape}")
        print(data.head())
    except Exception as e:
        print(f"❌ Failed to load data: {e}")
        exit(1)