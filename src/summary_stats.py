# src/summary_stats.py (Updated with Business Strategy logic)
import pandas as pd
import os

def generate_persona_report(data_path):
    if not os.path.exists(data_path):
        print(f"❌ Error: File {data_path} not found.")
        return

    df = pd.read_csv(data_path)
    if 'cluster' not in df.columns:
        print("❌ Error: Data not clustered.")
        return

    report = df.groupby('cluster').agg({
        'session_duration_hr': 'mean',
        'weekly_frequency': 'mean',
        'milestones_reached': 'mean'
    }).round(2)
    
    output_path = 'reports/persona_summary_stats.csv'
    report.to_csv(output_path)
    print(f"✅ Persona Summary saved to {output_path}")
    return report

def print_business_strategy(report):
    """Generates actionable advice based on persona averages."""
    print("\n--- Strategy Recommendations for Stakeholders ---")
    for cluster, row in report.iterrows():
        print(f"\nPersona {cluster}:")
        if row['milestones_reached'] > 50:
            print("  -> VIP Segment: High progression. Recommendation: Introduce early-access rewards.")
        elif row['session_duration_hr'] > 100:
            print("  -> Hardcore Segment: High uptime. Recommendation: Prioritize server stability for these nodes.")
        elif row['weekly_frequency'] < 2:
            print("  -> Churn Risk: Low frequency. Recommendation: Deploy re-engagement push notifications.")
        else:
            print("  -> Casual Segment: Stable play. Recommendation: Promote seasonal battle passes.")

if __name__ == "__main__":
    PROCESSED_DATA = 'data/processed/gaming_user_segments.csv'
    summary_report = generate_persona_report(PROCESSED_DATA)
    if summary_report is not None:
        print_business_strategy(summary_report)