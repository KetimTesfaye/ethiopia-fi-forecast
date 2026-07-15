import pandas as pd
import numpy as np
import os

ENRICHED_FILE = "data/processed/ethiopia_fi_unified_data_enriched.csv"

def run_eda_pipeline():
    if not os.path.exists(ENRICHED_FILE):
        print(f"✘ Error: Enriched data not found at {ENRICHED_FILE}. Run Task 1 script first.")
        return

    df = pd.read_csv(ENRICHED_FILE)
    print(f"✔ Successfully loaded enriched data. Total records: {len(df)}\n")

    # 1. Dataset Overview Breakdown
    print("=== 1. Record Type Breakdown ===")
    print(df['record_type'].value_counts(dropna=False))
    
    print("\n=== 2. Pillar Distribution ===")
    print(df['pillar'].value_counts(dropna=False))

    print("\n=== 3. Confidence Level Distribution (Data Quality) ===")
    print(df['confidence'].value_counts(dropna=False))

    # 2. Observations Temporal Analysis
    obs = df[df['record_type'] == 'observation'].copy()
    obs['observation_date'] = pd.to_datetime(obs['observation_date'], errors='coerce')
    
    print(f"\n=== 4. Observations Summary ===")
    print(f"Total Observation Metrics: {len(obs)}")
    print(f"Unique Indicator Codes: {obs['indicator_code'].nunique()}")
    
    # 3. Events Cataloged
    events = df[df['record_type'] == 'event']
    print(f"\n=== 5. Cataloged Events ({len(events)}) ===")
    for idx, row in events.iterrows():
        print(f" - [{row['id']}] {row['observation_date']}: {row['source_name']} (Category: {row['category']})")

if __name__ == "__main__":
    run_eda_pipeline()