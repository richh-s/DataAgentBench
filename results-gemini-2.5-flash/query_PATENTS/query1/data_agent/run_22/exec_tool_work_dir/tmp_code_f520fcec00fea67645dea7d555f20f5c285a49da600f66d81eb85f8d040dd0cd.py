code = """import pandas as pd
import json
import re

# Load the full result from the file
with open(locals()['var_function-call-2018874257286241520'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Extract year from 'filing_date' using str.extract
df['filing_year'] = df['filing_date'].str.extract(r'\b(\d{4})\b').astype(float)

# Filter out rows where filing_year is NaN and convert to int
df = df.dropna(subset=['filing_year'])
df['filing_year'] = df['filing_year'].astype(int)

# Parse 'cpc' JSON string and explode into separate rows
all_cpc_filings = []
for index, row in df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            all_cpc_filings.append({'cpc_code': cpc_item['code'], 'filing_year': row['filing_year']})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_filings_df = pd.DataFrame(all_cpc_filings)

# Filter for years up to 2022 (inclusive)
cpc_filings_df = cpc_filings_df[cpc_filings_df['filing_year'] <= 2022]

# Group by cpc_code and filing_year to count patents
patent_counts = cpc_filings_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Calculate Exponential Moving Average (EMA)
smoothing_factor = 0.2

ema_results = []
for cpc_code in patent_counts['cpc_code'].unique():
    cpc_data = patent_counts[patent_counts['cpc_code'] == cpc_code].sort_values(by='filing_year')
    
    # Initialize EMA for the first year
    if not cpc_data.empty:
        ema = cpc_data.iloc[0]['patent_count']
        ema_results.append({'cpc_code': cpc_code, 'filing_year': cpc_data.iloc[0]['filing_year'], 'ema': ema})

        # Calculate EMA for subsequent years
        for i in range(1, len(cpc_data)):
            current_patent_count = cpc_data.iloc[i]['patent_count']
            ema = (current_patent_count * smoothing_factor) + (ema * (1 - smoothing_factor))
            ema_results.append({'cpc_code': cpc_code, 'filing_year': cpc_data.iloc[i]['filing_year'], 'ema': ema})

ema_df = pd.DataFrame(ema_results)

# Find the best year for each CPC code
best_year_cpc = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for best year being 2022
best_year_2022_cpc_codes = best_year_cpc[best_year_cpc['filing_year'] == 2022]['cpc_code'].unique().tolist()

print('__RESULT__:')
print(json.dumps(best_year_2022_cpc_codes))"""

env_args = {'var_function-call-2018874257286241520': 'file_storage/function-call-2018874257286241520.json'}

exec(code, env_args)
