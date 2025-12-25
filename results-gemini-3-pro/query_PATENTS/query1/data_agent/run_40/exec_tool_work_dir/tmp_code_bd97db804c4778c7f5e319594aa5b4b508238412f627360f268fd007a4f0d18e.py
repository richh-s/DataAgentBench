code = """import json
import re

# Load level 5 symbols
# Using the variable names provided in previous steps
l5_path = locals()['var_function-call-15361020114366599726']
pubs_path = locals()['var_function-call-16075540632948786396']

with open(l5_path, 'r') as f:
    l5_data = json.load(f)

# Check lengths of symbols
lengths = set(len(item['symbol']) for item in l5_data)
# We expect only length 4
# print(f"Lengths: {lengths}")

l5_symbols = set(item['symbol'] for item in l5_data)

# Load publication data
with open(pubs_path, 'r') as f:
    pubs = json.load(f)

counts = {}
year_pattern = re.compile(r'\b((?:19|20)\d{2})\b')

for p in pubs:
    # Parse year
    f_date = p.get('filing_date', '')
    if not isinstance(f_date, str):
        continue
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(1))
    
    # Parse CPC
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    if not isinstance(cpc_list, list):
        continue

    # Identify unique level 5 symbols for this patent
    patent_symbols = set()
    for entry in cpc_list:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code', '')
        if not code:
            continue
        
        # Strategy: check if the first 4 chars form a valid level 5 symbol
        # This assumes level 5 symbols are 4 chars long.
        # If there are symbols of different lengths, this might need adjustment.
        # Based on the preview, they are 4 chars.
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in l5_symbols:
                patent_symbols.add(prefix)
    
    # Update counts
    for sym in patent_symbols:
        if sym not in counts:
            counts[sym] = {}
        counts[sym][year] = counts[sym].get(year, 0) + 1

# Calculate EMA and find best year
alpha = 0.2
result_symbols = []

for sym, year_counts in counts.items():
    if not year_counts:
        continue
        
    min_year = min(year_counts.keys())
    max_year = max(year_counts.keys())
    
    # We must consider up to 2022 to verify if it is the best year.
    # If the data for a symbol stops before 2022, 2022 counts as 0.
    # We should iterate up to max(max_year, 2022).
    # However, if max_year < 2022, 2022 will have 0 count and likely not be the best.
    # But if the peak was earlier, 0 won't change the max.
    # If the peak is 2022, we need to reach it.
    
    end_year = max(max_year, 2022)
    years = sorted(range(min_year, end_year + 1))
    
    ema = year_counts.get(min_year, 0)
    
    best_ema = ema
    best_year = min_year
    
    for y in years[1:]:
        val = year_counts.get(y, 0)
        ema = alpha * val + (1 - alpha) * ema
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    if best_year == 2022:
        result_symbols.append(sym)

print("__RESULT__:")
print(json.dumps(result_symbols))"""

env_args = {'var_function-call-15361020114366599726': 'file_storage/function-call-15361020114366599726.json', 'var_function-call-15361020114366601035': [{'count(*)': '277813'}], 'var_function-call-16075540632948786396': 'file_storage/function-call-16075540632948786396.json'}

exec(code, env_args)
