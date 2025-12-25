code = """import json
import re
import pandas as pd

# Load level 5 symbols
with open(locals()['var_function-call-12377978627195880798'], 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

# Print sample to verify format
print("Sample level 5 codes:", list(level5_codes)[:10])

# Load publication data
with open(locals()['var_function-call-17981272633275780013'], 'r') as f:
    publications = json.load(f)

print(f"Total publications: {len(publications)}")

# Data structure to hold counts: {code: {year: count}}
counts = {}

year_regex = re.compile(r'\b(19|20)\d{2}\b')

for pub in publications:
    # Parse year
    filing_date = pub.get('filing_date', '')
    match = year_regex.search(filing_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Parse CPC
    cpc_str = pub.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Extract codes and map to level 5
    # Assuming level 5 codes are subclasses (4 chars), or we need to check prefix
    # Let's assume matching is by checking if the pub_code starts with the level5_code
    # Since checking all level 5 codes for every pub code is slow, and level 5 codes seem to be Subclasses (4 chars)
    # We will try to extract the first 4 chars and see if it is in level5_codes.
    
    unique_codes_for_patent = set()
    
    for entry in cpc_list:
        code = entry.get('code', '')
        # Try 4 chars
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                unique_codes_for_patent.add(prefix)
            else:
                # In case level 5 codes are not just 4 chars (e.g. A01B1/00), 
                # but based on the preview, they look like A01B, H01M, etc.
                # Let's stick to 4 chars for now. 
                # If there are longer level 5 codes, this might miss.
                pass
    
    for c in unique_codes_for_patent:
        if c not in counts:
            counts[c] = {}
        counts[c][year] = counts[c].get(year, 0) + 1

# Calculate EMA
alpha = 0.2
result_codes = []

for code, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    
    # We need a continuous range of years? Or just data points?
    # EMA is time-series. Ideally we should fill missing years with 0?
    # Or just iterate through available years? 
    # Usually "each year" implies a time series. If a year is missing, the count is 0.
    # Let's fill the range from min_year to max_year (or current year).
    
    min_year = years[0]
    max_year = 2023 # Assuming data goes up to recent
    
    # But wait, we only care if the BEST year is 2022.
    # So we need to calculate EMA up to at least 2022.
    
    # Let's create a full range of years
    full_years = range(min_year, max_year + 1)
    
    ema = 0
    max_ema = -1
    best_year = -1
    
    first = True
    for y in full_years:
        count = year_counts.get(y, 0)
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        # Track best year
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    if best_year == 2022:
        result_codes.append(code)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-11743318916466858898': 'file_storage/function-call-11743318916466858898.json', 'var_function-call-16238834244750781196': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-12377978627195880798': 'file_storage/function-call-12377978627195880798.json', 'var_function-call-17981272633275780013': 'file_storage/function-call-17981272633275780013.json'}

exec(code, env_args)
