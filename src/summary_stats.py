import pandas as pd

def generate_summary(file_path):
    df = pd.read_csv(file_path)
    summary = df.describe()
    summary.to_csv("reports/summary_statistics.txt", sep='\t')
    print("Summary statistics generated in reports folder.")

if __name__ == "__main__":
    import os
    if not os.path.exists("reports"): os.makedirs("reports")
    generate_summary("data/processed/gaming_data_cleaned.csv")