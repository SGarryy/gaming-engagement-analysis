import os
import subprocess
import time

def run_demo():
    print("🚀 Initializing Gaming Intelligence Demo...")
    time.sleep(1)
    
    steps = [
        ("Step 1: Data Validation", "python src/validate_data.py"),
        ("Step 2: ML Clustering & Modeling", "python src/cluster_model.py"),
        ("Step 3: Business Strategy Generation", "python src/summary_stats.py")
    ]
    
    for description, command in steps:
        print(f"\n--- {description} ---")
        subprocess.run(command, shell=True)
        time.sleep(1)

    print("\n✅ Demo Complete. All reports generated in /reports/")

if __name__ == "__main__":
    run_demo()