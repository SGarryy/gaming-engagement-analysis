import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import joblib

def apply_clustering(scaled_data_path, n_clusters=4):
    # Load the scaled data we saved yesterday
    X_scaled = np.load(scaled_data_path)
    
    # Initialize and fit K-Means
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    cluster_labels = kmeans.fit_predict(X_scaled)
    
    return kmeans, cluster_labels

if __name__ == "__main__":
    SCALED_PATH = 'data/processed/scaled_gaming_data.npy'
    model, labels = apply_clustering(SCALED_PATH)
    print(f"Clustering complete. Identified {len(np.unique(labels))} user segments.")

# Save the model for future use
    import os
    if not os.path.exists('models'): os.makedirs('models')
    joblib.dump(model, 'models/gaming_kmeans_v1.pkl')
    print("Model saved to models/gaming_kmeans_v1.pkl")