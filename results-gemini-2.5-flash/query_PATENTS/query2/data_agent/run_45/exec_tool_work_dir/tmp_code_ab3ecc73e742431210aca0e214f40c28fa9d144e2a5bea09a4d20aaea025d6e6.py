code = """import json
import pandas as pd

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

all_patents = pd.read_json(locals()['var_function-call-159961854333049397'])

all_patents['grant_date_parsed'] = all_patents['grant_date'].apply(parse_date)
all_patents['filing_date_parsed'] = all_patents['filing_date'].apply(parse_date)

# Filter for German patents and second half of 2019
german_patents = all_patents[all_patents['Patents_info'].str.contains('country_code: DE', na=False)].copy()
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
                cpc_data.append({
                    'cpc_group': cpc_item['code'][:4],
                    'filing_year': row['filing_date_parsed'].year
                })
    except (json.JSONDecodeError, TypeError):
        continue

# Check if cpc_data is empty
if not cpc_data:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    cpc_df = pd.DataFrame(cpc_data)
    cpc_df['filing_year'] = cpc_df['filing_year'].astype(int)

    # Calculate yearly filings for each CPC group
    yearly_filings = cpc_df.groupby(['cpc_group', 'filing_year']).size().unstack(fill_value=0)

    # Calculate EMA
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

    # Find the best year for each CPC group
    best_ema_per_cpc = {}
    for cpc_group, ema_values in ema_result.items():
        if ema_values:
            best_year_entry = max(ema_values, key=lambda x: x['ema'])
            best_ema_per_cpc[cpc_group] = {
                'best_year': best_year_entry['year'],
                'max_ema': best_year_entry['ema']
            }

    # Sort by max_ema and get the top CPC groups
    sorted_cpc_groups = sorted(best_ema_per_cpc.items(), key=lambda item: item[1]['max_ema'], reverse=True)

    # Extract the CPC group codes at level 4 for querying definition database
    top_cpc_codes_level4 = [cpc_group for cpc_group, _ in sorted_cpc_groups]

    print("__RESULT__:")
    print(json.dumps(top_cpc_codes_level4))"""

env_args = {'var_function-call-13781591671737650296': [], 'var_function-call-159961854333049397': 'file_storage/function-call-159961854333049397.json'}

exec(code, env_args)
