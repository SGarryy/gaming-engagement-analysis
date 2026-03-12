import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import joblib
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def apply_clustering(scaled_data_path, n_clusters=4):
    """Apply K-Means clustering to scaled gaming data.
    
    Args:
        scaled_data_path: Path to the numpy array with scaled features
        n_clusters: Number of clusters (default 4)
    
    Returns:
        Tuple of (fitted KMeans model, cluster labels)
    """
    if not os.path.exists(scaled_data_path):
        raise FileNotFoundError(f"Scaled data not found at {scaled_data_path}")
    
    X_scaled = np.load(scaled_data_path)
    logging.info(f"Loaded scaled data with shape {X_scaled.shape}")
    
    # Initialize and fit K-Means
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    cluster_labels = kmeans.fit_predict(X_scaled)
    logging.info(f"K-Means fitting complete. Inertia: {kmeans.inertia_:.2f}")
    
    return kmeans, cluster_labels

if __name__ == "__main__":
    SCALED_PATH = 'data/processed/scaled_gaming_data.npy'
    
    try:
        model, labels = apply_clustering(SCALED_PATH)
        print(f"Clustering complete. Identified {len(np.unique(labels))} user segments.")
        
        # Save the model for future use
        if not os.path.exists('models'):
            os.makedirs('models')
        
        joblib.dump(model, 'models/gaming_kmeans_v1.pkl')
        logging.info("Model saved to models/gaming_kmeans_v1.pkl")
    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
        print(f"❌ {e}")
        exit(1)