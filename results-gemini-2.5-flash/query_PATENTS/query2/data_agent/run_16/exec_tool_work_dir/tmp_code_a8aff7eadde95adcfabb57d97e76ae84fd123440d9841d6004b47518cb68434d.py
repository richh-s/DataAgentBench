code = """import pandas as pd
import json
import re

def parse_date(date_str):
    try:
        # Prioritize parsing formats that are more likely to succeed
        if 'dated ' in date_str:
            date_str = date_str.replace('dated ', '')
        # Handle cases like "March the 18th, 2019"
        date_str = re.sub(r'(st|nd|rd|th),', ',', date_str)
        return pd.to_datetime(date_str, errors='coerce', dayfirst=False)
    except:
        return pd.NaT

def extract_country_code(patent_info):
    match = re.search(r'(ID\s+([A-Z]{2})-\d+)|(In\s+([A-Z]{2}),)', patent_info)
    if match:
        return match.group(2) or match.group(4)
    return None

with open(locals()['var_function-call-297126640787404012'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['grant_date'] = df['grant_date'].apply(parse_date)
df['filing_date'] = df['filing_date'].apply(parse_date)

# Filter for patents granted in the second half of 2019
df_filtered = df[(df['grant_date'].dt.year == 2019) & (df['grant_date'].dt.month >= 7)].copy()

# Extract country code and filter for Germany
df_filtered['country_code'] = df_filtered['Patents_info'].apply(extract_country_code)
df_germany = df_filtered[df_filtered['country_code'] == 'DE'].copy()

# Process CPC codes more efficiently
cpc_data = []
for index, row in df_germany.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        filing_year = row['filing_date'].year
        for cpc_item in cpc_list:
            code = cpc_item['code']
            if len(code) >= 4:
                cpc_group_4 = code[:4]
                cpc_data.append({'cpc_group_4': cpc_group_4, 'filing_year': filing_year})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(cpc_data)

# Calculate filings per CPC group per year
filings_by_cpc_year = cpc_df.groupby(['cpc_group_4', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA)
smoothing_factor = 0.1

def calculate_ema(group):
    group = group.sort_values(by='filing_year')
    group['ema'] = group['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    return group

ema_calculated_df = filings_by_cpc_year.groupby('cpc_group_4', group_keys=False).apply(calculate_ema)

# Find the best year (highest EMA) for each CPC group
best_ema_for_cpc = ema_calculated_df.loc[ema_calculated_df.groupby('cpc_group_4')['ema'].idxmax()]

# Select relevant columns
final_ema_results = best_ema_for_cpc[['cpc_group_4', 'filing_year', 'ema']].rename(columns={'filing_year': 'best_year', 'ema': 'max_ema'})

print("__RESULT__:")
print(final_ema_results.to_json(orient='records'))"""

env_args = {'var_function-call-297126640787404012': 'file_storage/function-call-297126640787404012.json'}

exec(code, env_args)
