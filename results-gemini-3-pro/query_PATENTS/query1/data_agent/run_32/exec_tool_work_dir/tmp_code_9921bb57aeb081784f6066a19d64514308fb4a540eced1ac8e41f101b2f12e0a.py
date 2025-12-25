code = """import json
import re

# Load previous results
with open('var_function-call-7207860585803115625.json', 'r') as f:
    l5_data = json.load(f)

# Create set of Level 5 symbols
l5_symbols = set()
for item in l5_data:
    if 'symbol' in item:
        l5_symbols.add(item['symbol'])

with open('var_function-call-5530323500134500439.json', 'r') as f:
    patents = json.load(f)

counts = {} # {symbol: {year: count}}

# Process patents
for p in patents:
    # Extract Year
    d_str = p.get('filing_date', '')
    if not isinstance(d_str, str):
        continue
    
    # Look for 4 digit year, likely starting with 19 or 20
    match = re.search(r'\b(19|20)\d{2}\b', d_str)
    if match:
        year = int(match.group(0))
    else:
        continue

    # Extract CPC
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    if not isinstance(cpc_list, list):
        continue
        
    # Find unique Level 5 symbols for this patent
    patent_l5s = set()
    for item in cpc_list:
        code = item.get('code', '')
        if code and len(code) >= 4:
            prefix = code[:4]
            if prefix in l5_symbols:
                patent_l5s.add(prefix)
    
    # Update counts
    for sym in patent_l5s:
        if sym not in counts:
            counts[sym] = {}
        counts[sym][year] = counts[sym].get(year, 0) + 1

# Calculate EMA and find best year
alpha = 0.2
final_candidates = []

for sym, year_counts in counts.items():
    if not year_counts:
        continue
        
    min_year = min(year_counts.keys())
    max_year = max(year_counts.keys())
    
    # We must cover up to 2022 if we want to check if 2022 is the best.
    # If the max year in data is 2021, 2022 is essentially count 0.
    # EMA would decay. It's unlikely to be the peak if count is 0, unless previous years were negative (impossible).
    # So if max_year < 2022, 2022 is not the peak (it would be lower than 2021 EMA).
    # If max_year > 2022, we check normally.
    # We should iterate up to max(max_year, 2022) to be safe? 
    # No, we strictly follow the data. If data ends in 2020, best year is within data range.
    
    current_ema = 0
    first = True
    
    max_ema_val = -1.0
    max_ema_year = -1
    
    # Iterate through all years
    for y in range(min_year, max_year + 1):
        cnt = year_counts.get(y, 0)
        
        if first:
            current_ema = cnt
            first = False
        else:
            current_ema = alpha * cnt + (1 - alpha) * current_ema
        
        if current_ema > max_ema_val:
            max_ema_val = current_ema
            max_ema_year = y
        # If equal, we keep the first occurrence or handle as you prefer.
        # Usually peak is the first time it reaches that max if it plateaus? 
        # Or last? Let's stick to strict greater.
            
    if max_ema_year == 2022:
        final_candidates.append(sym)

print("__RESULT__:")
print(json.dumps(final_candidates))"""

env_args = {'var_function-call-16354257400330351795': 'file_storage/function-call-16354257400330351795.json', 'var_function-call-16354257400330353054': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-10560939620404889531': [{'symbol': 'H01M', 'level': '5.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'H01M10/0565', 'level': '11.0'}], 'var_function-call-16184128629487448997': [{'len': '4', 'cnt': '677'}], 'var_function-call-4973736629774637364': [{'cnt': '277813'}], 'var_function-call-7207860585803115625': 'file_storage/function-call-7207860585803115625.json', 'var_function-call-5530323500134500439': 'file_storage/function-call-5530323500134500439.json'}

exec(code, env_args)
