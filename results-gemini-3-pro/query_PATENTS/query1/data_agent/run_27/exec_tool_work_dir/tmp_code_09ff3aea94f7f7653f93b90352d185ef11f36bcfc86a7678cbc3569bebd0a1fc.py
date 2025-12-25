code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-12790738948294253475'], 'r') as f:
    level5_data = json.load(f)
valid_level5_codes = set(item['symbol'] for item in level5_data)

with open(locals()['var_function-call-2189748292734170066'], 'r') as f:
    pub_data = json.load(f)

counts = {}
year_pattern = re.compile(r'\b(?:19|20)\d{2}\b')

for record in pub_data:
    date_str = record.get('filing_date', '')
    if not date_str:
        continue
    full_matches = year_pattern.findall(date_str)
    if not full_matches:
        continue
    year = int(full_matches[0])

    cpc_str = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in valid_level5_codes:
                patent_codes.add(subclass)
    
    for code in patent_codes:
        if year not in counts:
            counts[year] = {}
        counts[year][code] = counts[year].get(code, 0) + 1

data_list = []
for year, code_counts in counts.items():
    for code, count in code_counts.items():
        data_list.append({'Year': year, 'Code': code, 'Count': count})

df = pd.DataFrame(data_list)
debug_info = {}

if df.empty:
    debug_info['status'] = "DataFrame is empty"
else:
    df_pivot = df.pivot(index='Year', columns='Code', values='Count').fillna(0).sort_index()
    min_year = df_pivot.index.min()
    max_year = df_pivot.index.max()
    debug_info['year_range'] = [min_year, max_year]
    
    full_range = range(min_year, max_year + 1)
    df_pivot = df_pivot.reindex(full_range, fill_value=0)
    
    ema_df = df_pivot.ewm(alpha=0.2, adjust=False).mean()
    best_years = ema_df.idxmax()
    
    # Check counts of best years
    best_year_counts = best_years.value_counts().to_dict()
    # Convert keys to int (numpy int64 is not json serializable)
    best_year_counts = {int(k): v for k, v in best_year_counts.items()}
    debug_info['best_year_distribution'] = best_year_counts
    
    # Check if 2022 is in the columns/index
    debug_info['has_2022'] = 2022 in df_pivot.index

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-10820619102234232879': 'file_storage/function-call-10820619102234232879.json', 'var_function-call-13188904574193367056': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-13958987405040638588': [{'level': '2.0', 'sample_symbol': 'A'}, {'level': '4.0', 'sample_symbol': 'A01'}, {'level': '5.0', 'sample_symbol': 'A01B'}, {'level': '7.0', 'sample_symbol': 'A01B1/00'}, {'level': '8.0', 'sample_symbol': 'A01B1/02'}, {'level': '9.0', 'sample_symbol': 'A01B1/022'}, {'level': '10.0', 'sample_symbol': 'A01B1/225'}, {'level': '11.0', 'sample_symbol': 'A01B3/421'}, {'level': '12.0', 'sample_symbol': 'A01B3/4215'}, {'level': '13.0', 'sample_symbol': 'A01D2034/6843'}, {'level': '14.0', 'sample_symbol': 'A01D2034/6825'}, {'level': '15.0', 'sample_symbol': 'A47J31/4446'}, {'level': '16.0', 'sample_symbol': 'A61B17/7028'}, {'level': '17.0', 'sample_symbol': 'A61K47/6823'}, {'level': '18.0', 'sample_symbol': 'G01N2333/96444'}, {'level': '19.0', 'sample_symbol': 'H01L21/32137'}], 'var_function-call-12790738948294253475': 'file_storage/function-call-12790738948294253475.json', 'var_function-call-17223264580135065158': [{'count(*)': '277813'}], 'var_function-call-2189748292734170066': 'file_storage/function-call-2189748292734170066.json', 'var_function-call-10255768070835077748': []}

exec(code, env_args)
