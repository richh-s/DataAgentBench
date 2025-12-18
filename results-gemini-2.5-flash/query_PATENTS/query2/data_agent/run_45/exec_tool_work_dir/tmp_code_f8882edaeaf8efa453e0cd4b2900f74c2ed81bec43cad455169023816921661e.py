code = """import json
import pandas as pd
import re

def parse_date(date_str):
    if not isinstance(date_str, str):
        return None
    try:
        fmts = [
            '%Y, %B %dth',
            '%Y, %B %d',
            '%dth %b %Y',
            '%b %dth, %Y',
            '%Y-%m-%d',
            '%B %d, %Y',
            '%d %b %Y',
            '%Y',
            '%d %B %Y'
        ]
        for fmt in fmts:
            try:
                return pd.to_datetime(date_str, format=fmt)
            except ValueError:
                continue
        return pd.to_datetime(date_str, errors='coerce')
    except:
        return None

all_patents = pd.read_json(locals()['var_function-call-656837194378036393'])

all_patents['grant_date_parsed'] = all_patents['grant_date'].apply(parse_date)
all_patents['filing_date_parsed'] = all_patents['filing_date'].apply(parse_date)

# Filter for German patents and second half of 2019
german_patents = all_patents[
    all_patents['Patents_info'].apply(lambda x: bool(re.search(r'from DE', x)) if isinstance(x, str) else False)
].copy()
german_patents = german_patents[
    (german_patents['grant_date_parsed'].dt.year == 2019) & 
    (german_patents['grant_date_parsed'].dt.month >= 7)
].copy()

cpc_data = []
for _, row in german_patents.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            if 'code' in cpc_item and row['filing_date_parsed'] is not None:
                if len(cpc_item['code']) >= 4:
                    cpc_data.append({
                        'cpc_group': cpc_item['code'][:4],
                        'filing_year': row['filing_date_parsed'].year
                    })
    except (json.JSONDecodeError, TypeError):
        continue

if not cpc_data:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    cpc_df = pd.DataFrame(cpc_data)
    cpc_df['filing_year'] = cpc_df['filing_year'].astype(int)

    yearly_filings = cpc_df.groupby(['cpc_group', 'filing_year']).size().unstack(fill_value=0).fillna(0)

    smoothing_factor = 0.1
    ema_result = {}
    for cpc_group in yearly_filings.index:
        ema_values = []
        current_ema = 0
        for year in sorted(yearly_filings.columns):
            current_filings = yearly_filings.loc[cpc_group, year]
            current_ema = (current_filings * smoothing_factor) + (current_ema * (1 - smoothing_factor))
            ema_values.append({'year': year, 'ema': current_ema})
        ema_result[cpc_group] = ema_values

    best_ema_per_cpc = {}
    for cpc_group, ema_values in ema_result.items():
        if ema_values:
            best_year_entry = max(ema_values, key=lambda x: x['ema'])
            best_ema_per_cpc[cpc_group] = {
                'best_year': best_year_entry['year'],
                'max_ema': best_year_entry['ema']
            }

    sorted_cpc_groups = sorted(best_ema_per_cpc.items(), key=lambda item: item[1]['max_ema'], reverse=True)

    cpc_groups_for_query = []
    for cpc_group, details in sorted_cpc_groups:
        cpc_groups_for_query.append({
            'cpc_group': cpc_group,
            'best_year': details['best_year'],
            'max_ema': details['max_ema']
        })

    print("__RESULT__:")
    print(json.dumps(cpc_groups_for_query))"""

