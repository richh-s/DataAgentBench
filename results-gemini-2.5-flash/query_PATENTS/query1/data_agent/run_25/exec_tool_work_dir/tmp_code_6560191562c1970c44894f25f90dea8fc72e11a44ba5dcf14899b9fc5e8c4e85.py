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

# Extract just the symbol strings from the level 5 CPC data
cpc_level_5_symbols = {entry['symbol'] for entry in cpc_level_5_symbols_raw if 'symbol' in entry}

# Function to extract year from filing_date
def extract_year(date_string):
    if isinstance(date_string, str):
        match = re.search(r'\b(\d{4})\b', date_string)
        if match:
            return int(match.group(1))
    return None

# Function to extract all CPC codes and filter for level 5
def extract_and_filter_cpc_codes(cpc_json_string, level_5_codes):
    extracted_cpc_codes = []
    if isinstance(cpc_json_string, str):
        try:
            cpc_entries = json.loads(cpc_json_string)
            for entry in cpc_entries:
                code = entry.get('code')
                # Normalizing the CPC code to match the format in CPCDefinition_database if necessary.
                # The CPCDefinition_database has symbols like A01H, which means we should consider only the first 4-7 characters.
                # Assuming level 5 codes are of format 'A01B33/00' where A01B33 is the level 5 code.
                # We need to extract the part before '/' and then remove the non-alphanumeric character.
                if code:
                    # Attempt to standardize the code format for comparison
                    standardized_code = code.split('/')[0].strip()
                    # Level 5 codes in CPCDefinition_database are typically 4 characters + 2 digits (e.g., A01B33).
                    # We need to consider variants where it could be like A01H, A01B, or longer forms that resolve to level 5.
                    # For instance, if the symbol is 'A01B33/00', the level 5 part is 'A01B33'.
                    # if the symbol is 'A01B', it's a higher level, so we are looking for more specific ones.
                    # A common format for level 5 could be 7 characters (e.g., A01B33/00 becomes A01B33).

                    # Check for codes like 'A01H'
                    if standardized_code in level_5_codes:
                        extracted_cpc_codes.append(standardized_code)
                    # Check for codes like 'A01B33'
                    elif len(standardized_code) >= 6 and standardized_code[:6] in level_5_codes:
                        extracted_cpc_codes.append(standardized_code[:6])
                    # Check for codes like 'A01B3300' (from previous logic)
                    elif len(standardized_code) >= 7 and standardized_code[:7] in level_5_codes:
                        extracted_cpc_codes.append(standardized_code[:7])
                    # Attempt to extract the first 4 characters and check against level 5 symbols.
                    # This covers cases like A01B being a level 5 symbol in itself if no further subdivision.
                    elif len(standardized_code) >= 4 and standardized_code[:4] in level_5_codes:
                        extracted_cpc_codes.append(standardized_code[:4])

        except json.JSONDecodeError:
            pass
    return list(set(extracted_cpc_codes))

df_patents['filing_year'] = df_patents['filing_date'].apply(extract_year)
df_patents['level_5_cpc'] = df_patents['cpc'].apply(lambda x: extract_and_filter_cpc_codes(x, cpc_level_5_symbols))

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
        best_year = cpc_df.loc[cpc_df['ema'].idxmax()]
        best_year_cpc[cpc_code] = best_year['filing_year']

# Filter for CPC codes whose best year is 2022
cpc_best_in_2022 = [cpc for cpc, year in best_year_cpc.items() if year == 2022]

print('__RESULT__:')
print(json.dumps(cpc_best_in_2022))"""

env_args = {'var_function-call-13225136143239241627': 'file_storage/function-call-13225136143239241627.json', 'var_function-call-11412886215749648234': [], 'var_function-call-17210150630757963510': [], 'var_function-call-11601473409543975109': 'file_storage/function-call-11601473409543975109.json'}

exec(code, env_args)
