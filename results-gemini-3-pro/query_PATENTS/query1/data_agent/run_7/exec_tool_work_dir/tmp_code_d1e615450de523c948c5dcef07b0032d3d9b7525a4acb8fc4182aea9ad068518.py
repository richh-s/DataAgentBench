code = """import json
import re
import pandas as pd

# Load Level 5 definitions
with open(locals()['var_function-call-7168665038669852193'], 'r') as f:
    definitions = json.load(f)
valid_cpcs = set(d['symbol'] for d in definitions)

# Load Patent Data
with open(locals()['var_function-call-12636907471574372890'], 'r') as f:
    patents = json.load(f)

# Initialize counts
# Structure: {cpc: {year: count}}
counts = {}

# Date regex
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for p in patents:
    cpc = p.get('cpc_l5')
    date_str = p.get('filing_date')
    
    if not cpc or not date_str:
        continue
    
    # Check if valid Level 5
    if cpc not in valid_cpcs:
        continue
        
    # Extract year
    match = year_pattern.search(date_str)
    if match:
        year = int(match.group(0))
        if cpc not in counts:
            counts[cpc] = {}
        counts[cpc][year] = counts[cpc].get(year, 0) + 1

# Calculate EMA and find best year
results = []
alpha = 0.2

for cpc, year_data in counts.items():
    if not year_data:
        continue
        
    years = sorted(year_data.keys())
    min_year = years[0]
    max_year = years[-1]
    
    # We iterate from min_year to max_year filling gaps
    # Initialize
    ema = year_data[min_year]
    best_ema = ema
    best_year = min_year
    
    # Iterate
    for y in range(min_year + 1, max_year + 1):
        cnt = year_data.get(y, 0)
        ema = alpha * cnt + (1 - alpha) * ema
        
        # Check best (strictly greater to keep first peak, or >=?
        # "Best year" usually implies the absolute maximum.
        # If there's a tie, usually the later one is considered the "record" or earlier?
        # I'll stick to strictly greater. If 2022 ties with 2021, and 2021 was best, then best is 2021.
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    if best_year == 2022:
        results.append(cpc)

# Sort results for consistency
results.sort()

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7168665038669852193': 'file_storage/function-call-7168665038669852193.json', 'var_function-call-10792060600082410393': 'file_storage/function-call-10792060600082410393.json', 'var_function-call-17520737272150592810': [{'symbol': 'C01B', 'level': '5.0'}, {'symbol': 'C', 'level': '2.0'}, {'symbol': 'C01', 'level': '4.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-1418283475394270998': [{'count(*)': '277813'}], 'var_function-call-6985419727303954916': [{'code': 'C01B33/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01B35/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0565', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0562', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01G45/006', 'filing_date': 'dated 5th March 2019'}], 'var_function-call-12636907471574372890': 'file_storage/function-call-12636907471574372890.json'}

exec(code, env_args)