env_args = {'var_function-call-13781591671737650296': [], 'var_function-call-159961854333049397': 'file_storage/function-call-159961854333049397.json', 'var_function-call-14805747375982610187': [], 'var_function-call-10929909419482869292': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}], 'var_function-call-15674998834885795494': [], 'var_function-call-3203908515550012934': 'file_storage/function-call-3203908515550012934.json', 'var_function-call-600729039729646520': [], 'var_function-call-11435041568651700914': 'file_storage/function-call-11435041568651700914.json', 'var_function-call-8517005424988983734': [], 'var_function-call-656837194378036393': 'file_storage/function-call-656837194378036393.json', 'var_function-call-7737786209067804494': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H03L', 'best_year': 2015, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}, {'cpc_group': 'G01M', 'best_year': 2018, 'max_ema': 0.4}, {'cpc_group': 'F01D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'F05D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'H04L', 'best_year': 2015, 'max_ema': 0.2}, {'cpc_group': 'F04D', 'best_year': 2018, 'max_ema': 0.1}, {'cpc_group': 'F16F', 'best_year': 2018, 'max_ema': 0.1}], 'var_function-call-541724979457509416': ['A61F', 'H02J', 'H03L', 'A43B', 'G01M', 'F01D', 'F05D', 'H04L', 'F04D', 'F16F'], 'var_function-call-12857969857747079952': [], 'var_function-call-6666716879358711252': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H03L', 'best_year': 2015, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}, {'cpc_group': 'G01M', 'best_year': 2018, 'max_ema': 0.4}, {'cpc_group': 'F01D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'F05D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'H04L', 'best_year': 2015, 'max_ema': 0.2}, {'cpc_group': 'F04D', 'best_year': 2018, 'max_ema': 0.1}, {'cpc_group': 'F16F', 'best_year': 2018, 'max_ema': 0.1}], 'var_function-call-10749211325850591547': ['A61F', 'H02J', 'H03L', 'A43B', 'G01M', 'F01D', 'F05D', 'H04L', 'F04D', 'F16F'], 'var_function-call-10114930463046135881': 'file_storage/function-call-10114930463046135881.json', 'var_function-call-17116891878385305191': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H03L', 'best_year': 2015, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}, {'cpc_group': 'G01M', 'best_year': 2018, 'max_ema': 0.4}, {'cpc_group': 'F01D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'F05D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'H04L', 'best_year': 2015, 'max_ema': 0.2}, {'cpc_group': 'F04D', 'best_year': 2018, 'max_ema': 0.1}, {'cpc_group': 'F16F', 'best_year': 2018, 'max_ema': 0.1}], 'var_function-call-4837316381396745111': 'file_storage/function-call-4837316381396745111.json', 'var_function-call-1317980778041560380': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H03L', 'best_year': 2015, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}, {'cpc_group': 'G01M', 'best_year': 2018, 'max_ema': 0.4}, {'cpc_group': 'F01D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'F05D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'H04L', 'best_year': 2015, 'max_ema': 0.2}, {'cpc_group': 'F04D', 'best_year': 2018, 'max_ema': 0.1}, {'cpc_group': 'F16F', 'best_year': 2018, 'max_ema': 0.1}], 'var_function-call-6169857417003538237': 'file_storage/function-call-6169857417003538237.json', 'var_function-call-18195607739268006753': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H03L', 'best_year': 2015, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}, {'cpc_group': 'G01M', 'best_year': 2018, 'max_ema': 0.4}, {'cpc_group': 'F01D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'F05D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'H04L', 'best_year': 2015, 'max_ema': 0.2}, {'cpc_group': 'F04D', 'best_year': 2018, 'max_ema': 0.1}, {'cpc_group': 'F16F', 'best_year': 2018, 'max_ema': 0.1}], 'var_function-call-13937268158884103738': 'file_storage/function-call-13937268158884103738.json', 'var_function-call-4415129512760359865': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H03L', 'best_year': 2015, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}, {'cpc_group': 'G01M', 'best_year': 2018, 'max_ema': 0.4}, {'cpc_group': 'F01D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'F05D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'H04L', 'best_year': 2015, 'max_ema': 0.2}, {'cpc_group': 'F04D', 'best_year': 2018, 'max_ema': 0.1}, {'cpc_group': 'F16F', 'best_year': 2018, 'max_ema': 0.1}]}

exec(code, env_args)
