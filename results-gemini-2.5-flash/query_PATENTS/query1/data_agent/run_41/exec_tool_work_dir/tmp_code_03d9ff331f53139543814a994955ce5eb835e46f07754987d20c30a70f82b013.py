code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-5368828586906124532'], 'r') as f:
    data = json.load(f)

cpc_filing_data = []
for record in data:
    cpc_codes_str = record.get('cpc')
    filing_date_str = record.get('filing_date')

    if cpc_codes_str and filing_date_str:
        try:
            cpc_list = json.loads(cpc_codes_str)
            
            # Extract year from filing_date
            year_match = re.search(r'\d{4}', filing_date_str)
            filing_year = int(year_match.group(0)) if year_match else None

            if filing_year:
                for cpc_item in cpc_list:
                    cpc_code = cpc_item.get('code')
                    if cpc_code:
                        cpc_filing_data.append({'cpc_code': cpc_code, 'filing_year': filing_year})
        except json.JSONDecodeError:
            # Handle cases where cpc is not a valid JSON string
            continue

df_cpc_filing = pd.DataFrame(cpc_filing_data)

# Extract the group code (first 4 characters) and subgroup (remaining)
df_cpc_filing['cpc_group'] = df_cpc_filing['cpc_code'].apply(lambda x: x[:4] if x else None)

# Count filings per cpc_code per year
filings_per_year_cpc = df_cpc_filing.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA for each cpc_code
smoothing_factor = 0.2
ema_data = []

for cpc_code in filings_per_year_cpc['cpc_code'].unique():
    cpc_df = filings_per_year_cpc[filings_per_year_cpc['cpc_code'] == cpc_code].sort_values(by='filing_year')
    cpc_df['ema'] = cpc_df['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    ema_data.append(cpc_df)

if ema_data:
    ema_df = pd.concat(ema_data)
else:
    ema_df = pd.DataFrame(columns=['cpc_code', 'filing_year', 'filings', 'ema'])

# Find the best year (highest EMA) for each cpc_code
best_year_ema = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_codes_best_2022 = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_code'].unique().tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_best_2022))"""

env_args = {'var_function-call-5368828586906124532': 'file_storage/function-call-5368828586906124532.json'}

exec(code, env_args)
