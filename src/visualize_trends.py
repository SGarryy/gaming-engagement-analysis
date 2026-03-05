import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def plot_distributions(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found: {file_path}")
        
        df = pd.read_csv(file_path)
        
        if df.empty:
            raise ValueError("Input file is empty")
        
        if 'session_duration_hr' not in df.columns:
            raise KeyError("Column 'session_duration_hr' not found in data")
        
        output_dir = Path("reports")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        plt.figure(figsize=(10, 6))
        sns.histplot(df['session_duration_hr'], bins=30, kde=True)
        plt.title('Distribution of User Session Durations')
        
        output_path = output_dir / "duration_distribution.png"
        plt.savefig(output_path)
        plt.close()
        
        logging.info(f"Plot saved to {output_path}")
    except Exception as e:
        logging.error(f"Failed to create plot: {str(e)}")
        raise

if __name__ == "__main__":
    plot_distributions("data/processed/gaming_data_cleaned.csv")