code = """import pandas as pd
import json
import re

df = pd.read_json(locals()['var_function-call-1868845643524759541'])

# Filter for patents granted in the second half of 2019 in Germany
def filter_german_2019_second_half(row):
    grant_date_str = row['grant_date'].lower()
    patents_info_str = row['Patents_info'].lower()

    # Check for second half of 2019
    is_2019_second_half = False
    if '2019' in grant_date_str:
        if any(month in grant_date_str for month in ['jul', 'aug', 'sep', 'oct', 'nov', 'dec']):
            is_2019_second_half = True

    # Check for Germany
    is_germany = False
    if 'country_code_de' in patents_info_str or '(no. de-' in patents_info_str or 'from de' in patents_info_str:
        is_germany = True

    return is_2019_second_half and is_germany

df_filtered = df[df.apply(filter_german_2019_second_half, axis=1)].copy()

# Extract filing year
def extract_year(date_str):
    if isinstance(date_str, str):
        match = re.search(r'\b(20\d{2}|19\d{2})\b', date_str)
        if match:
            return int(match.group(0))
    return None

df_filtered['filing_year'] = df_filtered['filing_date'].apply(extract_year)
df_filtered = df_filtered.dropna(subset=['filing_year'])

# Extract CPC codes at level 4
cpc_codes_list = []
for index, row in df_filtered.iterrows():
    try:
        cpc_data = json.loads(row['cpc'])
        for cpc_item in cpc_data:
            code = cpc_item['code']
            if len(code) >= 4:
                cpc_group_4 = code[:4]
                cpc_codes_list.append({'cpc_group_code': cpc_group_4, 'filing_year': row['filing_year']})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(cpc_codes_list)

if cpc_df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Calculate yearly counts and EMA
    yearly_counts = cpc_df.groupby(['cpc_group_code', 'filing_year']).size().reset_index(name='count')
    yearly_counts = yearly_counts.sort_values(by=['cpc_group_code', 'filing_year'])

    ema_results = []
    alpha = 0.1
    for cpc_group in yearly_counts['cpc_group_code'].unique():
        group_data = yearly_counts[yearly_counts['cpc_group_code'] == cpc_group].copy()
        group_data['ema'] = group_data['count'].ewm(alpha=alpha, adjust=False).mean()
        if not group_data.empty:
            best_year_row = group_data.loc[group_data['ema'].idxmax()]
            ema_results.append({'cpc_group_code': cpc_group, 'best_year': int(best_year_row['filing_year']), 'max_ema': best_year_row['ema']})

    ema_df = pd.DataFrame(ema_results)
    ema_df = ema_df.sort_values(by='max_ema', ascending=False)

    result_for_next_step = ema_df.to_dict(orient='records')
    print('__RESULT__:')
    print(json.dumps(result_for_next_step))"""

env_args = {'var_function-call-11468183013790806528': ['publicationinfo'], 'var_function-call-11468183013790806491': ['cpc_definition'], 'var_function-call-15232240169378814865': [], 'var_function-call-14515858273810460582': 'file_storage/function-call-14515858273810460582.json', 'var_function-call-15163413259859991045': 'file_storage/function-call-15163413259859991045.json', 'var_function-call-236773821890115753': [], 'var_function-call-2444223950916495884': 'file_storage/function-call-2444223950916495884.json', 'var_function-call-8910827851189940778': 'file_storage/function-call-8910827851189940778.json', 'var_function-call-13383684003776608126': [], 'var_function-call-18229947996547152276': [], 'var_function-call-13251863267535079290': [], 'var_function-call-12035964178011117782': 'file_storage/function-call-12035964178011117782.json', 'var_function-call-1868845643524759541': 'file_storage/function-call-1868845643524759541.json'}

exec(code, env_args)
