code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-12790738948294253475'], 'r') as f:
    level5_data = json.load(f)
valid_level5_codes = set(item['symbol'] for item in level5_data)

with open(locals()['var_function-call-2189748292734170066'], 'r') as f:
    pub_data = json.load(f)

counts = {} # year -> code -> count

for record in pub_data:
    date_str = record.get('filing_date', '')
    if not date_str:
        continue
    
    # Find all digit sequences
    digit_sequences = re.findall(r'\d+', date_str)
    year = None
    for seq in digit_sequences:
        if len(seq) == 4 and (seq.startswith('19') or seq.startswith('20')):
            year = int(seq)
            break # Assume first 4-digit year is the one
            
    if year is None:
        continue

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

if df.empty:
    print("__RESULT__:")
    print("[]")
else:
    df_pivot = df.pivot(index='Year', columns='Code', values='Count').fillna(0).sort_index()
    
    min_year = df_pivot.index.min()
    max_year = df_pivot.index.max()
    full_range = range(min_year, max_year + 1)
    df_pivot = df_pivot.reindex(full_range, fill_value=0)
    
    ema_df = df_pivot.ewm(alpha=0.2, adjust=False).mean()
    best_years = ema_df.idxmax()
    
    target_codes = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_codes))"""

env_args = {'var_function-call-10820619102234232879': 'file_storage/function-call-10820619102234232879.json', 'var_function-call-13188904574193367056': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-13958987405040638588': [{'level': '2.0', 'sample_symbol': 'A'}, {'level': '4.0', 'sample_symbol': 'A01'}, {'level': '5.0', 'sample_symbol': 'A01B'}, {'level': '7.0', 'sample_symbol': 'A01B1/00'}, {'level': '8.0', 'sample_symbol': 'A01B1/02'}, {'level': '9.0', 'sample_symbol': 'A01B1/022'}, {'level': '10.0', 'sample_symbol': 'A01B1/225'}, {'level': '11.0', 'sample_symbol': 'A01B3/421'}, {'level': '12.0', 'sample_symbol': 'A01B3/4215'}, {'level': '13.0', 'sample_symbol': 'A01D2034/6843'}, {'level': '14.0', 'sample_symbol': 'A01D2034/6825'}, {'level': '15.0', 'sample_symbol': 'A47J31/4446'}, {'level': '16.0', 'sample_symbol': 'A61B17/7028'}, {'level': '17.0', 'sample_symbol': 'A61K47/6823'}, {'level': '18.0', 'sample_symbol': 'G01N2333/96444'}, {'level': '19.0', 'sample_symbol': 'H01L21/32137'}], 'var_function-call-12790738948294253475': 'file_storage/function-call-12790738948294253475.json', 'var_function-call-17223264580135065158': [{'count(*)': '277813'}], 'var_function-call-2189748292734170066': 'file_storage/function-call-2189748292734170066.json', 'var_function-call-10255768070835077748': [], 'var_function-call-955277057603577860': {'status': 'DataFrame is empty'}, 'var_function-call-2397787288433701033': ['Num valid codes: 677', 'C01B is valid', {'date_str': 'dated 5th March 2019', 'matches': [], 'cpc_str_len': 3547, 'cpc_parsed_len': 38, 'first_code': 'C01B33/00', 'subclass': 'C01B', 'is_valid': True}, {'date_str': 'March the 18th, 2019', 'matches': [], 'cpc_str_len': 2078, 'cpc_parsed_len': 22, 'first_code': 'F16H47/04', 'subclass': 'F16H', 'is_valid': True}, {'date_str': '29th March 2019', 'matches': [], 'cpc_str_len': 6267, 'cpc_parsed_len': 67, 'first_code': 'B29C70/48', 'subclass': 'B29C', 'is_valid': True}, {'date_str': 'on March 29th, 2019', 'matches': [], 'cpc_str_len': 1905, 'cpc_parsed_len': 20, 'first_code': 'A61K48/0066', 'subclass': 'A61K', 'is_valid': True}, {'date_str': '2nd April 2019', 'matches': [], 'cpc_str_len': 1015, 'cpc_parsed_len': 11, 'first_code': 'H01H9/042', 'subclass': 'H01H', 'is_valid': True}]}

exec(code, env_args)
