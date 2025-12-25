code = """import json
import re

cpc_defs_path = locals()['var_function-call-8775067390743093543']
patents_path = locals()['var_function-call-17651004867622027777']

debug_info = {}

with open(cpc_defs_path, 'r') as f:
    cpc_defs = json.load(f)

level_5_codes = set()
for item in cpc_defs:
    try:
        lvl = float(item.get('level', 0))
        if int(lvl) == 5:
            level_5_codes.add(item['symbol'])
    except:
        pass

debug_info['level_5_count'] = len(level_5_codes)

with open(patents_path, 'r') as f:
    patents = json.load(f)

counts = {}
year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')
years_found = set()

for p in patents:
    f_date = p.get('filing_date', '')
    match = year_pattern.search(f_date)
    if not match: continue
    year = int(match.group(1))
    years_found.add(year)
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    unique_codes = set()
    for c in cpc_list:
        code = c.get('code')
        if code in level_5_codes:
            unique_codes.add(code)
            
    for code in unique_codes:
        if code not in counts:
            counts[code] = {}
        counts[code][year] = counts[code].get(year, 0) + 1

debug_info['codes_with_filings'] = len(counts)
if years_found:
    debug_info['min_year'] = min(years_found)
    debug_info['max_year'] = max(years_found)

# Sample check
if counts:
    sample_code = list(counts.keys())[0]
    debug_info['sample_code'] = sample_code
    debug_info['sample_counts'] = counts[sample_code]
    
    alpha = 0.2
    years = sorted(counts[sample_code].keys())
    s_y = years[0]
    ema = counts[sample_code][s_y]
    best_ema = ema
    best_year = s_y
    
    limit = 2022 # Force check up to 2022
    for y in range(s_y + 1, limit + 1):
        val = counts[sample_code].get(y, 0)
        ema = val * alpha + ema * (1 - alpha)
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    debug_info['sample_best_year'] = best_year
    debug_info['sample_best_ema'] = best_ema

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-6641923460859800772': 'file_storage/function-call-6641923460859800772.json', 'var_function-call-6641923460859799993': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-4289607868665699138': [{'count': '260808'}], 'var_function-call-4289607868665698023': [{'count(*)': '277813'}], 'var_function-call-8775067390743093543': 'file_storage/function-call-8775067390743093543.json', 'var_function-call-17651004867622027777': 'file_storage/function-call-17651004867622027777.json', 'var_function-call-5059798945412610512': [], 'var_function-call-15245929960655701249': [], 'var_function-call-11939134990751395154': 'DONE'}

exec(code, env_args)
