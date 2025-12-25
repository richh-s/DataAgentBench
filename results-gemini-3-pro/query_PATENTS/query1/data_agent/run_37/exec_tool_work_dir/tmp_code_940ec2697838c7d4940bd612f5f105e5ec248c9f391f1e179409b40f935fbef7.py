code = """import json
import re

# Load Level 5 symbols
try:
    with open('var_function-call-3410019379130597084', 'r') as f:
        l5_data = json.load(f)
    l5_symbols = set(item['symbol'] for item in l5_data)
except Exception as e:
    print(f"Error loading symbols: {e}")
    l5_symbols = set()

# Load publications
try:
    with open('var_function-call-7906511271909197248', 'r') as f:
        pubs = json.load(f)
except Exception as e:
    print(f"Error loading publications: {e}")
    pubs = []

counts = {} # (symbol, year) -> count
# Keep track of global years to define the range
all_years = set()

for p in pubs:
    # Parse year
    d = p.get('filing_date')
    if not d: continue
    # Regex for year 19xx or 20xx
    m = re.search(r'\b(19|20)\d{2}\b', d)
    if not m: continue
    year = int(m.group(0))
    all_years.add(year)

    # Parse CPC
    cpc_str = p.get('cpc')
    if not cpc_str: continue
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    # Extract codes
    codes_in_pub = set()
    for item in cpc_list:
        code = item.get('code')
        if not code: continue
        
        # Check against l5_symbols
        # Heuristic: First 4 chars
        if len(code) >= 4:
            cand = code[:4]
            if cand in l5_symbols:
                codes_in_pub.add(cand)
            # Should we check 3 chars or other lengths?
            # If code is shorter than 4, check full code
            # But L5 are usually 4.
        else:
            if code in l5_symbols:
                codes_in_pub.add(code)
            
    for s in codes_in_pub:
        counts[(s, year)] = counts.get((s, year), 0) + 1

if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(all_years)
max_year = max(all_years)
years = range(min_year, max_year + 1)

alpha = 0.2
filtered_symbols = []

# Iterate over all symbols found in the publications (that are also valid L5)
found_symbols = set(s for s, y in counts.keys())

for s in found_symbols:
    ema = 0
    best_ema = -1
    best_year = -1
    
    # Initialize EMA at the start of the time series
    # Using the first year's count as the seed
    # EMA_min_year = count_min_year
    
    # We iterate through the full range of years to maintain time continuity
    # If a symbol has no filings in a year, count is 0.
    
    # Start loop
    # Base case
    ema = counts.get((s, min_year), 0)
    best_ema = ema
    best_year = min_year
    
    for y in years:
        if y == min_year:
            continue
        
        count = counts.get((s, y), 0)
        ema = alpha * count + (1 - alpha) * ema
        
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    if best_year == 2022:
        filtered_symbols.append(s)

print("__RESULT__:")
print(json.dumps(filtered_symbols))"""

env_args = {'var_function-call-3412756028934432070': 'file_storage/function-call-3412756028934432070.json', 'var_function-call-3412756028934430865': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-3410019379130597084': 'file_storage/function-call-3410019379130597084.json', 'var_function-call-10501866726357771340': [{'level': '2.0', 'sample_symbol': 'Y'}, {'level': '4.0', 'sample_symbol': 'Y10'}, {'level': '5.0', 'sample_symbol': 'Y10T'}, {'level': '7.0', 'sample_symbol': 'Y10T83/00'}, {'level': '8.0', 'sample_symbol': 'Y10T83/97'}, {'level': '9.0', 'sample_symbol': 'Y10T83/96'}, {'level': '10.0', 'sample_symbol': 'Y10T83/9498'}, {'level': '11.0', 'sample_symbol': 'Y10T83/949'}, {'level': '12.0', 'sample_symbol': 'Y10T83/9486'}, {'level': '13.0', 'sample_symbol': 'Y10T83/9341'}, {'level': '14.0', 'sample_symbol': 'Y10T83/9338'}, {'level': '15.0', 'sample_symbol': 'Y10T83/656'}, {'level': '16.0', 'sample_symbol': 'Y10T70/7616'}, {'level': '17.0', 'sample_symbol': 'Y10T70/761'}, {'level': '18.0', 'sample_symbol': 'Y10T70/5473'}, {'level': '19.0', 'sample_symbol': 'H01L2224/45984'}], 'var_function-call-7906511271909197248': 'file_storage/function-call-7906511271909197248.json'}

exec(code, env_args)
