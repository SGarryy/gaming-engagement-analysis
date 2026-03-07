# src/summary_stats.py
import pandas as pd
import os

def generate_persona_report(data_path):
    if not os.path.exists(data_path):
        print(f"❌ Error: File {data_path} not found.")
        return

    df = pd.read_csv(data_path)
    
    if 'cluster' not in df.columns:
        print("❌ Error: Data not yet clustered. Run cluster_model.py first.")
        return

    # Calculate mean metrics for each persona
    report = df.groupby('cluster').agg({
        'session_duration_hr': 'mean',
        'weekly_frequency': 'mean',
        'milestones_reached': 'mean'
    }).round(2)
    
    print("\n--- User Persona Summary Report ---")
    print(report)
    
    # Export for stakeholders
    output_path = 'reports/persona_summary_stats.csv'
    report.to_csv(output_path)
    print(f"\n✅ Report exported to {output_path}")

if __name__ == "__main__":
    PROCESSED_DATA = 'data/processed/gaming_user_segments.csv'
    generate_persona_report(PROCESSED_DATA)