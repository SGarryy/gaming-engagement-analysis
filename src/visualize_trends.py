import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(file_path):
    df = pd.read_csv(file_path)
    plt.figure(figsize=(10, 6))
    sns.histplot(df['session_duration_hr'], bins=30, kde=True)
    plt.title('Distribution of User Session Durations')
    plt.savefig('reports/duration_distribution.png')
    print("Plot saved to reports/duration_distribution.png")

if __name__ == "__main__":
    plot_distributions("data/processed/gaming_data_cleaned.csv")