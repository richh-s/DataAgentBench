code = """import pandas as pd
import json

df = pd.read_json(locals()['var_function-call-15163413259859991045'])

# Filter for patents granted in the second half of 2019 in Germany
def parse_date(date_str):
    if isinstance(date_str, str):
        date_str = date_str.lower()
        if 'jan' in date_str or 'feb' in date_str or 'mar' in date_str or 'apr' in date_str or 'may' in date_str or 'jun' in date_str:
            return None # First half of the year
        if 'jul' in date_str or 'aug' in date_str or 'sep' in date_str or 'oct' in date_str or 'nov' in date_str or 'dec' in date_str:
            return True # Second half of the year
    return None

df['grant_date_parsed'] = df['grant_date'].apply(parse_date)
df = df[df['grant_date_parsed'] == True]
df = df[df['Patents_info'].str.contains('country_code_DE')]

# Extract filing year
def extract_year(date_str):
    if isinstance(date_str, str):
        for part in date_str.replace(',', '').split():
            if part.isdigit() and len(part) == 4:
                return int(part)
    return None

df['filing_year'] = df['filing_date'].apply(extract_year)
df = df.dropna(subset=['filing_year'])

# Extract CPC codes at level 4
cpc_codes = []
for index, row in df.iterrows():
    cpc_list = json.loads(row['cpc'])
    for cpc_item in cpc_list:
        code = cpc_item['code']
        if len(code) >= 4:
            cpc_group_4 = code[:4]
            cpc_codes.append({'cpc_group_code': cpc_group_4, 'filing_year': row['filing_year']})

cpc_df = pd.DataFrame(cpc_codes)

# Calculate yearly counts and EMA
yearly_counts = cpc_df.groupby(['cpc_group_code', 'filing_year']).size().reset_index(name='count')
yearly_counts = yearly_counts.sort_values(by=['cpc_group_code', 'filing_year'])

ema_results = {}
alpha = 0.1
for cpc_group in yearly_counts['cpc_group_code'].unique():
    group_data = yearly_counts[yearly_counts['cpc_group_code'] == cpc_group].copy()
    group_data['ema'] = group_data['count'].ewm(alpha=alpha, adjust=False).mean()
    if not group_data.empty:
        best_year_row = group_data.loc[group_data['ema'].idxmax()]
        ema_results[cpc_group] = {'best_year': int(best_year_row['filing_year']), 'max_ema': best_year_row['ema']}

# Convert ema_results to a list of dictionaries for easier merging
ema_results_list = [{'cpc_group_code': k, 'best_year': v['best_year'], 'max_ema': v['max_ema']} for k, v in ema_results.items()]
ema_df = pd.DataFrame(ema_results_list)

# Sort by EMA in descending order
ema_df = ema_df.sort_values(by='max_ema', ascending=False)

# Get top CPC groups (e.g., top 10 for demonstration, adjust as needed)
top_cpc_groups = ema_df.head(10)

print('__RESULT__:')
print(top_cpc_groups.to_json(orient='records'))"""

env_args = {'var_function-call-11468183013790806528': ['publicationinfo'], 'var_function-call-11468183013790806491': ['cpc_definition'], 'var_function-call-15232240169378814865': [], 'var_function-call-14515858273810460582': 'file_storage/function-call-14515858273810460582.json', 'var_function-call-15163413259859991045': 'file_storage/function-call-15163413259859991045.json'}

exec(code, env_args)
