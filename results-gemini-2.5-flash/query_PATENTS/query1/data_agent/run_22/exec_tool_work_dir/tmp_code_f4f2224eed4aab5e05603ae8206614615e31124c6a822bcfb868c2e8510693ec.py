code = """import pandas as pd
import json
import re

# Load patent publication data
with open(locals()['var_function-call-2018874257286241520'], 'r') as f:
    publication_data = json.load(f)

publications_df = pd.DataFrame(publication_data)

# Extract year from 'filing_date'
def extract_year(date_string):
    if isinstance(date_string, str):
        match = re.search(r'\b(\d{4})\b', date_string)
        if match:
            return int(match.group(1))
    return None

publications_df['filing_year'] = publications_df['filing_date'].apply(extract_year)

# Filter out rows with invalid filing years and convert to int
publications_df = publications_df.dropna(subset=['filing_year'])
publications_df['filing_year'] = publications_df['filing_year'].astype(int)

# Process CPC codes and explode into separate rows
all_cpc_filings = []
for _, row in publications_df.iterrows():
    try:
        if isinstance(row['cpc'], str):
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
    
    if not cpc_data.empty:
        ema = cpc_data.iloc[0]['patent_count']
        ema_results.append({'cpc_code': cpc_code, 'filing_year': cpc_data.iloc[0]['filing_year'], 'ema': ema})

        for i in range(1, len(cpc_data)):
            current_patent_count = cpc_data.iloc[i]['patent_count']
            ema = (current_patent_count * smoothing_factor) + (ema * (1 - smoothing_factor))
            ema_results.append({'cpc_code': cpc_code, 'filing_year': cpc_data.iloc[i]['filing_year'], 'ema': ema})

ema_df = pd.DataFrame(ema_results)

# Find the best year for each CPC code (highest EMA)
best_year_cpc = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for best year being 2022
cpc_best_year_2022 = best_year_cpc[best_year_cpc['filing_year'] == 2022]['cpc_code'].unique().tolist()

# Load level 5 CPC codes from CPCDefinition_database
with open(locals()['var_function-call-5891838390981204155'], 'r') as f:
    level_5_cpc_data = json.load(f)

level_5_cpc_symbols = {item['symbol'] for item in level_5_cpc_data}

# Filter for CPC codes that are also at level 5
final_cpc_codes = [code for code in cpc_best_year_2022 if code in level_5_cpc_symbols]

print('__RESULT__:')
print(json.dumps(final_cpc_codes))"""

env_args = {'var_function-call-2018874257286241520': 'file_storage/function-call-2018874257286241520.json', 'var_function-call-10242324406622312450': ['cpc_definition'], 'var_function-call-13458682655913919725': 'file_storage/function-call-13458682655913919725.json', 'var_function-call-5891838390981204155': 'file_storage/function-call-5891838390981204155.json'}

exec(code, env_args)
