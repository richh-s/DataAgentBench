code = """import json
import re
import pandas as pd

# Load Level 5 CPC symbols
with open(locals()['var_function-call-11899126964537840596'], 'r') as f:
    cpc_defs = json.load(f)

# Create a set of level 5 symbols
# From preview, they look like 'A01H'. 
level_5_symbols = set(item['symbol'] for item in cpc_defs)

# Load Patent Data
with open(locals()['var_function-call-2886696176158669052'], 'r') as f:
    patents = json.load(f)

# Regex for year extraction
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

# Data structure to hold counts: {symbol: {year: count}}
data_counts = {}

for p in patents:
    # Extract Year
    f_date = p.get('filing_date', '')
    if not f_date:
        continue
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Extract CPCs
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    # Identify unique level 5 symbols for this patent
    patent_symbols = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Try to match with level 5 symbols
        # Assumption: Level 5 symbols are prefixes (e.g. Subclasses like 'A01B')
        # We check if the code starts with any level 5 symbol.
        # Since level 5 symbols seem to be 4 chars, we can just take first 4 chars.
        # But to be safe, we check if the 4-char prefix is in our set.
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level_5_symbols:
                patent_symbols.add(prefix)
    
    # Update counts
    for sym in patent_symbols:
        if sym not in data_counts:
            data_counts[sym] = {}
        data_counts[sym][year] = data_counts[sym].get(year, 0) + 1

# Calculate EMA
# Smoothing factor alpha = 0.2
alpha = 0.2
results_best_year = {}

for sym, year_counts in data_counts.items():
    if not year_counts:
        continue
    
    # Get all years from min to max to handle missing years properly? 
    # The prompt says "patent filings each year". If a year has 0, EMA should update with 0?
    # Usually yes.
    min_year = min(year_counts.keys())
    max_year = max(year_counts.keys())
    
    # We should probably stop at 2022 or 2023 or 2024 depending on data.
    # But for "best year is 2022", we surely care about 2022.
    # Let's run up to the max year present in the data for that symbol.
    
    sorted_years = sorted(range(min_year, max_year + 1))
    
    ema = 0
    best_ema = -1
    best_year = -1
    
    first = True
    for y in sorted_years:
        count = year_counts.get(y, 0)
        if first:
            ema = count
            first = False
        else:
            ema = (count * alpha) + (ema * (1 - alpha))
        
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    results_best_year[sym] = best_year

# Filter for best year == 2022
final_cpc_codes = [sym for sym, year in results_best_year.items() if year == 2022]

print("__RESULT__:")
print(json.dumps(final_cpc_codes))"""

env_args = {'var_function-call-11899126964537840596': 'file_storage/function-call-11899126964537840596.json', 'var_function-call-13245455590723009020': [{'count(*)': '277813'}], 'var_function-call-2886696176158669052': 'file_storage/function-call-2886696176158669052.json'}

exec(code, env_args)
