code = """import json
import re

path_cpc = locals()['var_function-call-17682530284056883508']
path_patents = locals()['var_function-call-1425838539260044447']

debug_info = {}

with open(path_cpc, 'r') as f:
    cpc_defs = json.load(f)

level_5_symbols = set()
for item in cpc_defs:
    if 'symbol' in item:
        level_5_symbols.add(item['symbol'])

debug_info['sample_level_5'] = list(level_5_symbols)[:10]

with open(path_patents, 'r') as f:
    patents = json.load(f)

debug_info['match_mode'] = 'subclass' if all(len(s) == 4 for s in debug_info['sample_level_5']) else 'exact'

counts = {}
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

debug_dates = []
debug_codes = []
matches_count = 0

for i, p in enumerate(patents):
    f_date = p.get('filing_date', '')
    if i < 5:
        debug_dates.append(f_date)
        
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
        if i < 5:
            debug_codes.append(code)
            
        target_code = None
        if debug_info['match_mode'] == 'subclass':
            if len(code) >= 4:
                target_code = code[:4]
        else:
            target_code = code
            
        if target_code in level_5_symbols:
            matches_count += 1
            if target_code not in counts:
                counts[target_code] = {}
            counts[target_code][year] = counts[target_code].get(year, 0) + 1

debug_info['dates_preview'] = debug_dates
debug_info['codes_preview'] = debug_codes
debug_info['total_matches'] = matches_count
debug_info['unique_matched_codes'] = len(counts)

if counts:
    sample_code = list(counts.keys())[0]
    debug_info['sample_code'] = sample_code
    debug_info['sample_counts'] = counts[sample_code]
    
    alpha = 0.2
    years = sorted(counts[sample_code].keys())
    min_year = years[0]
    limit_year = max(years[-1], 2022)
    ema = 0
    first = True
    best_ema = -1
    best_year = -1
    history = []
    
    for y in range(min_year, limit_year + 1):
        count = counts[sample_code].get(y, 0)
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        history.append({'year': y, 'count': count, 'ema': ema})
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    debug_info['sample_history'] = history
    debug_info['sample_best_year'] = best_year

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-17682530284056883508': 'file_storage/function-call-17682530284056883508.json', 'var_function-call-1425838539260044447': 'file_storage/function-call-1425838539260044447.json', 'var_function-call-767001268371460585': [], 'var_function-call-2505620898448165995': 'DEBUG_DONE'}

exec(code, env_args)
