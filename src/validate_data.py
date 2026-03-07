import pandas as pd
import os

def run_integrity_check(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: File {file_path} not found.")
        return False
    
    df = pd.read_csv(file_path)
    
    # Check 1: Record Count
    print(f"✅ Record Count: {len(df)} rows detected.")
    
    # Check 2: Null Values
    null_counts = df.isnull().sum().sum()
    if null_counts == 0:
        print("✅ Data Integrity: 0 null values found.")
    else:
        print(f"⚠️ Warning: {null_counts} null values detected.")
        
    # Check 3: Schema validation
    required_cols = ['session_duration_hr', 'weekly_frequency', 'milestones_reached']
    if all(col in df.columns for col in required_cols):
        print("✅ Schema: All required features present.")
    else:
        print("❌ Schema Error: Missing required columns.")
        return False
        
    return True

if __name__ == "__main__":
    DATA_PATH = 'data/processed/gaming_data_cleaned.csv'
    run_integrity_check(DATA_PATH)