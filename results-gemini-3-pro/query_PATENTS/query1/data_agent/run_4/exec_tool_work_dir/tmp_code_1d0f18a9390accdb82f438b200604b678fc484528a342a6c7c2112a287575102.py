code = """import json
import re

path_cpc = locals()['var_function-call-17682530284056883508']
path_patents = locals()['var_function-call-1425838539260044447']

with open(path_cpc, 'r') as f:
    cpc_defs = json.load(f)

level_5_symbols = set()
for item in cpc_defs:
    if 'symbol' in item:
        level_5_symbols.add(item['symbol'])

with open(path_patents, 'r') as f:
    patents = json.load(f)

# Determine matching strategy
sample_symbols = list(level_5_symbols)[:100]
if all(len(s) == 4 for s in sample_symbols):
    match_mode = 'subclass'
else:
    match_mode = 'exact'

counts = {}
year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')

for p in patents:
    f_date = p.get('filing_date', '')
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    year = int(matches[-1])
    
    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        if not code:
            continue
            
        target_code = None
        if match_mode == 'subclass':
            if len(code) >= 4:
                target_code = code[:4]
        else:
            target_code = code
            
        if target_code in level_5_symbols:
            if target_code not in counts:
                counts[target_code] = {}
            counts[target_code][year] = counts[target_code].get(year, 0) + 1

# Calculate EMA
alpha = 0.2
results = []

# Global max year check
all_years = set()
for yc in counts.values():
    all_years.update(yc.keys())

if not all_years:
    limit_year = 2022
else:
    limit_year = max(max(all_years), 2022)

# EMA Calculation
for code, year_counts in counts.items():
    years = sorted(year_counts.keys())
    min_year = years[0]
    
    ema = 0
    first = True
    best_ema = -1.0
    best_year = -1
    
    # We iterate up to limit_year. 
    # If the code has no data in later years, EMA decays.
    # Note: If min_year > limit_year (unlikely), range is empty.
    
    for y in range(min_year, limit_year + 1):
        count = year_counts.get(y, 0)
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    if best_year == 2022:
        results.append(code)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-17682530284056883508': 'file_storage/function-call-17682530284056883508.json', 'var_function-call-1425838539260044447': 'file_storage/function-call-1425838539260044447.json', 'var_function-call-767001268371460585': [], 'var_function-call-2505620898448165995': 'DEBUG_DONE', 'var_function-call-4017213322786989118': {'sample_level_5': ['G01B', 'G21C', 'E02F', 'F41H', 'A22C', 'A24B', 'H99Z', 'A61Q', 'C21B', 'D05B'], 'match_mode': 'subclass', 'dates_preview': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'codes_preview': [], 'total_matches': 0, 'unique_matched_codes': 0}, 'var_function-call-18026136881528221405': {'cpc_raw_type': "<class 'str'>", 'cpc_raw_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n  ', 'cpc_parsed_type': "<class 'list'>", 'cpc_parsed_len': 38, 'first_item': {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}}}

exec(code, env_args)
