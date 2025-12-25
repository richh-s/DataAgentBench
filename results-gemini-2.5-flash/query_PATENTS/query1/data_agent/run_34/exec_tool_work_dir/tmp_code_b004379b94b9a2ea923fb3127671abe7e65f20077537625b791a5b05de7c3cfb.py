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

# Initialize lists to store parsed publication data
cpc_codes_raw = []
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
    
    # Parse CPC codes
    if cpc_str:
        try:
            cpc_entries = json.loads(cpc_str)
            for entry in cpc_entries:
                cpc_codes_raw.append(entry['code'])
                filing_years_raw.append(filing_year)
        except json.JSONDecodeError:
            # If cpc_str is not valid JSON, skip this record's CPCs
            continue

# Create a DataFrame for filings
df_filings = pd.DataFrame({'cpc_code': cpc_codes_raw, 'filing_year': filing_years_raw})

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

    # Create a cartesian product of all unique CPC codes and all years to fill missing years with 0
    unique_cpc_codes = filings_per_year['cpc_code'].unique()
    all_combinations = pd.MultiIndex.from_product([unique_cpc_codes, all_years], names=['cpc_code', 'filing_year']).to_frame(index=False)

    filings_per_year_complete = pd.merge(all_combinations, filings_per_year, on=['cpc_code', 'filing_year'], how='left')
    filings_per_year_complete['filing_count'] = filings_per_year_complete['filing_count'].fillna(0).astype(int) # Fillna before astype(int)

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
    cpc_best_2022_candidates = best_year_ema[best_year_ema['best_ema_year'] == 2022]['cpc_code'].tolist()

    # Extract level 5 CPC symbols from cpc_definition_data
    level_5_cpc_symbols = []
    for entry in cpc_definition_data:
        if entry['symbol'] and 'level' in entry:
            try:
                # Convert level to float first, then check if it's an integer 5
                if float(entry['level']) == 5.0:
                    level_5_cpc_symbols.append(entry['symbol'])
            except ValueError:
                # Handle cases where level might not be a valid float string
                continue

    # Create a set of valid level 5 CPC symbols for efficient lookup.
    valid_level_5_symbols_set = set(level_5_cpc_symbols)

    # Filter the cpc_best_2022_candidates to keep only those that are exactly in the level 5 symbols set
    final_cpc_best_2022 = [cpc for cpc in cpc_best_2022_candidates if cpc in valid_level_5_symbols_set]

    print('__RESULT__:')
    print(json.dumps(final_cpc_best_2022))"""

env_args = {'var_function-call-17019213161780401760': 'file_storage/function-call-17019213161780401760.json', 'var_function-call-1961943814564711613': 'file_storage/function-call-1961943814564711613.json', 'var_function-call-13243559376153268010': [], 'var_function-call-5899265488545421578': [], 'var_function-call-12980736389288638869': [], 'var_function-call-8742510392090125440': 'file_storage/function-call-8742510392090125440.json', 'var_function-call-14553140379206991239': [], 'var_function-call-18100120667767954602': 'file_storage/function-call-18100120667767954602.json'}

exec(code, env_args)
