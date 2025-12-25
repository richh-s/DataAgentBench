code = """import pandas as pd
import json
import re

# Load the data from the JSON file
with open(locals()['var_function-call-16624233199797624692'], 'r') as f:
    data = json.load(f)

# Create a list to store processed data
processed_data = []

for record in data:
    filing_date = record.get('filing_date')
    cpc_raw = record.get('cpc')

    if filing_date and cpc_raw:
        # Extract year from filing_date
        year_match = re.search(r'\\d{4}', filing_date)
        if year_match:
            year = int(year_match.group(0))
        else:
            continue

        # Parse CPC codes
        try:
            cpc_list = json.loads(cpc_raw)
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code')
                if code and len(code) >= 7 and code[4] == '/' and len(code.split('/')[0]) == 4:
                    # Extract level 5 CPC group code (e.g., A01B1/00)
                    # CPC group code at level 5 means taking the first 7 characters including the slash.
                    level_5_cpc = code[:7]
                    processed_data.append({'year': year, 'cpc_code': level_5_cpc})
        except json.JSONDecodeError:
            continue

df = pd.DataFrame(processed_data)

# Count patent filings per CPC code per year
filings_count = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')

# Calculate Exponential Moving Average (EMA)
smoothing_factor = 0.2
ema_dfs = [] # Changed to store DataFrames

# Sort by CPC code and year for correct EMA calculation
filings_count = filings_count.sort_values(by=['cpc_code', 'year'])

for cpc_code, group in filings_count.groupby('cpc_code'):
    group = group.sort_values(by='year').copy() # Add .copy() to avoid SettingWithCopyWarning
    ema_values = []
    if not group.empty:
        current_ema = group.iloc[0]['count']
        ema_values.append(current_ema)

        for i in range(1, len(group)):
            current_ema = (group.iloc[i]['count'] * smoothing_factor) + (current_ema * (1 - smoothing_factor))
            ema_values.append(current_ema)
    
    group['ema'] = ema_values
    ema_dfs.append(group) # Append the DataFrame

# Concatenate all the individual CPC dataframes with EMA values
if ema_dfs:
    ema_df = pd.concat(ema_dfs)
else:
    ema_df = pd.DataFrame(columns=['cpc_code', 'year', 'count', 'ema']) # Handle case where no data

# Find the best year for each CPC code
# Ensure 'cpc_code' is present before grouping
if not ema_df.empty:
    best_year_df = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

    # Filter for CPC codes whose best year is 2022
    cpc_codes_2022_best = best_year_df[best_year_df['year'] == 2022]['cpc_code'].tolist()
else:
    cpc_codes_2022_best = []

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-16624233199797624692': 'file_storage/function-call-16624233199797624692.json'}

exec(code, env_args)
