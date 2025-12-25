code = """import json
import re

# Load Level 5 CPC symbols
with open(locals()['var_function-call-11899126964537840596'], 'r') as f:
    cpc_defs = json.load(f)
level_5_symbols = set(item['symbol'] for item in cpc_defs)

# Load Patent Data
with open(locals()['var_function-call-2886696176158669052'], 'r') as f:
    patents = json.load(f)

# Improved regex
year_pattern = re.compile(r'\d{4}')

data_counts = {}

for p in patents:
    f_date = p.get('filing_date', '')
    matches = year_pattern.findall(f_date)
    year = None
    for m in matches:
        y = int(m)
        if 1900 <= y <= 2025:
            year = y
            break # Take the first valid year found
    
    if year is None:
        continue
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_symbols = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level_5_symbols:
                patent_symbols.add(prefix)
    
    for sym in patent_symbols:
        if sym not in data_counts:
            data_counts[sym] = {}
        data_counts[sym][year] = data_counts[sym].get(year, 0) + 1

# Calculate EMA
alpha = 0.2
results_best_year = {}

for sym, year_counts in data_counts.items():
    if not year_counts:
        continue
    
    min_year = min(year_counts.keys())
    max_year = max(year_counts.keys())
    
    # Fill missing years with 0
    # EMA must be updated for every year in the sequence
    sorted_years = range(min_year, max_year + 1)
    
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
        
        # We want the best year based on the EMA value at that year
        # Check if this year's EMA is the highest so far?
        # No, we need the global max EMA year.
        if ema > best_ema:
            best_ema = ema
            best_year = y
    
    # Store the best year
    results_best_year[sym] = best_year

# Filter for best year == 2022
final_cpc_codes = [sym for sym, year in results_best_year.items() if year == 2022]

print("__RESULT__:")
print(json.dumps(final_cpc_codes))"""

env_args = {'var_function-call-11899126964537840596': 'file_storage/function-call-11899126964537840596.json', 'var_function-call-13245455590723009020': [{'count(*)': '277813'}], 'var_function-call-2886696176158669052': 'file_storage/function-call-2886696176158669052.json', 'var_function-call-5697690738001880409': [], 'var_function-call-4493493728235645575': {'years_sample': [], 'min_year': None, 'max_year': None, 'symbols_matched_count': 103630, 'total_patents_checked': 10000}, 'var_function-call-9400873537323889565': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019']}

exec(code, env_args)
