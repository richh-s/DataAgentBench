code = """import json
import pandas as pd
import re
import numpy as np

# Load the large JSON data from the file for publication info
with open(locals()['var_function-call-1961943814564711613'], 'r') as f:
    publication_data = json.load(f)

# Load the large JSON data from the file for CPC definitions (with level information)
with open(locals()['var_function-call-18100120667767954602'], 'r') as f:
    cpc_definition_data = json.load(f)

# Extract actual level 5 CPC symbols from cpc_definition_data first
actual_level_5_cpc_symbols = set()
for entry in cpc_definition_data:
    if entry['symbol'] and 'level' in entry:
        try:
            if float(entry['level']) == 5.0:
                actual_level_5_cpc_symbols.add(entry['symbol'])
        except ValueError:
            continue

# Initialize lists to store parsed publication data
cpc_codes_filtered = []
filing_years_raw = []

for record in publication_data:
    cpc_str = record['cpc']
    filing_date_str = record['filing_date']

    # Extract year from filing_date using regex
    filing_year = np.nan # Use numpy.nan for missing values
    if filing_date_str:
        year_match = re.search(r'\b(19|20)\d{2}\b', filing_date_str)
        if year_match:
            year_int = int(year_match.group(0))
            if 1900 <= year_int <= 2023: # Filter for reasonable years
                filing_year = year_int
    
    # Parse CPC codes and filter immediately for actual level 5 codes
    if cpc_str:
        try:
            cpc_entries = json.loads(cpc_str)
            for entry in cpc_entries:
                original_cpc_code = entry['code']
                # Only add the code if it is an exact match to an actual level 5 symbol
                if original_cpc_code in actual_level_5_cpc_symbols:
                    cpc_codes_filtered.append(original_cpc_code)
                    filing_years_raw.append(filing_year)
        except json.JSONDecodeError:
            continue

# Create a DataFrame for filings with only level 5 CPC codes
df_filings = pd.DataFrame({'cpc_code': cpc_codes_filtered, 'filing_year': filing_years_raw})

# Drop rows where filing_year is NaN and convert to integer
df_filings.dropna(subset=['filing_year'], inplace=True)
df_filings['filing_year'] = df_filings['filing_year'].astype(int)

# Count filings per CPC code per year
filings_per_year = df_filings.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filing_count')

# Handle case where filings_per_year might be empty after filtering
if filings_per_year.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Get min and max year from the actual data for more realistic range
    min_year = int(filings_per_year['filing_year'].min())
    max_year = int(filings_per_year['filing_year'].max())
    all_years = pd.Series(range(min_year, max_year + 1), dtype=int)

    # Reindex each group to ensure all years are present for each CPC code
    def reindex_cpc_group(group):
        reindexed_group = group.set_index('filing_year')['filing_count'].reindex(all_years, fill_value=0).reset_index()
        reindexed_group['cpc_code'] = group['cpc_code'].iloc[0] # Add cpc_code back
        reindexed_group['filing_count'] = reindexed_group['filing_count'].astype(int)
        return reindexed_group

    filings_per_year_complete = filings_per_year.groupby('cpc_code').apply(reindex_cpc_group).reset_index(drop=True)

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
    final_cpc_best_2022 = best_year_ema[best_year_ema['best_ema_year'] == 2022]['cpc_code'].tolist()

    print('__RESULT__:')
    print(json.dumps(final_cpc_best_2022))"""

env_args = {'var_function-call-17019213161780401760': 'file_storage/function-call-17019213161780401760.json', 'var_function-call-1961943814564711613': 'file_storage/function-call-1961943814564711613.json', 'var_function-call-13243559376153268010': [], 'var_function-call-5899265488545421578': [], 'var_function-call-12980736389288638869': [], 'var_function-call-8742510392090125440': 'file_storage/function-call-8742510392090125440.json', 'var_function-call-14553140379206991239': [], 'var_function-call-18100120667767954602': 'file_storage/function-call-18100120667767954602.json', 'var_function-call-4084629753541667608': [], 'var_function-call-12256813177757523368': []}

exec(code, env_args)
