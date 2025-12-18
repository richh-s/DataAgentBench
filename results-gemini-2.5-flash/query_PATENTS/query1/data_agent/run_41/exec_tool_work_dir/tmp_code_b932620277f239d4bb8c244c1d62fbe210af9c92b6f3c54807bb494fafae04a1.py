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
                    full_cpc_code = cpc_item.get('code')
                    if full_cpc_code and len(full_cpc_code) >= 4:
                        # Extract the first 4 characters, which represents the level 5 group
                        cpc_group_code_level5 = full_cpc_code[:4]
                        if cpc_group_code_level5 in level5_symbols:
                            processed_records.append({'cpc_group_code': cpc_group_code_level5, 'filing_year': filing_year})
        except json.JSONDecodeError:
            continue

df_cpc_filing_level5 = pd.DataFrame(processed_records)

# Count filings per cpc_group_code per year
filings_per_year_cpc_group = df_cpc_filing_level5.groupby(['cpc_group_code', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA for each cpc_group_code
smoothing_factor = 0.2

def calculate_ema(group):
    # Ensure years are sorted for correct EMA calculation
    group = group.sort_values(by='filing_year')
    group['ema'] = group['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    return group

ema_df = filings_per_year_cpc_group.groupby('cpc_group_code', group_keys=False).apply(calculate_ema)

# Find the best year (highest EMA) for each cpc_group_code
best_year_ema = ema_df.loc[ema_df.groupby('cpc_group_code')['ema'].idxmax()]

# Filter for CPC group codes whose best year is 2022
cpc_groups_best_2022 = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_group_code'].unique().tolist()

# Ensure uniqueness and sort the final result
final_result = sorted(list(set(cpc_groups_best_2022)))

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_function-call-5368828586906124532': 'file_storage/function-call-5368828586906124532.json', 'var_function-call-317718304673024433': 'file_storage/function-call-317718304673024433.json'}

exec(code, env_args)
