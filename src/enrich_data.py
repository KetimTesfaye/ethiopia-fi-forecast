import pandas as pd
import os

PROCESSED_DIR = "data/processed"
RAW_FILE = "data/raw/ethiopia_fi_unified_data.csv"
ENRICHED_FILE = os.path.join(PROCESSED_DIR, "ethiopia_fi_unified_data_enriched.csv")

def append_enriched_data():
    if not os.path.exists(RAW_FILE):
        print(f"Raw file not found at {RAW_FILE}. Creating a mock file to test the flow...")
        # Create empty mock framework if CSV hasn't been pulled yet
        cols = ['id', 'record_type', 'parent_id', 'pillar', 'category', 'indicator_code', 
                'value_numeric', 'observation_date', 'source_name', 'source_url', 
                'confidence', 'collected_by', 'collection_date', 'notes']
        df = pd.DataFrame(columns=cols)
    else:
        df = pd.read_csv(RAW_FILE)

    new_records = [
        # 1. Observation: Telebirr User growth (Jan 2026)
        {
            'id': 'OBS_031',
            'record_type': 'observation',
            'parent_id': None,
            'pillar': 'Access',
            'category': None,
            'indicator_code': 'active_mobile_money_users_telebirr',
            'value_numeric': 58610000.0,
            'observation_date': '2026-01-29',
            'source_name': 'Ethio Telecom H1 Business Report',
            'source_url': 'https://www.ethiotelecom.et/ethio-telecom-2025-26-fiscal-year-first-half-year-business-performance-report/',
            'confidence': 'high',
            'collected_by': 'HP',
            'collection_date': '2026-07-15',
            'notes': 'Verified H1 2025/26 data point. Telebirr represents the massive core of Ethiopia\'s mobile money expansion.'
        },
        # 2. Observation: M-Pesa Ethiopia growth (March 2026)
        {
            'id': 'OBS_032',
            'record_type': 'observation',
            'parent_id': None,
            'pillar': 'Access',
            'category': None,
            'indicator_code': 'active_mobile_money_users_mpesa',
            'value_numeric': 5200000.0,
            'observation_date': '2026-03-31',
            'source_name': 'Safaricom Group FY26 Results',
            'source_url': 'https://www.safaricom.et/whats-new/latest/news-and-blogs/safaricom-ethiopia-records-1309-service-revenue-growth-in-fy26',
            'confidence': 'high',
            'collected_by': 'HP',
            'collection_date': '2026-07-15',
            'notes': 'Reflects Safaricom Ethiopia FY26 results showing M-Pesa customer numbers more than doubling.'
        },
        # 3. Event: Fayda National ID Milestone
        {
            'id': 'EVT_011',
            'record_type': 'event',
            'parent_id': None,
            'pillar': None,  # Kept empty intentionally to keep the data unbiased
            'category': 'infrastructure',
            'indicator_code': None,
            'value_numeric': 30000000.0,  # 30M registered IDs
            'observation_date': '2025-12-31',
            'source_name': 'Uchumi360 Review / National ID Program',
            'source_url': 'https://uchumi360.com/r/e/telebirr-million-users-pesa',
            'confidence': 'high',
            'collected_by': 'HP',
            'collection_date': '2026-07-15',
            'notes': 'Over 30M registrations out of 90M target achieved. Drastically simplifies onboarding and KYC.'
        },
        # 4. Impact Link: Connecting Fayda ID (EVT_011) to Access (Account Ownership Rate)
        {
            'id': 'IMP_015',
            'record_type': 'impact_link',
            'parent_id': 'EVT_011',
            'pillar': 'Access',
            'category': None,
            'indicator_code': 'account_ownership_rate',
            'value_numeric': 0.05,  # Estimated 5 percentage point positive impact over long run
            'observation_date': None,
            'source_name': 'Global Findex India/Aadhaar Analogy Case Studies',
            'source_url': 'https://id.gov.et/strategies',
            'confidence': 'medium',
            'collected_by': 'HP',
            'collection_date': '2026-07-15',
            'notes': 'Bridges the Fayda ID system rollout to lower entry-barriers in formal finance. Modeled lag: 3-6 months.'
        }
    ]

    new_df = pd.DataFrame(new_records)
    
    # Merge datasets, drop duplicates if already exists
    combined_df = pd.concat([df, new_df], ignore_index=True).drop_duplicates(subset=['id'], keep='last')
    
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    combined_df.to_csv(ENRICHED_FILE, index=False)
    print(f"✔ Successfully saved enriched dataset ({len(combined_df)} total records) to: {ENRICHED_FILE}")

if __name__ == "__main__":
    append_enriched_data()