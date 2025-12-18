code = """import pandas as pd
import json
import re

df = pd.read_json(locals()['var_function-call-8910827851189940778'])

# Filter for patents granted in the second half of 2019 in Germany
def parse_grant_date_and_country(row):
    grant_date_str = row['grant_date'].lower()
    country_info = row['Patents_info']

    # Check for second half of 2019
    is_2019_second_half = False
    if '2019' in grant_date_str:
        if any(month in grant_date_str for month in ['jul', 'aug', 'sep', 'oct', 'nov', 'dec']):
            is_2019_second_half = True

    # Check for Germany
    is_germany = 'country_code_DE' in country_info or '(no. DE-' in country_info or 'from DE' in country_info

    return is_2019_second_half and is_germany

df['is_target'] = df.apply(parse_grant_date_and_country, axis=1)
df_filtered = df[df['is_target'] == True].copy()

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
cpc_codes = []
for index, row in df_filtered.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            if len(code) >= 4:
                cpc_group_4 = code[:4]
                cpc_codes.append({'cpc_group_code': cpc_group_4, 'filing_year': row['filing_year'], 'title_localized': row['title_localized']})
    except json.JSONDecodeError:
        continue # Skip if cpc field is not valid JSON

cpc_df = pd.DataFrame(cpc_codes)

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

    # Sort by EMA in descending order
    ema_df = ema_df.sort_values(by='max_ema', ascending=False)

    # Get the original title for each CPC group from the filtered DataFrame
    # This assumes that the title_localized for a given cpc_group_code is consistent
    # We will pick one title for each unique cpc_group_code from the df_filtered.
    cpc_titles = {}
    for index, row in df_filtered.iterrows():
        try:
            cpc_list = json.loads(row['cpc'])
            for cpc_item in cpc_list:
                code = cpc_item['code']
                if len(code) >= 4:
                    cpc_group_4 = code[:4]
                    if cpc_group_4 not in cpc_titles and row['title_localized']:
                        try:
                            titles = json.loads(row['title_localized'])
                            for title_entry in titles:
                                if title_entry['language'] == 'de': # Prioritize German title
                                    cpc_titles[cpc_group_4] = title_entry['text']
                                    break
                            if cpc_group_4 not in cpc_titles and titles: # If no German, take first available
                                cpc_titles[cpc_group_4] = titles[0]['text']
                        except json.JSONDecodeError:
                            cpc_titles[cpc_group_4] = row['title_localized'] # Fallback if not JSON
        except json.JSONDecodeError:
            continue

    # Merge EMA results with titles
    final_results = []
    for index, row in ema_df.iterrows():
        cpc_code = row['cpc_group_code']
        # Try to get the title from the publication database first
        title = cpc_titles.get(cpc_code, "Title not found")
        final_results.append({
            'cpc_group_code': cpc_code,
            'best_year': row['best_year'],
            'exponential_moving_average': row['max_ema'],
            'title_localized': title
        })
    print('__RESULT__:')
    print(pd.DataFrame(final_results).to_json(orient='records'))"""

env_args = {'var_function-call-11468183013790806528': ['publicationinfo'], 'var_function-call-11468183013790806491': ['cpc_definition'], 'var_function-call-15232240169378814865': [], 'var_function-call-14515858273810460582': 'file_storage/function-call-14515858273810460582.json', 'var_function-call-15163413259859991045': 'file_storage/function-call-15163413259859991045.json', 'var_function-call-236773821890115753': [], 'var_function-call-2444223950916495884': 'file_storage/function-call-2444223950916495884.json', 'var_function-call-8910827851189940778': 'file_storage/function-call-8910827851189940778.json'}

exec(code, env_args)
