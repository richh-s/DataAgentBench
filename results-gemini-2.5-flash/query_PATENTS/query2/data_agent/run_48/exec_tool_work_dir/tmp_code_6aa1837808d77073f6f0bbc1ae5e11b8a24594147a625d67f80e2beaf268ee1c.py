code = """import pandas as pd
import json
import re

df = pd.read_json(locals()['var_function-call-6051245445662132030'])

# Filter for patents granted in the second half of 2019 in Germany
def filter_german_2019_second_half(row):
    grant_date_str = row['grant_date'].lower()
    patents_info_str = row['Patents_info']

    # Check for second half of 2019
    is_2019_second_half = False
    if '2019' in grant_date_str:
        if any(month in grant_date_str for month in ['jul', 'aug', 'sep', 'oct', 'nov', 'dec']):
            is_2019_second_half = True

    # Check for Germany by looking for 'DE-' in application number or 'from DE' in Patents_info
    is_germany = False
    if re.search(r'de-\d+', patents_info_str, re.IGNORECASE) or 'from de' in patents_info_str.lower() or 'in de,' in patents_info_str.lower():
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

# Extract CPC codes at level 4 and relevant titles
cpc_data_for_analysis = []
for index, row in df_filtered.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        
        # Extract the title in German if available, otherwise the first available title
        patent_title = ""
        try:
            title_localized_list = json.loads(row['title_localized'])
            for title_entry in title_localized_list:
                if title_entry.get('language') == 'de':
                    patent_title = title_entry.get('text', "")
                    break
            if not patent_title and title_localized_list:
                patent_title = title_localized_list[0].get('text', "")
        except (json.JSONDecodeError, TypeError):
            patent_title = row['title_localized'] # Fallback if not JSON or other error

        for cpc_item in cpc_list:
            code = cpc_item.get('code')
            if code and len(code) >= 4:
                cpc_group_4 = code[:4]
                cpc_data_for_analysis.append({'cpc_group_code': cpc_group_4, 'filing_year': row['filing_year'], 'title_full': patent_title})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(cpc_data_for_analysis)

if cpc_df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Calculate yearly counts and EMA
    yearly_counts = cpc_df.groupby(['cpc_group_code', 'filing_year']).size().reset_index(name='count')
    yearly_counts = yearly_counts.sort_values(by=['cpc_group_code', 'filing_year'])

    ema_results = []
    alpha = 0.1
    
    # Group by cpc_group_code to calculate EMA separately for each group
    for cpc_group in yearly_counts['cpc_group_code'].unique():
        group_data = yearly_counts[yearly_counts['cpc_group_code'] == cpc_group].copy()
        if not group_data.empty and 'count' in group_data.columns:
            group_data['ema'] = group_data['count'].ewm(alpha=alpha, adjust=False).mean()
            best_year_row = group_data.loc[group_data['ema'].idxmax()]
            ema_results.append({
                'cpc_group_code': cpc_group,
                'best_year': int(best_year_row['filing_year']),
                'exponential_moving_average': best_year_row['ema']
            })

    ema_df = pd.DataFrame(ema_results)

    # Get a unique title for each CPC group from the cpc_df
    cpc_to_title = cpc_df.drop_duplicates(subset=['cpc_group_code']).set_index('cpc_group_code')['title_full'].to_dict()

    final_results = []
    for index, row in ema_df.iterrows():
        cpc_code = row['cpc_group_code']
        title = cpc_to_title.get(cpc_code, "Title not found")
        final_results.append({
            'cpc_group_code': cpc_code,
            'title_full': title,
            'best_year': row['best_year'],
            'exponential_moving_average': row['exponential_moving_average']
        })

    final_df = pd.DataFrame(final_results)
    final_df = final_df.sort_values(by='exponential_moving_average', ascending=False)

    print('__RESULT__:')
    print(final_df.to_json(orient='records'))"""

env_args = {'var_function-call-11468183013790806528': ['publicationinfo'], 'var_function-call-11468183013790806491': ['cpc_definition'], 'var_function-call-15232240169378814865': [], 'var_function-call-14515858273810460582': 'file_storage/function-call-14515858273810460582.json', 'var_function-call-15163413259859991045': 'file_storage/function-call-15163413259859991045.json', 'var_function-call-236773821890115753': [], 'var_function-call-2444223950916495884': 'file_storage/function-call-2444223950916495884.json', 'var_function-call-8910827851189940778': 'file_storage/function-call-8910827851189940778.json', 'var_function-call-13383684003776608126': [], 'var_function-call-18229947996547152276': [], 'var_function-call-13251863267535079290': [], 'var_function-call-12035964178011117782': 'file_storage/function-call-12035964178011117782.json', 'var_function-call-1868845643524759541': 'file_storage/function-call-1868845643524759541.json', 'var_function-call-4304302799727589438': [], 'var_function-call-6626801525559584896': 'file_storage/function-call-6626801525559584896.json', 'var_function-call-6981722048677097500': [], 'var_function-call-7326097344363331795': 'file_storage/function-call-7326097344363331795.json', 'var_function-call-10115504908300973529': 'file_storage/function-call-10115504908300973529.json', 'var_function-call-7763245620173558087': 'file_storage/function-call-7763245620173558087.json', 'var_function-call-6051245445662132030': 'file_storage/function-call-6051245445662132030.json', 'var_function-call-1919503483377256526': 'file_storage/function-call-1919503483377256526.json', 'var_function-call-6570687612487073823': 'file_storage/function-call-6570687612487073823.json'}

exec(code, env_args)
