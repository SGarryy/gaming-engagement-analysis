# src/summary_stats.py - Business Strategy Generation & Reporting
import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_persona_report(data_path):
    """Generate summary statistics for each identified persona.
    
    Args:
        data_path: Path to the segmented gaming data CSV
    
    Returns:
        DataFrame with aggregate statistics per cluster
    """
    if not os.path.exists(data_path):
        logging.error(f"File {data_path} not found.")
        print(f"❌ Error: File {data_path} not found.")
        return None

    try:
        df = pd.read_csv(data_path)
        
        if 'cluster' not in df.columns:
            logging.error("Data is not clustered. Missing 'cluster' column.")
            print("❌ Error: Data not clustered. Run cluster_model.py first.")
            return None
        
        if df[['cluster']].empty:
            logging.error("No cluster assignments found.")
            print("❌ Error: No clusters assigned to users.")
            return None

        report = df.groupby('cluster').agg({
            'session_duration_hr': 'mean',
            'weekly_frequency': 'mean',
            'milestones_reached': 'mean'
        }).round(2)
        
        output_path = 'reports/persona_summary_stats.csv'
        os.makedirs('reports', exist_ok=True)
        report.to_csv(output_path)
        logging.info(f"Persona Summary saved to {output_path}")
        print(f"✅ Persona Summary saved to {output_path}")
        return report
    
    except Exception as e:
        logging.error(f"Error generating report: {str(e)}")
        print(f"❌ Error: {str(e)}")
        return None

def print_business_strategy(report):
    """Generates actionable strategy recommendations based on persona profiles.
    
    Args:
        report: DataFrame with cluster statistics
    """
    if report is None or report.empty:
        logging.warning("Cannot generate strategy: empty report")
        return
    
    print("\n--- Strategy Recommendations for Stakeholders ---")
    persona_names = {
        0: "Casual Segment",
        1: "Power Users",
        2: "Hardcore Grinders",
        3: "At-Risk Segment"
    }
    
    for cluster, row in report.iterrows():
        persona_name = persona_names.get(cluster, f"Cluster {cluster}")
        print(f"\n👥 {persona_name} (Cluster {cluster}):")
        print(f"   Avg Session Hours: {row['session_duration_hr']:.1f} | Weekly Frequency: {row['weekly_frequency']:.1f} | Milestones: {row['milestones_reached']:.1f}")
        
        if row['milestones_reached'] > 50:
            print("   → Strategy: VIP Segment. Introduce early-access rewards and exclusive cosmetics.")
        elif row['session_duration_hr'] > 100:
            print("   → Strategy: Hardcore Segment. Prioritize server stability and uptime for these users.")
        elif row['weekly_frequency'] < 2:
            print("   → Strategy: Churn Risk. Deploy re-engagement push notifications and comeback bonuses.")
        else:
            print("   → Strategy: Stable Casual Base. Promote seasonal battle passes and social events.")

if __name__ == "__main__":
    PROCESSED_DATA = 'data/processed/gaming_user_segments.csv'
    summary_report = generate_persona_report(PROCESSED_DATA)
    
    if summary_report is not None:
        print_business_strategy(summary_report)
        print("\n✅ Strategy generation complete.")
    else:
        logging.error("Failed to generate business strategy report.")
        exit(1)