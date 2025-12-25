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
        # Handle cases like "2013 on Oct 29th" or "March the 7th, 2014"
        parts = date_str.replace("the ", "").replace("on ", "").split()
        for part in parts:
            if part.isdigit() and len(part) == 4:
                return int(part)
    return None

germany_df['filing_year'] = germany_df['filing_date'].apply(extract_year)
germany_df = germany_df.dropna(subset=['filing_year'])

# Extract level 4 CPC codes
def extract_cpc_level4(cpc_json_str):
    if pd.isna(cpc_json_str):
        return []
    cpc_list = json.loads(cpc_json_str)
    level4_codes = []
    for cpc_item in cpc_list:
        code = cpc_item.get('code')
        if code and len(code) >= 4:
            # CPC level 4 is typically the first 4 characters followed by a slash and then 1 or 2 digits,
            # or it can be just the first 4 characters.
            # Example: A61B, A61B 5, A61B 5/00
            # For this problem, we need level 4 which usually means the first four characters of the code.
            # Let's consider the group code up to the slash or the end if no slash
            if '/' in code:
                level4_codes.append(code.split('/')[0])
            else:
                level4_codes.append(code)
    return list(set(level4_codes)) # Get unique level 4 codes for a patent

all_cpc_level4 = germany_df['cpc'].apply(extract_cpc_level4)
germany_df = germany_df.assign(cpc_level4_groups=all_cpc_level4)
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

ema_df = filings_count.groupby('cpc_level4_groups').apply(calculate_ema)

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
