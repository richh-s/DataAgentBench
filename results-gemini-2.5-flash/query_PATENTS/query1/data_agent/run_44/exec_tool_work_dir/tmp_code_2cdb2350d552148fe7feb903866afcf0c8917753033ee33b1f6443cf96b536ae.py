code = """import json
import pandas as pd
import re

# Load the data from the JSON file
with open(locals()['var_function-call-13877299948745859293'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Extract filing_year using regex, resulting in floats (NaN for non-matches)
df['filing_year'] = df['filing_date'].str.extract(r'\b(\d{4})\b').astype(float)

# Drop rows where filing_year could not be extracted or is NaN
df.dropna(subset=['filing_year'], inplace=True)

# Convert filing_year to integer after dropping NaNs
df['filing_year'] = df['filing_year'].astype(int)

# Filter for valid years up to 2022
df = df[ (df['filing_year'] > 0) & (df['filing_year'] <= 2022) ]

# Process cpc codes
def parse_cpc_codes(cpc_str):
    try:
        cpc_list = json.loads(cpc_str)
        return [item['code'] for item in cpc_list if 'code' in item]
    except (json.JSONDecodeError, TypeError):
        return []

df['parsed_cpc_codes'] = df['cpc'].apply(parse_cpc_codes)

# Explode the list of CPC codes so each code gets its own row
df_exploded = df.explode('parsed_cpc_codes')

# Rename the column for clarity
df_exploded.rename(columns={'parsed_cpc_codes': 'cpc_code'}, inplace=True)

# Drop rows where cpc_code is empty after parsing
df_exploded = df_exploded[df_exploded['cpc_code'].astype(bool)]

# Group by cpc_code and filing_year to count patents
patent_counts = df_exploded.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Ensure min/max year are integers for range function
min_year = int(patent_counts['filing_year'].min())
max_year = int(patent_counts['filing_year'].max())

all_cpc_codes = patent_counts['cpc_code'].unique()
all_years = range(min_year, max_year + 1)

# Create a complete dataframe with all CPC codes and years, filling missing counts with 0
full_index = pd.MultiIndex.from_product([all_cpc_codes, all_years], names=['cpc_code', 'filing_year'])
patent_counts_full = patent_counts.set_index(['cpc_code', 'filing_year']).reindex(full_index, fill_value=0).reset_index()

# Sort for EMA calculation
patent_counts_full.sort_values(by=['cpc_code', 'filing_year'], inplace=True)

# Calculate EMA
smoothing_factor = 0.2
patent_counts_full['ema'] = patent_counts_full.groupby('cpc_code')['patent_count'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

# Find the year with the highest EMA for each CPC code
best_ema_year = patent_counts_full.loc[patent_counts_full.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022 and are level 5 group codes
cpc_best_in_2022_level5 = []
for cpc_code in best_ema_year[best_ema_year['filing_year'] == 2022]['cpc_code'].tolist():
    # A simple heuristic for level 5: 9 characters when '/' is removed (e.g., A61B5/00 -> A61B500)
    if len(cpc_code.replace('/', '')) == 9:
        cpc_best_in_2022_level5.append(cpc_code)

print("__RESULT__:")
print(json.dumps(cpc_best_in_2022_level5))"""

env_args = {'var_function-call-13877299948745859293': 'file_storage/function-call-13877299948745859293.json'}

exec(code, env_args)
