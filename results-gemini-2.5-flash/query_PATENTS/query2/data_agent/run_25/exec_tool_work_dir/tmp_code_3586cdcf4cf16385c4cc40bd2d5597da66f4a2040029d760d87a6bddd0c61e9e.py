code = """import json
import pandas as pd

# Load the full data from the file
with open(locals()['var_function-call-16368827637550378910'], 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Filter for German patents (Patents_info contains 'DE')
germany_df = df[df['Patents_info'].str.contains('DE', na=False)]

# Extract filing year
def extract_year(date_str):
    if isinstance(date_str, str):
        parts = date_str.replace("the ", "").replace("on ", "").split()
        for part in parts:
            if part.isdigit() and len(part) == 4:
                return int(part)
    return None

germany_df['filing_year'] = germany_df['filing_date'].apply(extract_year)
germany_df = germany_df.dropna(subset=['filing_year'])

# Extract all CPC codes directly from the 'cpc' field
def extract_all_cpc_codes(cpc_json_str):
    if pd.isna(cpc_json_str):
        return []
    cpc_list = json.loads(cpc_json_str)
    codes = [cpc_item.get('code') for cpc_item in cpc_list if cpc_item.get('code')]
    return list(set(codes))

germany_df['cpc_codes'] = germany_df['cpc'].apply(extract_all_cpc_codes)
germany_df = germany_df.explode('cpc_codes')
germany_df = germany_df.dropna(subset=['cpc_codes'])

# Count patent filings per CPC group per year
filings_count = germany_df.groupby(['cpc_codes', 'filing_year']).size().reset_index(name='count')

# Calculate EMA
smoothing_factor = 0.1
filings_count = filings_count.sort_values(by=['cpc_codes', 'filing_year'])

def calculate_ema(group):
    group['ema'] = group['count'].ewm(alpha=smoothing_factor, adjust=False).mean()
    return group

ema_df = filings_count.groupby('cpc_codes').apply(calculate_ema)

# Find the best year for each CPC group
best_years = ema_df.loc[ema_df.groupby('cpc_codes')['ema'].idxmax()]

# Get unique CPC codes for fetching full titles
unique_cpc_codes = best_years['cpc_codes'].unique().tolist()

result = {
    'best_years_ema': best_years.to_dict(orient='records'),
    'unique_cpc_codes': unique_cpc_codes
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16368827637550378910': 'file_storage/function-call-16368827637550378910.json'}

exec(code, env_args)
