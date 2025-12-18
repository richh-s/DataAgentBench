code = """import json
import pandas as pd
import re

# Load the data from the JSON file
with open(locals()['var_function-call-13877299948745859293'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Extract filing_year using regex
df['filing_year'] = df['filing_date'].str.extract(r'\b(\d{4})\b').astype(float).fillna(-1).astype(int)

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

# Drop rows where cpc_code is empty after parsing (should not happen if parse_cpc_codes is robust)
df_exploded = df_exploded[df_exploded['cpc_code'].astype(bool)]


# Group by cpc_code and filing_year to count patents
patent_counts = df_exploded.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Get all unique CPC codes and all years to ensure all combinations exist for EMA calculation
all_cpc_codes = patent_counts['cpc_code'].unique()
all_years = range(patent_counts['filing_year'].min(), patent_counts['filing_year'].max() + 1)

# Create a complete dataframe with all CPC codes and years, filling missing counts with 0
full_index = pd.MultiIndex.from_product([all_cpc_codes, all_years], names=['cpc_code', 'filing_year'])
patent_counts_full = patent_counts.set_index(['cpc_code', 'filing_year']).reindex(full_index, fill_value=0).reset_index()

# Sort for EMA calculation
patent_counts_full.sort_values(by=['cpc_code', 'filing_year'], inplace=True)

# Calculate EMA
smoothing_factor = 0.2
patent_counts_full['ema'] = patent_counts_full.groupby('cpc_code')['patent_count'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

# Find the year with the highest EMA for each CPC code
# Use idxmax to get the index of the max EMA for each group, then loc to retrieve the full row
best_ema_year = patent_counts_full.loc[patent_counts_full.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_best_in_2022 = best_ema_year[best_ema_year['filing_year'] == 2022]['cpc_code'].tolist()

print("__RESULT__:")
print(json.dumps(cpc_best_in_2022))"""

env_args = {'var_function-call-13877299948745859293': 'file_storage/function-call-13877299948745859293.json'}

exec(code, env_args)
