import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_gaming_data(file_path):
    logging.info(f"Attempting to load data from {file_path}")
    """
    Template function to load synthetic gaming data.
    """
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print("Data file not found.")
        return None

if __name__ == "__main__":
    print("Data Loader Script Initialized.")