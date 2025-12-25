code = """import json
import re

l5_path = locals()['var_function-call-7207860585803115625']
patents_path = locals()['var_function-call-5530323500134500439']

with open(l5_path, 'r') as f:
    l5_data = json.load(f)
l5_symbols = set(item['symbol'] for item in l5_data if 'symbol' in item)

with open(patents_path, 'r') as f:
    patents = json.load(f)

counts = {} # {symbol: {year: count}}

for p in patents:
    d_str = p.get('filing_date', '')
    match = re.search(r'(19|20)\d{2}', str(d_str))
    if match:
        year = int(match.group(0))
    else:
        continue
        
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    if not isinstance(cpc_list, list):
        continue
        
    patent_l5s = set()
    for item in cpc_list:
        code = item.get('code', '')
        if code and len(code) >= 4:
            prefix = code[:4]
            if prefix in l5_symbols:
                patent_l5s.add(prefix)
    
    for sym in patent_l5s:
        if sym not in counts:
            counts[sym] = {}
        counts[sym][year] = counts[sym].get(year, 0) + 1

alpha = 0.2
candidates = []

for sym, year_counts in counts.items():
    if not year_counts:
        continue
    
    min_year = min(year_counts.keys())
    max_year = max(year_counts.keys())
    
    curr_ema = 0
    first = True
    
    max_ema = -1.0
    best_year = -1
    
    for y in range(min_year, max_year + 1):
        val = year_counts.get(y, 0)
        if first:
            curr_ema = val
            first = False
        else:
            curr_ema = alpha * val + (1 - alpha) * curr_ema
        
        if curr_ema > max_ema:
            max_ema = curr_ema
            best_year = y
            
    if best_year == 2022:
        candidates.append(sym)

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-16354257400330351795': 'file_storage/function-call-16354257400330351795.json', 'var_function-call-16354257400330353054': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-10560939620404889531': [{'symbol': 'H01M', 'level': '5.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'H01M10/0565', 'level': '11.0'}], 'var_function-call-16184128629487448997': [{'len': '4', 'cnt': '677'}], 'var_function-call-4973736629774637364': [{'cnt': '277813'}], 'var_function-call-7207860585803115625': 'file_storage/function-call-7207860585803115625.json', 'var_function-call-5530323500134500439': 'file_storage/function-call-5530323500134500439.json', 'var_function-call-6282301310973396861': [], 'var_function-call-3212865062370055516': {'total': 277813, 'valid_years': 0, 'valid_cpc': 0, 'matched_l5': 0, 'year_min': None, 'year_max': None, 'top_years': {}}, 'var_function-call-8762404416262283466': 'file_storage/function-call-8762404416262283466.json', 'var_function-call-12606317811182743240': [{'raw_date': 'dated 5th March 2019', 'type': "<class 'str'>", 'match': 'No Match'}, {'raw_date': 'March the 18th, 2019', 'type': "<class 'str'>", 'match': 'No Match'}, {'raw_date': '29th March 2019', 'type': "<class 'str'>", 'match': 'No Match'}, {'raw_date': 'on March 29th, 2019', 'type': "<class 'str'>", 'match': 'No Match'}, {'raw_date': '2nd April 2019', 'type': "<class 'str'>", 'match': 'No Match'}], 'var_function-call-13650205791277643486': [{'raw_date': 'dated 5th March 2019', 'year_found': '2019', 'cpc_raw_len': 3547, 'cpc_parsed_type': "<class 'list'>", 'cpc_parsed_len': 38, 'cpc_error': None, 'first_code': 'C01B33/00'}, {'raw_date': 'March the 18th, 2019', 'year_found': '2019', 'cpc_raw_len': 2078, 'cpc_parsed_type': "<class 'list'>", 'cpc_parsed_len': 22, 'cpc_error': None, 'first_code': 'F16H47/04'}]}

exec(code, env_args)
