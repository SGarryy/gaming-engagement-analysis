# src/visualize_trends.py - Cluster Visualization & Analysis
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def plot_cluster_comparison(data_path):
    """Generate visualization comparing progression metrics across user clusters.
    
    Args:
        data_path: Path to segmented gaming data CSV
    """
    if not os.path.exists(data_path):
        logging.error(f"Data file missing: {data_path}")
        print("❌ Data file missing for visualization.")
        return False

    try:
        df = pd.read_csv(data_path)
        
        if 'cluster' not in df.columns:
            logging.error("Missing 'cluster' column in data.")
            print("❌ Error: Data does not contain cluster assignments.")
            return False
        
        # Create output directory
        os.makedirs('reports', exist_ok=True)
        
        plt.figure(figsize=(10, 6))
        
        # Visualizing Progression vs Persona
        sns.barplot(data=df, x='cluster', y='milestones_reached', palette='magma')
        
        plt.title('In-Game Progression Comparison by User Persona', fontsize=14, fontweight='bold')
        plt.xlabel('User Cluster / Persona')
        plt.ylabel('Average Milestones Reached')
        plt.tight_layout()
        
        output_img = 'reports/cluster_progression_comparison.png'
        plt.savefig(output_img, dpi=300)
        logging.info(f"Visualization saved to {output_img}")
        print(f"✅ Visualization saved to {output_img}")
        plt.close()
        
        return True
        
    except Exception as e:
        logging.error(f"Error during visualization: {str(e)}")
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    DATA_PATH = 'data/processed/gaming_user_segments.csv'
    success = plot_cluster_comparison(DATA_PATH)
    
    if not success:
        logging.error("Visualization generation failed.")
        exit(1)