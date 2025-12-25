code = """import json
import re

# Load Level 5 CPC symbols
with open(locals()['var_function-call-15650209111599627391'], 'r') as f:
    cpc_defs = json.load(f)
level_5_codes = set(item['symbol'] for item in cpc_defs)

# Load Publication Info
with open(locals()['var_function-call-13092592968484268973'], 'r') as f:
    pubs = json.load(f)

counts = {}
years_seen = set()

# Improved regex
date_pattern = re.compile(r'(19|20)\d{2}')

for p in pubs:
    f_date = p.get('filing_date', '')
    if not f_date:
        continue
    match = date_pattern.search(f_date)
    if not match:
        continue
    
    try:
        year = int(match.group(0))
    except ValueError:
        continue

    years_seen.add(year)
    
    cpc_str = p.get('cpc', '')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_codes = set()
    for entry in cpc_list:
        full_code = entry.get('code', '')
        if len(full_code) >= 4:
            subclass = full_code[:4]
            if subclass in level_5_codes:
                patent_codes.add(subclass)
    
    for code in patent_codes:
        if code not in counts:
            counts[code] = {}
        counts[code][year] = counts[code].get(year, 0) + 1

if not counts:
    print("__RESULT__:")
    print("[]")
else:
    min_year = min(years_seen)
    max_year = max(years_seen)
    
    results = []
    
    # Iterate all codes
    for code, year_counts in counts.items():
        # Build EMA series
        # We must iterate strictly from min_year to max_year (or 2022 if higher/lower)
        # Assuming we want to capture the trend over the years available in the db.
        # However, the prompt implies "Identify ... each year".
        
        # Note: If a code has no filings before 2020, its EMA starts then.
        # But to be comparable, we usually align to the same timeline or just process per code history.
        # "Best year" implies comparing EMA(y) for y in Years.
        
        ema_values = []
        prev_ema = None
        alpha = 0.2
        
        for y in range(min_year, max_year + 1):
            val = year_counts.get(y, 0)
            if prev_ema is None:
                # Initialize
                # If we are filling gaps with 0, and the series starts with 0s, 
                # then EMA stays 0 until first data.
                current_ema = val
            else:
                current_ema = (val * alpha) + (prev_ema * (1 - alpha))
            
            prev_ema = current_ema
            ema_values.append((y, current_ema))
        
        # Find best year
        if not ema_values:
            continue
            
        best_year, max_ema = max(ema_values, key=lambda x: x[1])
        
        if best_year == 2022:
            results.append(code)

    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-15650209111599627391': 'file_storage/function-call-15650209111599627391.json', 'var_function-call-13092592968484268973': 'file_storage/function-call-13092592968484268973.json', 'var_function-call-348235414228454795': [], 'var_function-call-3774834379313605805': {'l5_count': 677, 'l5_samples': ['B28D', 'B29D', 'B29K', 'B29C', 'B29B', 'B29L', 'B30B', 'B31D', 'B31B', 'B64G'], 'pubs_count': 277813, 'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'extracted_years': [], 'sample_cpc_extracted': [['C01B', 'C01B', 'H01M', 'H01M', 'C01G', 'H01M', 'H01M', 'C01P', 'C01G', 'Y02E', 'C01P', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'C01B', 'H01M', 'H01M', 'H01M', 'H01M', 'C01B', 'H01M', 'H01M', 'C01B', 'H01M', 'C01B', 'C01P', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'C01G'], ['F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H', 'F16H'], ['B29C', 'C08J', 'C08J', 'C08J', 'C08J', 'B32B', 'B32B', 'C09D', 'B29L', 'B32B', 'C08G', 'B32B', 'B29C', 'B32B', 'B32B', 'B29K', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'C08J', 'B32B', 'B32B', 'B32B', 'C08G', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'C08G', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'C08G', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'B32B', 'B29K', 'C08G', 'B32B', 'B32B', 'B29C', 'B32B', 'B29L', 'B29K', 'B32B', 'B29K', 'B32B', 'B32B', 'B29C', 'C08J', 'C08J'], ['A61K', 'C12N', 'C12N', 'A01K', 'A01K', 'C12N', 'C12N', 'A61P', 'A61K', 'C12N', 'C12N', 'A01K', 'A61K', 'C12N', 'C12N', 'C12N', 'A61K', 'C12N', 'C12N', 'C12N'], ['H01H', 'H01H', 'H01H', 'H01H', 'H01H', 'H01H', 'H01H', 'H01H', 'H01H', 'H01H', 'H01H']], 'matches_in_1000': 1000}}

exec(code, env_args)
