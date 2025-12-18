code = """import pandas as pd
import json
import re

# Load the data from the large result file
with open(locals()['var_function-call-16843532275750202797']['query_db_response']['results'], 'r') as f:
    data = json.load(f)

filings_data = []
for record in data:
    # Extract filing year
    filing_date_str = record['filing_date']
    year_match = re.search(r'\d{4}', filing_date_str)
    year = int(year_match.group(0)) if year_match else None

    if year:
        # Parse CPC codes
        try:
            cpc_list = json.loads(record['cpc'])
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code')
                if code and len(code) >= 5 and re.match(r'^[A-Z]\d{2}[A-Z]\d{1,2}/\d+$', code): # Filter for level 5 CPC codes pattern, e.g., A01B1/00
                    filings_data.append({'year': year, 'cpc_code': code})
        except json.JSONDecodeError:
            continue

df = pd.DataFrame(filings_data)

# Count patent filings per CPC code per year
yearly_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA)
smoothing_factor = 0.2
ema_results = []

for cpc_code in yearly_counts['cpc_code'].unique():
    cpc_df = yearly_counts[yearly_counts['cpc_code'] == cpc_code].sort_values(by='year')
    if not cpc_df.empty:
        # Ensure all years are present for EMA calculation by reindexing
        all_years = range(cpc_df['year'].min(), cpc_df['year'].max() + 1)
        cpc_df_full = cpc_df.set_index('year').reindex(all_years, fill_value=0).reset_index()
        cpc_df_full['ema'] = cpc_df_full['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
        ema_results.append(cpc_df_full[['cpc_code', 'year', 'ema']])

if ema_results:
    ema_df = pd.concat(ema_results)

    # Identify best year for each CPC code
    idx = ema_df.groupby('cpc_code')['ema'].idxmax()
    best_years = ema_df.loc[idx]

    # Filter for best year 2022
    cpc_codes_best_in_2022 = best_years[best_years['year'] == 2022]['cpc_code'].tolist()
else:
    cpc_codes_best_in_2022 = []

print('__RESULT__:')
print(json.dumps(cpc_codes_best_in_2022))"""

env_args = {'var_function-call-16843532275750202797': 'file_storage/function-call-16843532275750202797.json'}

exec(code, env_args)
