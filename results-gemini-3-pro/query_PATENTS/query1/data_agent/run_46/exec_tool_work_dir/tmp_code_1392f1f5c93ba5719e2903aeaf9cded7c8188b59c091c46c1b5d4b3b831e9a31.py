code = """import json
import re
import pandas as pd

# Load Level 5 symbols
with open(locals()['var_function-call-18248492955501393710'], 'r') as f:
    level5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_data)

# Load Patent Data
with open(locals()['var_function-call-9463417367070983'], 'r') as f:
    patents = json.load(f)

# Initialize counts
# Structure: {symbol: {year: count}}
counts = {}

year_pattern = re.compile(r'(\d{4})')

for patent in patents:
    # Extract Year
    f_date = patent.get('filing_date', '')
    if not f_date:
        continue
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(1))
    
    # Extract CPC codes
    cpc_str = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Get unique Level 5 symbols for this patent
    patent_symbols = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        # Check if code maps to a Level 5 symbol
        # Assuming Level 5 symbols are 4 characters (Subclass)
        # We take the first 4 chars of the code.
        if len(code) >= 4:
            candidate = code[:4]
            if candidate in level5_symbols:
                patent_symbols.add(candidate)
    
    # Update counts
    for sym in patent_symbols:
        if sym not in counts:
            counts[sym] = {}
        counts[sym][year] = counts[sym].get(year, 0) + 1

# Calculate EMA and find best year
alpha = 0.2
result_symbols = []

# Find global min/max year to align timelines?
# Or just process per symbol? "each year" implies the series for that symbol.
# Usually, EMA runs over the years present or a full range. 
# Best practice: Full range from min_year of the whole dataset to max_year.
all_years = set()
for sym in counts:
    all_years.update(counts[sym].keys())

if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(all_years)
max_year = max(all_years)
full_year_range = range(min_year, max_year + 1)

for sym, year_counts in counts.items():
    ema = None
    best_ema = -1
    best_year = -1
    
    # Iterate through the full range of years to handle zeros correctly
    for year in full_year_range:
        count = year_counts.get(year, 0)
        
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > best_ema:
            best_ema = ema
            best_year = year
            
    if best_year == 2022:
        result_symbols.append(sym)

print("__RESULT__:")
print(json.dumps(result_symbols))"""

env_args = {'var_function-call-18248492955501393710': 'file_storage/function-call-18248492955501393710.json', 'var_function-call-18248492955501392609': 'file_storage/function-call-18248492955501392609.json', 'var_function-call-2230299089368143118': [{'level': '5.0', 'symbol': 'A01B'}, {'level': '10.0', 'symbol': 'A01B3/12'}, {'level': '10.0', 'symbol': 'A01B3/70'}, {'level': '7.0', 'symbol': 'A01B1/00'}, {'level': '10.0', 'symbol': 'A01B3/18'}, {'level': '10.0', 'symbol': 'A01B3/20'}, {'level': '10.0', 'symbol': 'A01B3/10'}, {'level': '10.0', 'symbol': 'A01B3/08'}, {'level': '10.0', 'symbol': 'A01B3/22'}, {'level': '10.0', 'symbol': 'A01B3/44'}, {'level': '10.0', 'symbol': 'A01B3/42'}, {'level': '10.0', 'symbol': 'A01B3/56'}, {'level': '10.0', 'symbol': 'A01B3/54'}, {'level': '10.0', 'symbol': 'A01B3/60'}, {'level': '7.0', 'symbol': 'A01B9/00'}, {'level': '10.0', 'symbol': 'A01B3/34'}, {'level': '10.0', 'symbol': 'A01B3/30'}, {'level': '10.0', 'symbol': 'A01B3/14'}, {'level': '10.0', 'symbol': 'A01B3/32'}, {'level': '7.0', 'symbol': 'A01B3/00'}], 'var_function-call-2230299089368142565': [{'count(*)': '277813'}], 'var_function-call-9463417367070983': 'file_storage/function-call-9463417367070983.json'}

exec(code, env_args)
