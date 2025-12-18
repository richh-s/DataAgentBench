code = """import pandas as pd
import json
import re

# Load the large JSON data from the file
with open(locals()['var_function-call-12031246827532621766'], 'r') as f:
    data = json.load(f)

df_raw = pd.DataFrame(data)

# Efficient Date Parsing
df_raw['year'] = pd.to_datetime(df_raw['filing_date'], errors='coerce').dt.year
df_raw = df_raw.dropna(subset=['year'])
df_raw['year'] = df_raw['year'].astype(int)

# Function to extract and filter CPC codes
def extract_level5_cpc(cpc_json_str):
    codes = []
    if pd.isna(cpc_json_str):
        return codes
    try:
        cpc_entries = json.loads(cpc_json_str)
        for entry in cpc_entries:
            cpc_code = entry.get('code')
            if cpc_code:
                # Level 5 heuristic: contains '/' and has at least two digits after it.
                # Example: A01B1/00 (8 chars), B60W30/0803 (10 chars)
                # A simpler regex to identify codes that likely are level 5 or deeper:
                # Should have a '/' followed by digits, and be long enough.
                cleaned_code = cpc_code.replace(' ', '')
                if re.match(r'^[A-Z]{1}\d{2}[A-Z]{1}\d{1,3}/\d{2,}', cleaned_code):
                    codes.append(cleaned_code)
    except json.JSONDecodeError:
        pass
    return codes

# Apply the extraction function
df_raw['level5_cpc_codes'] = df_raw['cpc'].apply(extract_level5_cpc)

# Explode the list of CPC codes into separate rows
df_exploded = df_raw.explode('level5_cpc_codes')

# Drop rows where level5_cpc_codes is empty (no level 5 codes found)
df_exploded = df_exploded.dropna(subset=['level5_cpc_codes'])

# Count filings per CPC code and year
yearly_filings = df_exploded.groupby(['level5_cpc_codes', 'year']).size().reset_index(name='filings')

# Calculate EMA for each CPC code
smoothing_factor = 0.2
ema_results = []

# Process only if yearly_filings is not empty
if not yearly_filings.empty:
    for cpc_code in yearly_filings['level5_cpc_codes'].unique():
        cpc_df = yearly_filings[yearly_filings['level5_cpc_codes'] == cpc_code].sort_values(by='year')
        cpc_df['ema'] = cpc_df['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
        ema_results.append(cpc_df)

if ema_results:
    ema_df = pd.concat(ema_results)
else:
    ema_df = pd.DataFrame(columns=['level5_cpc_codes', 'year', 'filings', 'ema'])

# Find the best year (highest EMA) for each CPC code
if not ema_df.empty:
    idx = ema_df.groupby('level5_cpc_codes')['ema'].idxmax()
    best_years_df = ema_df.loc[idx]

    # Filter for CPC codes whose best year is 2022
    cpc_codes_2022_best = best_years_df[best_years_df['year'] == 2022]['level5_cpc_codes'].tolist()
else:
    cpc_codes_2022_best = []

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-12031246827532621766': 'file_storage/function-call-12031246827532621766.json'}

exec(code, env_args)
