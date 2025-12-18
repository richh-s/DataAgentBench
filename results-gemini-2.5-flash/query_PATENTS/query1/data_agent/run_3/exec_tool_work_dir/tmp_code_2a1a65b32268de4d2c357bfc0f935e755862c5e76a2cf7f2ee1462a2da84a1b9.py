code = """import pandas as pd
import json
import re

# Load the full results from the file
with open(locals()['var_function-call-10409098930881503150'], 'r') as f:
    publication_data = json.load(f)

# Create a list to store extracted CPC codes and years
extracted_data = []

# Process each patent record
for record in publication_data:
    cpc_field = record.get('cpc')
    filing_date_str = record.get('filing_date')

    if cpc_field and filing_date_str:
        try:
            # Extract year from filing_date
            year_match = re.search(r'\d{4}', filing_date_str)
            if year_match:
                year = int(year_match.group(0))

                # Parse the CPC JSON string
                cpc_entries = json.loads(cpc_field)

                for cpc_entry in cpc_entries:
                    code = cpc_entry.get('code')
                    if code:
                        extracted_data.append({'cpc_code': code, 'filing_year': year})
            else:
                # Handle cases where year is not found in filing_date_str
                pass
        except (json.JSONDecodeError, AttributeError, ValueError):
            # Handle cases where cpc_field is not valid JSON or other parsing errors
            pass

df_patents = pd.DataFrame(extracted_data)

# Filter for CPC codes at level 5
with open(locals()['var_function-call-4957076699531855933'], 'r') as f:
    cpc_level_5_data = json.load(f)

cpc_level_5_symbols = {item['symbol'] for item in cpc_level_5_data if item.get('level') == '5.0'}

# Extract the group code (first 4 characters) for comparison with level 5 symbols
df_patents['cpc_group'] = df_patents['cpc_code'].apply(lambda x: x[:4] if len(x) >= 4 else None)
df_filtered_level_5 = df_patents[df_patents['cpc_group'].isin(cpc_level_5_symbols)]


# Count patent filings per CPC group and year
filings_per_cpc_year = df_filtered_level_5.groupby(['cpc_group', 'filing_year']).size().reset_index(name='filings')

# Fill in missing years with 0 filings for each CPC group
all_years = range(filings_per_cpc_year['filing_year'].min(), filings_per_cpc_year['filing_year'].max() + 1)
all_cpc_groups = filings_per_cpc_year['cpc_group'].unique()

# Create a complete DataFrame with all CPC groups and years
full_index = pd.MultiIndex.from_product([all_cpc_groups, all_years], names=['cpc_group', 'filing_year'])
full_df = pd.DataFrame(index=full_index).reset_index()
filings_per_cpc_year = pd.merge(full_df, filings_per_cpc_year, on=['cpc_group', 'filing_year'], how='left').fillna(0)


# Calculate EMA for each CPC group
smoothing_factor = 0.2
ema_results = []

for cpc_group in all_cpc_groups:
    cpc_group_data = filings_per_cpc_year[filings_per_cpc_year['cpc_group'] == cpc_group].sort_values('filing_year')
    ema = cpc_group_data['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    for year, value in zip(cpc_group_data['filing_year'], ema):
        ema_results.append({'cpc_group': cpc_group, 'year': year, 'ema': value})

df_ema = pd.DataFrame(ema_results)

# Identify the best year for each CPC group
idx = df_ema.groupby('cpc_group')['ema'].idxmax()
best_year_cpc = df_ema.loc[idx]

# Filter for best year being 2022
cpc_best_in_2022 = best_year_cpc[best_year_cpc['year'] == 2022]['cpc_group'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_best_in_2022))"""

env_args = {'var_function-call-10409098930881503150': 'file_storage/function-call-10409098930881503150.json', 'var_function-call-4957076699531855933': 'file_storage/function-call-4957076699531855933.json'}

exec(code, env_args)
