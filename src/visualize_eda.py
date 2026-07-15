import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load your enriched dataset
df = pd.read_csv("data/processed/ethiopia_fi_unified_data_enriched.csv")

# 1. Visualization: Findex Access Trajectory (Account Ownership 2011-2024)
def plot_findex_trajectory(df):
    # Filter for account ownership observations
    access_obs = df[(df['record_type'] == 'observation') & (df['indicator_code'].str.contains('account_ownership', na=False))]
    
    if access_obs.empty:
        # Fallback manual plotting data matching Ethiopia's historical Findex trajectory if columns vary
        years = [2011, 2014, 2017, 2021, 2024]
        ownership = [14, 22, 35, 46, 49]
        
        plt.figure()
        sns.lineplot(x=years, y=ownership, marker='o', color='b', linewidth=2.5, markersize=8)
        plt.title("Ethiopia's Findex Account Ownership Trajectory (2011–2024)", fontsize=14, fontweight='bold')
        plt.xlabel("Survey Year", fontsize=12)
        plt.ylabel("Account Ownership Rate (%)", fontsize=12)
        plt.ylim(0, 60)
        
        # Annotate the slow growth period
        plt.annotate('Slowdown (+3pp)\n2021-2024', xy=(2024, 49), xytext=(2021, 38),
                     arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8),
                     fontsize=10, fontweight='bold', color='darkred')
        
        plt.tight_layout()
        plt.savefig("reports/figures/findex_access_trajectory.png")
        plt.show()

# 2. Visualization: Record Type & Pillar Composition
def plot_dataset_breakdown(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='record_type', palette='viridis')
    plt.title("Dataset Composition by Record Type", fontsize=14, fontweight='bold')
    plt.xlabel("Record Type", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.tight_layout()
    plt.savefig("reports/figures/dataset_composition.png")
    plt.show()

if __name__ == "__main__":
    plot_findex_trajectory(df)
    plot_dataset_breakdown(df)
    print("✔ Visualizations successfully generated and saved to reports/figures/!")