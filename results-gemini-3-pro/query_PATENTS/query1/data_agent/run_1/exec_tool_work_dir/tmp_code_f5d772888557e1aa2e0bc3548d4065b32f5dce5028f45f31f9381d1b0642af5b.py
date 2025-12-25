code = """import json
import re

# Get file paths from locals
cpc_defs_path = locals()['var_function-call-8775067390743093543']
patents_path = locals()['var_function-call-17651004867622027777']

# Load CPC Definitions
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

# Load Patent Filings
with open(patents_path, 'r') as f:
    patents = json.load(f)

counts = {}
year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')

for p in patents:
    f_date = p.get('filing_date', '')
    if not f_date:
        continue
    
    # Extract Year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(1))
    
    cpc_str = p.get('cpc', '[]')
    if not cpc_str: 
        continue
        
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    # Identify unique level 5 codes for this patent
    unique_codes = set()
    for c in cpc_list:
        code = c.get('code')
        if code in level_5_codes:
            unique_codes.add(code)
            
    for code in unique_codes:
        if code not in counts:
            counts[code] = {}
        counts[code][year] = counts[code].get(year, 0) + 1

# Calculate EMA
alpha = 0.2
result_codes = []

# Determine global max year to iterate up to
if counts:
    global_max_year = 0
    for c in counts:
        if counts[c]:
            mx = max(counts[c].keys())
            if mx > global_max_year:
                global_max_year = mx
    
    # If the latest year in data is less than 2022, then 2022 cannot be the best year (EMA would decay).
    # If the latest year is 2022 or more, we can check.
    # The query implies finding "whose best year is 2022", assuming 2022 is within the data or the period of interest.
    # If data ends in 2019, result is empty.
    # Let's assume we calculate up to the max(data_year, 2022).
    # If data ends at 2020, and we extend to 2022 with 0s, EMA decays. Best year won't be 2022.
    # So we strictly follow the data range, but if the user asks for 2022, likely the data contains 2022.
    
    limit_year = max(global_max_year, 2022)
else:
    limit_year = 2022

for code, year_map in counts.items():
    if not year_map:
        continue
        
    years = sorted(year_map.keys())
    start_year = years[0]
    
    ema = year_map[start_year]
    best_ema = ema
    best_year = start_year
    
    # Iterate from start_year + 1 to limit_year
    # We must account for years with 0 filings if they fall within the range start_year to limit_year
    for y in range(start_year + 1, limit_year + 1):
        val = year_map.get(y, 0)
        ema = (val * alpha) + (ema * (1 - alpha))
        
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    if best_year == 2022:
        result_codes.append(code)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-6641923460859800772': 'file_storage/function-call-6641923460859800772.json', 'var_function-call-6641923460859799993': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-4289607868665699138': [{'count': '260808'}], 'var_function-call-4289607868665698023': [{'count(*)': '277813'}], 'var_function-call-8775067390743093543': 'file_storage/function-call-8775067390743093543.json', 'var_function-call-17651004867622027777': 'file_storage/function-call-17651004867622027777.json', 'var_function-call-5059798945412610512': []}

exec(code, env_args)
