code = """import json
import re

# Load level 5 symbols
with open(locals()['var_function-call-2614386764590376133'], 'r') as f:
    cpc_defs = json.load(f)
level5_symbols = set(item['symbol'] for item in cpc_defs)

# Load publication info
with open(locals()['var_function-call-16781152453932160086'], 'r') as f:
    pub_info = json.load(f)

# Structure: {code: {year: count}}
cpc_counts = {}

# Relaxed regex
year_pattern = re.compile(r'(19|20)\d{2}')

for row in pub_info:
    f_date = row.get('filing_date')
    cpc_json = row.get('cpc')
    
    if not isinstance(f_date, str) or not cpc_json:
        continue
    
    # Parse year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Basic year filter to avoid bad data (e.g. 1900 or 2050)
    if year < 1900 or year > 2025:
        continue

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

# Calculate EMA
result_codes = []
alpha = 0.2

for code, year_counts in cpc_counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
        
    min_year = years[0]
    max_year = years[-1]
    
    # If the max year in data is less than 2022, it can't be the best year 2022 unless we project?
    # But if the data stops at 2021, we can't say 2022 is best.
    # If data goes up to 2022 or beyond, we can check.
    # However, if max_year < 2022, then 2022 count is 0.
    # EMA will decay. So best year won't be 2022.
    # So we only care if max_year >= 2022.
    
    max_ema = -1.0
    best_year = -1
    
    prev_ema = float(year_counts[min_year])
    
    # Check first year
    if prev_ema > max_ema:
        max_ema = prev_ema
        best_year = min_year
        
    # Iterate
    # We must iterate continuously from min_year to max_year (or 2022 if we want to ensure we cover it? No, only up to available data usually).
    # But if the user asks "best year is 2022", it implies 2022 is in the range.
    
    for y in range(min_year + 1, max_year + 1):
        count = year_counts.get(y, 0)
        current_ema = (alpha * count) + ((1.0 - alpha) * prev_ema)
        
        # Use strict greater to update best_year to the new peak
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
        prev_ema = current_ema
        
    if best_year == 2022:
        result_codes.append(code)

# Sort results for consistent output
result_codes.sort()

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-2614386764590376133': 'file_storage/function-call-2614386764590376133.json', 'var_function-call-2614386764590378216': 'file_storage/function-call-2614386764590378216.json', 'var_function-call-2614386764590376203': [{'count(*)': '277813'}], 'var_function-call-13581485319416773306': [{'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-13581485319416772329': [{'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-1876496665420648110': [{'symbol': 'C01B', 'level': '5.0'}], 'var_function-call-16781152453932160086': 'file_storage/function-call-16781152453932160086.json', 'var_function-call-13569511951389533102': [], 'var_function-call-11370879038426979545': {}, 'var_function-call-13352540612842005112': 'file_storage/function-call-13352540612842005112.json'}

exec(code, env_args)
