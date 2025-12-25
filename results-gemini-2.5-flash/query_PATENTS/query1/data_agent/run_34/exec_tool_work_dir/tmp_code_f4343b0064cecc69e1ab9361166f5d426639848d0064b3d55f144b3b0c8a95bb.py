code = """import json
import pandas as pd
import re

# Load the large JSON data from the file
with open(locals()['var_function-call-1961943814564711613'], 'r') as f:
    data = json.load(f)

# Initialize lists to store parsed data
cpc_codes = []
filing_years = []

for record in data:
    cpc_str = record['cpc']
    filing_date_str = record['filing_date']

    # Extract year from filing_date using regex
    filing_year = None
    if filing_date_str:
        # Look for a 4-digit number that could be a year
        year_match = re.search(r'\b(19|20)\d{2}\b', filing_date_str)
        if year_match:
            year_int = int(year_match.group(0))
            if 1900 <= year_int <= 2023: # Filter for reasonable years
                filing_year = year_int
    
    # Parse CPC codes
    if cpc_str:
        try:
            cpc_entries = json.loads(cpc_str)
            for entry in cpc_entries:
                cpc_codes.append(entry['code'])
                filing_years.append(filing_year)
        except json.JSONDecodeError:
            # If cpc_str is not valid JSON, skip this record's CPCs
            continue

# Create a DataFrame
df_filings = pd.DataFrame({'cpc_code': cpc_codes, 'filing_year': filing_years})

# Drop rows where filing_year is None
df_filings.dropna(subset=['filing_year'], inplace=True)
df_filings['filing_year'] = df_filings['filing_year'].astype(int)

# Count filings per CPC code per year
filings_per_year = df_filings.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filing_count')

# Get min and max year from the actual data for more realistic range
min_year = filings_per_year['filing_year'].min()
max_year = filings_per_year['filing_year'].max()
all_years = pd.Series(range(min_year, max_year + 1))

# Create a cartesian product of all CPC codes and all years to fill missing years with 0
unique_cpc_codes = filings_per_year['cpc_code'].unique()
all_combinations = pd.MultiIndex.from_product([unique_cpc_codes, all_years], names=['cpc_code', 'filing_year']).to_frame(index=False)
filings_per_year_complete = pd.merge(all_combinations, filings_per_year, on=['cpc_code', 'filing_year'], how='left').fillna(0)

# Sort for EMA calculation
filings_per_year_complete = filings_per_year_complete.sort_values(by=['cpc_code', 'filing_year'])

# Calculate EMA (smoothing factor 0.2)
alpha = 0.2
filings_per_year_complete['ema'] = filings_per_year_complete.groupby('cpc_code')['filing_count'].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# Find the year with the highest EMA for each CPC code
idx_max_ema = filings_per_year_complete.groupby('cpc_code')['ema'].idxmax()
best_year_ema = filings_per_year_complete.loc[idx_max_ema, ['cpc_code', 'filing_year', 'ema']]
best_year_ema = best_year_ema.rename(columns={'filing_year': 'best_ema_year'})

# Filter for CPC codes whose best year is 2022
cpc_best_2022 = best_year_ema[best_year_ema['best_ema_year'] == 2022]['cpc_code'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_best_2022))"""

env_args = {'var_function-call-17019213161780401760': 'file_storage/function-call-17019213161780401760.json', 'var_function-call-1961943814564711613': 'file_storage/function-call-1961943814564711613.json', 'var_function-call-13243559376153268010': []}

exec(code, env_args)
