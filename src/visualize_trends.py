# src/visualize_trends.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_cluster_comparison(data_path):
    if not os.path.exists(data_path):
        print("❌ Data file missing for visualization.")
        return

    df = pd.read_csv(data_path)
    plt.figure(figsize=(10, 6))
    
    # Visualizing Progression vs Persona
    sns.barplot(data=df, x='cluster', y='milestones_reached', palette='magma')
    
    plt.title('In-Game Progression Comparison by User Persona')
    plt.xlabel('User Cluster / Persona')
    plt.ylabel('Average Milestones Reached')
    
    output_img = 'reports/cluster_progression_comparison.png'
    plt.savefig(output_img)
    print(f"✅ Visualization saved to {output_img}")

if __name__ == "__main__":
    plot_cluster_comparison('data/processed/gaming_user_segments.csv')