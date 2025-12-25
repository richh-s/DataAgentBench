code = """import json
import pandas as pd
from dateutil import parser as date_parser

# Access the file paths from previous tool results
# Using locals() to get the variable values dynamically
level_5_file = locals()['var_function-call-16990557340386241487']
publications_file = locals()['var_function-call-5319668294970635765']

# 1. Load Level 5 Symbols
with open(level_5_file, 'r') as f:
    level_5_data = json.load(f)

# Create a set of valid level 5 symbols
# We assume level 5 corresponds to the Subclass level (4 chars, e.g., 'A01B')
# We will verify this assumption by checking lengths.
valid_level_5 = set()
for item in level_5_data:
    sym = item['symbol']
    valid_level_5.add(sym)

# Check lengths to confirm strategy
lengths = set(len(s) for s in valid_level_5)
# print(f"DEBUG: Level 5 symbol lengths: {lengths}") 

# 2. Process Publications
counts = {} # {symbol: {year: count}}

with open(publications_file, 'r') as f:
    publications_data = json.load(f)

for record in publications_data:
    f_date_str = record.get('filing_date')
    cpc_str = record.get('cpc')
    
    if not f_date_str or not cpc_str:
        continue
        
    # Parse Year
    try:
        # fuzzy=True allows skipping extra text like "dated"
        dt = date_parser.parse(f_date_str, fuzzy=True)
        year = dt.year
    except:
        continue
        
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Extract unique level 5 symbols for this patent
    patent_symbols = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        # Try to map code to a valid level 5 symbol
        # Strategy: Try longest prefix match or just 4 chars?
        # Given the preview showed 4-char symbols for level 5, we try taking first 4 chars.
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in valid_level_5:
                patent_symbols.add(prefix)
            else:
                # Sometimes level 5 might be different length?
                # But based on standard CPC, Subclass is 4 chars.
                pass
    
    # Update counts
    for sym in patent_symbols:
        if sym not in counts:
            counts[sym] = {}
        counts[sym][year] = counts[sym].get(year, 0) + 1

# 3. Calculate EMA
# Formula: EMA_t = alpha * count_t + (1 - alpha) * EMA_{t-1}
alpha = 0.2
results = []

for sym, year_counts in counts.items():
    if not year_counts:
        continue
        
    years = sorted(year_counts.keys())
    # We should probably consider all years in the range to handle years with 0 filings properly?
    # "EMA of patent filings each year". If a year has 0 filings, count is 0.
    # So we should fill in the gaps between min and max year, or even start from min year of all data?
    # Usually EMA is continuous. I'll fill gaps between min(years) and max(years) for that symbol.
    
    min_year = years[0]
    max_year = years[-1]
    
    ema_vals = {}
    previous_ema = None
    
    # Iterate through all years for this symbol
    best_year = None
    max_ema = -1.0
    
    for y in range(min_year, max_year + 1):
        count = year_counts.get(y, 0)
        
        if previous_ema is None:
            current_ema = float(count)
        else:
            current_ema = alpha * count + (1 - alpha) * previous_ema
            
        ema_vals[y] = current_ema
        previous_ema = current_ema
        
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
        # Handle tie-breaking? The query doesn't specify.
        # But float comparison is tricky. exact match is rare.
        # Using > implies first occurrence or strictly greater.
    
    results.append({
        'symbol': sym,
        'best_year': best_year,
        'max_ema': max_ema
    })

# 4. Filter for Best Year == 2022
final_symbols = [r['symbol'] for r in results if r['best_year'] == 2022]

print("__RESULT__:")
print(json.dumps(final_symbols))"""

env_args = {'var_function-call-10895278239684927522': ['publicationinfo'], 'var_function-call-10895278239684931209': ['cpc_definition'], 'var_function-call-16990557340386241487': 'file_storage/function-call-16990557340386241487.json', 'var_function-call-16990557340386242026': 'file_storage/function-call-16990557340386242026.json', 'var_function-call-6988039574666266032': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}, {'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}], 'var_function-call-4440676724583882356': {'error': "name 'var_function_call_16990557340386241487' is not defined"}, 'var_function-call-5319668294970635765': 'file_storage/function-call-5319668294970635765.json'}

exec(code, env_args)
