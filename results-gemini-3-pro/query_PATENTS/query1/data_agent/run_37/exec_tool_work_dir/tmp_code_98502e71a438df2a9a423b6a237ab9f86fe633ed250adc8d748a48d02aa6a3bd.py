code = """import json
import re

# Get file paths from local variables
path_l5 = locals()['var_function-call-3410019379130597084']
path_pubs = locals()['var_function-call-7906511271909197248']

# Load Level 5 symbols
with open(path_l5, 'r') as f:
    l5_data = json.load(f)
l5_symbols = set(item['symbol'] for item in l5_data)

# Load publications
with open(path_pubs, 'r') as f:
    pubs = json.load(f)

counts = {} # (symbol, year) -> count
all_years = set()

for p in pubs:
    # Parse year
    d = p.get('filing_date')
    if not d: continue
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
        if len(code) >= 4:
            cand = code[:4]
            if cand in l5_symbols:
                codes_in_pub.add(cand)
        elif code in l5_symbols:
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

found_symbols = set(s for s, y in counts.keys())

for s in found_symbols:
    # EMA Calculation
    # We scan from min_year to max_year
    ema = counts.get((s, min_year), 0)
    best_ema = ema
    best_year = min_year
    
    # If a symbol had no counts at min_year, ema starts at 0.
    
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

env_args = {'var_function-call-3412756028934432070': 'file_storage/function-call-3412756028934432070.json', 'var_function-call-3412756028934430865': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-3410019379130597084': 'file_storage/function-call-3410019379130597084.json', 'var_function-call-10501866726357771340': [{'level': '2.0', 'sample_symbol': 'Y'}, {'level': '4.0', 'sample_symbol': 'Y10'}, {'level': '5.0', 'sample_symbol': 'Y10T'}, {'level': '7.0', 'sample_symbol': 'Y10T83/00'}, {'level': '8.0', 'sample_symbol': 'Y10T83/97'}, {'level': '9.0', 'sample_symbol': 'Y10T83/96'}, {'level': '10.0', 'sample_symbol': 'Y10T83/9498'}, {'level': '11.0', 'sample_symbol': 'Y10T83/949'}, {'level': '12.0', 'sample_symbol': 'Y10T83/9486'}, {'level': '13.0', 'sample_symbol': 'Y10T83/9341'}, {'level': '14.0', 'sample_symbol': 'Y10T83/9338'}, {'level': '15.0', 'sample_symbol': 'Y10T83/656'}, {'level': '16.0', 'sample_symbol': 'Y10T70/7616'}, {'level': '17.0', 'sample_symbol': 'Y10T70/761'}, {'level': '18.0', 'sample_symbol': 'Y10T70/5473'}, {'level': '19.0', 'sample_symbol': 'H01L2224/45984'}], 'var_function-call-7906511271909197248': 'file_storage/function-call-7906511271909197248.json', 'var_function-call-10796942973819325316': [], 'var_function-call-10181520103458689916': 'Done', 'var_function-call-12627134431421983675': {'pubs_error': "[Errno 2] No such file or directory: 'var_function-call-7906511271909197248'", 'years_count': 0, 'l5_error': "[Errno 2] No such file or directory: 'var_function-call-3410019379130597084'", 'sample_matched_l5': [], 'cpc_hits_first_100': 0}}

exec(code, env_args)
