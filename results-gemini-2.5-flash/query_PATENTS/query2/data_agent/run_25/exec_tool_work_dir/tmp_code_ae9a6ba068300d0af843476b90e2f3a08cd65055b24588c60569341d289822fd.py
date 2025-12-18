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
        import re
        match = re.search(r'\d{4}', date_str)
        if match:
            return int(match.group(0))
    return None

germany_df['filing_year'] = germany_df['filing_date'].apply(extract_year)
germany_df = germany_df.dropna(subset=['filing_year'])

# Extract level 4 CPC group codes (first 4 characters)
def extract_cpc_level4_groups(cpc_json_str):
    if pd.isna(cpc_json_str):
        return []
    cpc_list = json.loads(cpc_json_str)
    level4_groups = []
    for cpc_item in cpc_list:
        code = cpc_item.get('code')
        if code and len(code) >= 4:
            # Take the first 4 characters as the level 4 group
            level4_groups.append(code[:4])
    return list(set(level4_groups)) # Get unique level 4 groups for a patent

germany_df['cpc_level4_groups'] = germany_df['cpc'].apply(extract_cpc_level4_groups)
germany_df = germany_df.explode('cpc_level4_groups')
germany_df = germany_df.dropna(subset=['cpc_level4_groups'])

# Count patent filings per CPC group per year
filings_count = germany_df.groupby(['cpc_level4_groups', 'filing_year']).size().reset_index(name='count')

# Calculate EMA
smoothing_factor = 0.1
filings_count = filings_count.sort_values(by=['cpc_level4_groups', 'filing_year'])

def calculate_ema(group):
    group['ema'] = group['count'].ewm(alpha=smoothing_factor, adjust=False).mean()
    return group

# Apply EMA calculation, resetting index to avoid ambiguity
ema_df = filings_count.groupby('cpc_level4_groups', group_keys=False).apply(calculate_ema).reset_index(drop=True)

# Find the best year for each CPC group
best_years = ema_df.loc[ema_df.groupby('cpc_level4_groups')['ema'].idxmax()]

# Get unique CPC level 4 codes for fetching full titles
unique_cpc_codes = best_years['cpc_level4_groups'].unique().tolist()

result = {
    'best_years_ema': best_years.to_dict(orient='records'),
    'unique_cpc_codes': unique_cpc_codes
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16368827637550378910': 'file_storage/function-call-16368827637550378910.json'}

exec(code, env_args)
