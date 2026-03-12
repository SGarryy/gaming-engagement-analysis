# src/feature_scaling.py - Feature Normalization for Clustering
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scale_features(input_path, output_path=None):
    """Apply z-score normalization (StandardScaler) to gaming features.
    
    This ensures distance-based clustering algorithms like K-Means work correctly
    by standardizing the scale of different features.
    
    Args:
        input_path: Path to cleaned CSV data
        output_path: Path to save scaled numpy array (optional)
    
    Returns:
        Scaled feature array (numpy ndarray)
    """
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        # Load cleaned data
        df = pd.read_csv(input_path)
        logging.info(f"Loaded data: {df.shape}")
        
        # Select only numeric features for clustering
        feature_columns = ['session_duration_hr', 'weekly_frequency', 'milestones_reached']
        
        missing_cols = [col for col in feature_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        X = df[feature_columns].values
        
        # Apply StandardScaler for z-score normalization
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        logging.info(f"Feature scaling complete. Shape: {X_scaled.shape}")
        
        # Save scaled data if output path is provided
        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            np.save(output_path, X_scaled)
            logging.info(f"Scaled features saved to {output_path}")
            print(f"✅ Scaled data saved to {output_path}")
        
        return X_scaled
    
    except Exception as e:
        logging.error(f"Error during feature scaling: {str(e)}")
        print(f"❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    INPUT_PATH = 'data/processed/gaming_data_cleaned.csv'
    OUTPUT_PATH = 'data/processed/scaled_gaming_data.npy'
    
    try:
        scaled_data = scale_features(INPUT_PATH, OUTPUT_PATH)
        print(f"✅ Feature scaling complete. Scaled data shape: {scaled_data.shape}")
        print(f"   Features normalized using z-score (StandardScaler)")
    except Exception as e:
        logging.error("Feature scaling failed.")
        exit(1)
