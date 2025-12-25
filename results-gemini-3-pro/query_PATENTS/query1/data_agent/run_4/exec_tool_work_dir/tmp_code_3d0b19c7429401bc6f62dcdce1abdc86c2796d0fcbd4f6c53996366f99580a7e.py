code = """import json
import re

path_cpc = locals()['var_function-call-17682530284056883508']
path_patents = locals()['var_function-call-1425838539260044447']

with open(path_cpc, 'r') as f:
    cpc_defs = json.load(f)
level_5_symbols = set(item['symbol'] for item in cpc_defs if 'symbol' in item)

with open(path_patents, 'r') as f:
    patents = json.load(f)

match_mode = 'subclass' # Based on previous finding

counts = {}
year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')

debug_years = set()

for p in patents:
    f_date = p.get('filing_date', '')
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    year = int(matches[-1])
    debug_years.add(year)
    
    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        if not code:
            continue
        
        target_code = code[:4] if len(code) >= 4 else None
        
        if target_code and target_code in level_5_symbols:
            if target_code not in counts:
                counts[target_code] = {}
            counts[target_code][year] = counts[target_code].get(year, 0) + 1

info = {}
info['min_year'] = min(debug_years) if debug_years else None
info['max_year'] = max(debug_years) if debug_years else None
info['matched_codes_count'] = len(counts)

# Top 5 codes
sorted_codes = sorted(counts.items(), key=lambda x: sum(x[1].values()), reverse=True)[:5]
info['top_codes'] = []

alpha = 0.2
for code, year_counts in sorted_codes:
    years = sorted(year_counts.keys())
    # EMA
    min_y = years[0]
    limit_y = max(years[-1], 2022)
    ema = 0
    first = True
    best_ema = -1
    best_y = -1
    hist = []
    
    for y in range(min_y, limit_y + 1):
        c = year_counts.get(y, 0)
        if first:
            ema = c
            first = False
        else:
            ema = alpha * c + (1 - alpha) * ema
        hist.append((y, c, "{:.2f}".format(ema)))
        if ema > best_ema:
            best_ema = ema
            best_y = y
            
    info['top_codes'].append({
        'code': code,
        'history': hist,
        'best_year': best_y
    })

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_function-call-17682530284056883508': 'file_storage/function-call-17682530284056883508.json', 'var_function-call-1425838539260044447': 'file_storage/function-call-1425838539260044447.json', 'var_function-call-767001268371460585': [], 'var_function-call-2505620898448165995': 'DEBUG_DONE', 'var_function-call-4017213322786989118': {'sample_level_5': ['G01B', 'G21C', 'E02F', 'F41H', 'A22C', 'A24B', 'H99Z', 'A61Q', 'C21B', 'D05B'], 'match_mode': 'subclass', 'dates_preview': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'codes_preview': [], 'total_matches': 0, 'unique_matched_codes': 0}, 'var_function-call-18026136881528221405': {'cpc_raw_type': "<class 'str'>", 'cpc_raw_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n  ', 'cpc_parsed_type': "<class 'list'>", 'cpc_parsed_len': 38, 'first_item': {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}}, 'var_function-call-13507219659217068897': []}

exec(code, env_args)
