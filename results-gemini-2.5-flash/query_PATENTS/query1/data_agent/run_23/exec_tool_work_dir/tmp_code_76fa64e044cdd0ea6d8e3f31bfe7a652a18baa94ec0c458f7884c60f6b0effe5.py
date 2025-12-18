code = """import pandas as pd
import json
import re

# Load publicationinfo data
data = pd.read_json(locals()['var_function-call-9499660023967929457'])

# Load cpc_definition data for level 5 symbols
with open(locals()['var_function-call-4508705775201837439'], 'r') as f:
    cpc_level5_data = json.load(f)
cpc_level5_df = pd.DataFrame(cpc_level5_data)
cpc_level5_df['level'] = pd.to_numeric(cpc_level5_df['level'])
level5_symbols = sorted(cpc_level5_df[cpc_level5_df['level'] == 5.0]['symbol'].tolist(), key=len, reverse=True)

# Function to parse year
def parse_year(date_str):
    if isinstance(date_str, str):
        match = re.search(r'\\d{4}', date_str)
        if match:
            return int(match.group(0))
    return None

data['filing_year'] = data['filing_date'].apply(parse_year)

# Filter for years up to 2022 early
data = data[data['filing_year'] <= 2022].copy()

# Parse 'cpc' column (JSON string) into actual list of dicts
data['cpc_parsed'] = data['cpc'].apply(lambda x: json.loads(x) if pd.notna(x) else [])

# Explode the cpc_parsed column to get one row per cpc code
exploded_cpc = data.explode('cpc_parsed')

# Extract the 'code' from the cpc_parsed dictionary
exploded_cpc['cpc_code_full'] = exploded_cpc['cpc_parsed'].apply(lambda x: x.get('code') if isinstance(x, dict) else None)

# Drop rows where cpc_code_full is None
exploded_cpc.dropna(subset=['cpc_code_full'], inplace=True)

# Create a mapping for unique full CPC codes to their level 5 parent
unique_cpc_full_codes = exploded_cpc['cpc_code_full'].unique()
cpc_to_level5_map = {}
for cpc_code_full in unique_cpc_full_codes:
    mapped_level5_code = None
    for symbol in level5_symbols: # Iterate sorted (longest first)
        if cpc_code_full.startswith(symbol):
            mapped_level5_code = symbol
            break # Found the most specific level 5 prefix
    cpc_to_level5_map[cpc_code_full] = mapped_level5_code

# Apply the pre-calculated mapping
exploded_cpc['level5_cpc_code'] = exploded_cpc['cpc_code_full'].map(cpc_to_level5_map)

# Drop rows where level5_cpc_code is None (meaning no level 5 mapping found)
exploded_cpc.dropna(subset=['level5_cpc_code'], inplace=True)

# Calculate annual filings for each mapped CPC code
annual_filings = exploded_cpc.groupby(['level5_cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Prepare for EMA calculation: Pivot to get years as columns
min_year = annual_filings['filing_year'].min() if not annual_filings.empty else 2022
max_year = annual_filings['filing_year'].max() if not annual_filings.empty else 2022
all_years = range(min_year, max_year + 1) # Use actual range of years present in the data for EMA

pivoted_filings = annual_filings.pivot_table(index='level5_cpc_code', columns='filing_year', values='patent_count').fillna(0)
pivoted_filings = pivoted_filings.reindex(columns=all_years, fill_value=0) # Ensure all years up to 2022 are present


# Calculate EMA
smoothing_factor = 0.2
ema_df = pivoted_filings.ewm(alpha=smoothing_factor, axis=1, adjust=False).mean()

# Find the best year for each CPC code based on EMA
best_year_series = ema_df.idxmax(axis=1)

# Filter for CPC codes whose best year is 2022
cpc_best_in_2022_ema = best_year_series[best_year_series == 2022].index.tolist()

print("__RESULT__:")
print(json.dumps(cpc_best_in_2022_ema))"""

env_args = {'var_function-call-14696505315028543546': 'file_storage/function-call-14696505315028543546.json', 'var_function-call-9499660023967929457': 'file_storage/function-call-9499660023967929457.json', 'var_function-call-17851144477517317510': 'file_storage/function-call-17851144477517317510.json', 'var_function-call-4508705775201837439': 'file_storage/function-call-4508705775201837439.json', 'var_function-call-16860636197230919779': []}

exec(code, env_args)
