import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

REQUIRED_COLUMNS = ['session_duration_hr', 'weekly_frequency', 'milestones_reached', 'avg_session_min']

def run_integrity_check(file_path):
    """Validate the integrity and schema of cleaned gaming data.
    
    Args:
        file_path: Path to the CSV file to validate
    
    Returns:
        Boolean indicating if validation passed
    """
    if not os.path.exists(file_path):
        print(f"❌ Error: File {file_path} not found.")
        logging.error(f"File not found: {file_path}")
        return False
    
    try:
        df = pd.read_csv(file_path)
        
        # Check 1: Record Count
        print(f"✅ Record Count: {len(df)} rows detected.")
        logging.info(f"Data loaded: {len(df)} rows")
        
        # Check 2: Null Values
        null_counts = df.isnull().sum().sum()
        if null_counts == 0:
            print("✅ Data Integrity: 0 null values found.")
            logging.info("No null values detected")
        else:
            print(f"⚠️ Warning: {null_counts} null values detected.")
            logging.warning(f"{null_counts} null values found in data")
            
        # Check 3: Schema validation
        missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if not missing_cols:
            print("✅ Schema: All required features present.")
            logging.info(f"All required columns present: {REQUIRED_COLUMNS}")
            return True
        else:
            print(f"❌ Schema Error: Missing required columns: {missing_cols}")
            logging.error(f"Missing columns: {missing_cols}")
            return False
            
    except Exception as e:
        print(f"❌ Error during validation: {str(e)}")
        logging.error(f"Validation error: {str(e)}")
        return False

if __name__ == "__main__":
    DATA_PATH = 'data/processed/gaming_data_cleaned.csv'
    success = run_integrity_check(DATA_PATH)
    
    if not success:
        print("\n⚠️ Data validation failed. Please run feature_engineering.py first.")
        exit(1)
    else:
        print("\n✅ Data validation complete. Ready for clustering.")