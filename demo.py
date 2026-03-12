import os
import subprocess
import time
import sys

def run_demo():
    """Execute the complete gaming engagement analysis pipeline."""
    print("🚀 Initializing Gaming Intelligence Demo...")
    time.sleep(1)
    
    steps = [
        ("Step 0: Environment Check", "python src/check_env.py"),
        ("Step 1: Feature Engineering & Cleaning", "python src/feature_engineering.py"),
        ("Step 2: Feature Scaling & Normalization", "python src/feature_scaling.py"),
        ("Step 3: Data Validation", "python src/validate_data.py"),
        ("Step 4: ML Clustering & Modeling", "python src/cluster_model.py"),
        ("Step 5: Business Strategy Generation", "python src/summary_stats.py"),
        ("Step 6: Visualization & Reporting", "python src/visualize_trends.py")
    ]
    
    for description, command in steps:
        print(f"\n--- {description} ---")
        result = subprocess.run(command, shell=True)
        
        if result.returncode != 0:
            print(f"❌ {description} failed with exit code {result.returncode}")
            print("Pipeline halted. Please check the error messages above.")
            sys.exit(1)
        
        time.sleep(0.5)

    print("\n" + "="*60)
    print("✅ DEMO COMPLETE - All Analysis Steps Successful!")
    print("="*60)
    print("\nGenerated Reports & Outputs:")
    print("  📊 /reports/persona_summary_stats.csv - Cluster statistics")
    print("  📈 /reports/cluster_progression_comparison.png - Visualization")
    print("  💾 /data/processed/gaming_user_segments.csv - Final segmented data")
    print("  🤖 /models/gaming_kmeans_v1.pkl - Trained K-Means model")
    print("\nYou can now review the cluster analysis in /reports/")

if __name__ == "__main__":
    run_demo()