code = """import json
import re

# Load level 5 symbols
with open(locals()['var_function_call_2614386764590376133'], 'r') as f:
    cpc_defs = json.load(f)
level5_symbols = set(item['symbol'] for item in cpc_defs)

# Load publication info
with open(locals()['var_function_call_16781152453932160086'], 'r') as f:
    pub_info = json.load(f)

# Structure to hold counts: {cpc_code: {year: count}}
cpc_counts = {}

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for row in pub_info:
    f_date = row.get('filing_date')
    cpc_json = row.get('cpc')
    
    if not f_date or not cpc_json:
        continue
    
    # Parse year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Parse CPC
    try:
        codes_list = json.loads(cpc_json)
    except:
        continue
        
    # Extract unique level 5 codes for this patent
    patent_codes = set()
    for item in codes_list:
        code = item.get('code', '')
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in level5_symbols:
                patent_codes.add(subclass)
    
    # Update counts
    for code in patent_codes:
        if code not in cpc_counts:
            cpc_counts[code] = {}
        cpc_counts[code][year] = cpc_counts[code].get(year, 0) + 1

# Calculate EMA and find best year
result_codes = []
alpha = 0.2

for code, year_counts in cpc_counts.items():
    if not year_counts:
        continue
        
    years = sorted(year_counts.keys())
    min_year = years[0]
    max_year = years[-1]
    
    max_ema = -1.0
    best_year = -1
    
    # Initialize with first year count
    prev_ema = float(year_counts[min_year])
    
    # Check first year
    if prev_ema > max_ema:
        max_ema = prev_ema
        best_year = min_year
        
    # Iterate subsequent years
    for y in range(min_year + 1, max_year + 1):
        count = year_counts.get(y, 0)
        current_ema = (alpha * count) + ((1.0 - alpha) * prev_ema)
        
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
        prev_ema = current_ema
        
    if best_year == 2022:
        result_codes.append(code)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-2614386764590376133': 'file_storage/function-call-2614386764590376133.json', 'var_function-call-2614386764590378216': 'file_storage/function-call-2614386764590378216.json', 'var_function-call-2614386764590376203': [{'count(*)': '277813'}], 'var_function-call-13581485319416773306': [{'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-13581485319416772329': [{'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-1876496665420648110': [{'symbol': 'C01B', 'level': '5.0'}], 'var_function-call-16781152453932160086': 'file_storage/function-call-16781152453932160086.json'}

exec(code, env_args)
