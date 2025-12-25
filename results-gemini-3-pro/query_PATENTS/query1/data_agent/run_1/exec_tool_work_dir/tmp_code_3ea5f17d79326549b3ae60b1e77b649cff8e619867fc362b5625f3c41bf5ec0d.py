code = """import json
import re

cpc_defs_path = locals()['var_function-call-8775067390743093543']
patents_path = locals()['var_function-call-17651004867622027777']

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

print(f"DEBUG: Found {len(level_5_codes)} Level 5 CPC codes.")

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

print(f"DEBUG: Found {len(counts)} Level 5 codes with filings.")
if years_found:
    print(f"DEBUG: Year range in data: {min(years_found)} to {max(years_found)}")

# Inspect one code
if counts:
    sample_code = list(counts.keys())[0]
    print(f"DEBUG: Counts for {sample_code}: {counts[sample_code]}")
    
    # Calculate EMA for this sample
    alpha = 0.2
    years = sorted(counts[sample_code].keys())
    s_y = years[0]
    ema = counts[sample_code][s_y]
    best_ema = ema
    best_year = s_y
    print(f"DEBUG: Start Year: {s_y}, Start EMA: {ema}")
    
    limit = max(max(years_found), 2022)
    for y in range(s_y + 1, limit + 1):
        val = counts[sample_code].get(y, 0)
        ema = val * 0.2 + ema * 0.8
        if ema > best_ema:
            best_ema = ema
            best_year = y
    print(f"DEBUG: Best Year for {sample_code}: {best_year} (EMA: {best_ema})")

print("__RESULT__:")
print(json.dumps("DONE"))"""

env_args = {'var_function-call-6641923460859800772': 'file_storage/function-call-6641923460859800772.json', 'var_function-call-6641923460859799993': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-4289607868665699138': [{'count': '260808'}], 'var_function-call-4289607868665698023': [{'count(*)': '277813'}], 'var_function-call-8775067390743093543': 'file_storage/function-call-8775067390743093543.json', 'var_function-call-17651004867622027777': 'file_storage/function-call-17651004867622027777.json', 'var_function-call-5059798945412610512': [], 'var_function-call-15245929960655701249': []}

exec(code, env_args)
