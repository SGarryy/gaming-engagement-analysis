import pandas as pd
import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_summary(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found: {file_path}")
        
        df = pd.read_csv(file_path)
        
        if df.empty:
            raise ValueError("Input file is empty")
        
        summary = df.describe()
        
        output_dir = Path("reports")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_path = output_dir / "summary_statistics.txt"
        summary.to_csv(output_path, sep='\t')
        
        logging.info(f"Summary statistics generated at {output_path}")
        return summary
    except Exception as e:
        logging.error(f"Failed to generate summary: {str(e)}")
        raise

if __name__ == "__main__":
    generate_summary("data/processed/gaming_data_cleaned.csv")