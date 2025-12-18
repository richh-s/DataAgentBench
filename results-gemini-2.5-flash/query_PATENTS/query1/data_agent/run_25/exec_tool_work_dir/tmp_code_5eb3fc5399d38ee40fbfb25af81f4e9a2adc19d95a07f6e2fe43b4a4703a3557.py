code = """import pandas as pd
import json
import re

# Load patent data from the stored file
with open(locals()['var_function-call-13225136143239241627'], 'r') as f:
    patent_data = json.load(f)

df_patents = pd.DataFrame(patent_data)

# Load level 5 CPC symbols from the stored file
with open(locals()['var_function-call-11601473409543975109'], 'r') as f:
    cpc_level_5_symbols_raw = json.load(f)

# Extract just the symbol strings from the level 5 CPC data into a set for efficient lookup
cpc_level_5_symbols_set = {entry['symbol'] for entry in cpc_level_5_symbols_raw if 'symbol' in entry}

# Function to extract year from filing_date
def extract_year(date_string):
    if isinstance(date_string, str):
        match = re.search(r'\b(\d{4})\b', date_string)
        if match:
            return int(match.group(1))
    return None

# Function to extract and filter level 5 CPC codes from patent data
def extract_and_filter_cpc_codes(cpc_json_string, level_5_codes_set):
    extracted_cpc_codes = []
    if isinstance(cpc_json_string, str):
        try:
            cpc_entries = json.loads(cpc_json_string)
            for entry in cpc_entries:
                code = entry.get('code')
                if code:
                    # Clean the code: remove '/', spaces, and make uppercase
                    cleaned_code = code.split('/')[0].strip().upper()

                    # Iterate through possible lengths for level 5 CPC symbols (e.g., A01H, A01B33)
                    # Assuming level 5 symbols are typically 4 to 7 characters long after the section and class.
                    # The CPC Definition database contains symbols such as A01H (4 chars), A01B33 (6 chars).
                    # Let's check for these specific lengths.
                    possible_lengths = [4, 5, 6, 7]
                    matched_level_5_code = None

                    # Check longer prefixes first for a more specific match
                    for length in sorted(possible_lengths, reverse=True):
                        if len(cleaned_code) >= length:
                            prefix = cleaned_code[:length]
                            if prefix in level_5_codes_set:
                                matched_level_5_code = prefix
                                break # Found the longest match, so stop checking shorter ones

                    if matched_level_5_code:
                        extracted_cpc_codes.append(matched_level_5_code)

        except json.JSONDecodeError:
            pass
    return list(set(extracted_cpc_codes))

df_patents['filing_year'] = df_patents['filing_date'].apply(extract_year)
df_patents['level_5_cpc'] = df_patents['cpc'].apply(lambda x: extract_and_filter_cpc_codes(x, cpc_level_5_symbols_set))

# Explode the DataFrame to have one CPC code per row
df_exploded = df_patents.explode('level_5_cpc')

# Filter out rows with no valid year or CPC code
df_filtered = df_exploded.dropna(subset=['filing_year', 'level_5_cpc'])

# Count patent filings per CPC code per year
filings_per_year_cpc = df_filtered.groupby(['level_5_cpc', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA
smoothing_factor = 0.2
ema_results = {}

for cpc_code in filings_per_year_cpc['level_5_cpc'].unique():
    cpc_data = filings_per_year_cpc[filings_per_year_cpc['level_5_cpc'] == cpc_code].sort_values(by='filing_year')
    ema = []
    if not cpc_data.empty:
        # Initialize EMA with the first year's filings
        ema_current = cpc_data.iloc[0]['filings']
        ema.append(ema_current)
        for i in range(1, len(cpc_data)):
            ema_current = (cpc_data.iloc[i]['filings'] * smoothing_factor) + (ema_current * (1 - smoothing_factor))
            ema.append(ema_current)
    cpc_data['ema'] = ema
    ema_results[cpc_code] = cpc_data

# Find the best year (highest EMA) for each CPC code
best_year_cpc = {}
for cpc_code, cpc_df in ema_results.items():
    if not cpc_df.empty:
        # Ensure 'ema' column exists and is not empty before calling idxmax
        if 'ema' in cpc_df.columns and not cpc_df['ema'].empty:
            best_year_entry = cpc_df.loc[cpc_df['ema'].idxmax()]
            best_year_cpc[cpc_code] = best_year_entry['filing_year']

# Filter for CPC codes whose best year is 2022
cpc_best_in_2022 = [cpc for cpc, year in best_year_cpc.items() if year == 2022]

print('__RESULT__:')
print(json.dumps(cpc_best_in_2022))"""

env_args = {'var_function-call-13225136143239241627': 'file_storage/function-call-13225136143239241627.json', 'var_function-call-11412886215749648234': [], 'var_function-call-17210150630757963510': [], 'var_function-call-11601473409543975109': 'file_storage/function-call-11601473409543975109.json', 'var_function-call-16165218290343077891': []}

exec(code, env_args)
