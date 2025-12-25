code = """import json
import re
import pandas as pd

# Load the publication info data
with open(locals()['var_function-call-5368828586906124532'], 'r') as f:
    publication_data = json.load(f)

# Load level 5 CPC symbols
with open(locals()['var_function-call-317718304673024433'], 'r') as f:
    level5_symbols_raw = json.load(f)
level5_symbols = {item['symbol'] for item in level5_symbols_raw}

processed_records = []
for record in publication_data:
    cpc_codes_str = record.get('cpc')
    filing_date_str = record.get('filing_date')

    if cpc_codes_str and filing_date_str:
        try:
            cpc_list = json.loads(cpc_codes_str)
            year_match = re.search(r'\\d{4}', filing_date_str)
            filing_year = int(year_match.group(0)) if year_match else None

            if filing_year:
                for cpc_item in cpc_list:
                    cpc_code = cpc_item.get('code')
                    if cpc_code:
                        # Extract the first 4 characters for group code level check
                        cpc_group_code = cpc_code[:4]
                        if cpc_group_code in level5_symbols:
                            processed_records.append({'cpc_code': cpc_code, 'filing_year': filing_year})
        except json.JSONDecodeError:
            continue

df_cpc_filing = pd.DataFrame(processed_records)

# Count filings per cpc_code per year
filings_per_year_cpc = df_cpc_filing.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA for each cpc_code
smoothing_factor = 0.2

# Use apply with groupby for efficient EMA calculation
def calculate_ema(group):
    group = group.sort_values(by='filing_year')
    group['ema'] = group['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    return group

ema_df = filings_per_year_cpc.groupby('cpc_code').apply(calculate_ema)

# Find the best year (highest EMA) for each cpc_code
best_year_ema = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022 and extract the group code at level 5
cpc_codes_best_2022_level5 = []
for cpc_code in best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_code'].unique():
    cpc_group_code = cpc_code[:4]  # Get the group code (first 4 characters)
    if cpc_group_code in level5_symbols:
        cpc_codes_best_2022_level5.append(cpc_group_code)

# Ensure uniqueness and convert to list
final_result = sorted(list(set(cpc_codes_best_2022_level5)))

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_function-call-5368828586906124532': 'file_storage/function-call-5368828586906124532.json', 'var_function-call-317718304673024433': 'file_storage/function-call-317718304673024433.json'}

exec(code, env_args)
