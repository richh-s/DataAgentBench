code = """import json
import re

path_level5 = locals()['var_function-call-8552121385304934685']
path_patents = locals()['var_function-call-12122079112080214207']

with open(path_level5, 'r') as f:
    level5_list = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_list)

with open(path_patents, 'r') as f:
    patent_data = json.load(f)

# Simplified regex
year_pattern = re.compile(r'(19|20)\d{2}')

counts = {} # {symbol: {year: count}}

for row in patent_data:
    f_date = row.get('filing_date')
    if not f_date:
        continue
    
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    cpc_str = row.get('cpc')
    if not cpc_str:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    current_patent_symbols = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_symbols:
                current_patent_symbols.add(prefix)
            
    for s in current_patent_symbols:
        if s not in counts:
            counts[s] = {}
        counts[s][year] = counts[s].get(year, 0) + 1

# Calculate EMA and find best year
alpha = 0.2
selected_symbols = []

for sym, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
        
    start_year = years[0]
    end_year = years[-1]
    
    # We must ensure we cover up to 2022 if possible to check if it's the peak.
    # If the data stops before 2022, we can't say 2022 is the best year.
    if end_year < 2022:
        continue
        
    ema = 0
    max_ema = -1
    best_year = -1
    
    current_ema = None
    
    # Iterate from start_year to end_year.
    # Should we iterate to 2022 explicitly if end_year > 2022? Yes.
    # If end_year == 2022, we stop there.
    
    for y in range(start_year, end_year + 1):
        c = year_counts.get(y, 0)
        if current_ema is None:
            current_ema = c
        else:
            current_ema = alpha * c + (1 - alpha) * current_ema
        
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
    if best_year == 2022:
        selected_symbols.append(sym)

print("__RESULT__:")
print(json.dumps(selected_symbols))"""

env_args = {'var_function-call-1397089811542180174': ['publicationinfo'], 'var_function-call-1397089811542180177': ['cpc_definition'], 'var_function-call-3017323399836205737': 'file_storage/function-call-3017323399836205737.json', 'var_function-call-3017323399836208786': [{'count': '677'}], 'var_function-call-16375230660246420135': [{'count(*)': '277813'}], 'var_function-call-8552121385304934685': 'file_storage/function-call-8552121385304934685.json', 'var_function-call-12122079112080214207': 'file_storage/function-call-12122079112080214207.json', 'var_function-call-16341698527960964951': [], 'var_function-call-14015928151608336976': {'min_year': None, 'max_year': None, 'total_patents': 277813, 'patents_with_matches': 0, 'sample_keys': [], 'sample_data': {}}, 'var_function-call-3065730860646420937': [{'index': 0, 'filing_date': 'dated 5th March 2019', 'match': None, 'type': "<class 'str'>"}, {'index': 1, 'filing_date': 'March the 18th, 2019', 'match': None, 'type': "<class 'str'>"}, {'index': 2, 'filing_date': '29th March 2019', 'match': None, 'type': "<class 'str'>"}, {'index': 3, 'filing_date': 'on March 29th, 2019', 'match': None, 'type': "<class 'str'>"}, {'index': 4, 'filing_date': '2nd April 2019', 'match': None, 'type': "<class 'str'>"}, {'index': 5, 'filing_date': 'on April 8th, 2019', 'match': None, 'type': "<class 'str'>"}, {'index': 6, 'filing_date': '15th April 2019', 'match': None, 'type': "<class 'str'>"}, {'index': 7, 'filing_date': 'April 19th, 2019', 'match': None, 'type': "<class 'str'>"}, {'index': 8, 'filing_date': '2019, April 24th', 'match': None, 'type': "<class 'str'>"}, {'index': 9, 'filing_date': 'April 26th, 2019', 'match': None, 'type': "<class 'str'>"}], 'var_function-call-11388689994011465635': {'C01B_in_level5': True, 'match1': '2019', 'match2': '2019'}}

exec(code, env_args)
