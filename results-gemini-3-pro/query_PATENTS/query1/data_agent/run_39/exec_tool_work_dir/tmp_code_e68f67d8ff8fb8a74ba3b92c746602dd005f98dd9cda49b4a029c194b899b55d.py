code = """import json
import re
import pandas as pd

# Load Level 5 CPC symbols
# var_function-call-4228191098478002445 is a file path to the result of list query
with open(locals()['var_function-call-4228191098478002445'], 'r') as f:
    l5_data = json.load(f)

# Extract symbols into a set
target_cpcs = set(item['symbol'] for item in l5_data)

# Load publication info
# var_function-call-4228191098478004752 is a file path
with open(locals()['var_function-call-4228191098478004752'], 'r') as f:
    pub_data = json.load(f)

# Structure to hold counts: counts[cpc][year] = count
counts = {}

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for row in pub_data:
    f_date = row.get('filing_date', '')
    if not f_date:
        continue
    
    # Extract year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Check bounds (optional, but good for sanity)
    if year < 1900 or year > 2025:
        continue
        
    cpc_json = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Collect unique target CPCs for this patent to avoid double counting same subclass in one patent?
    # Usually one patent contributes 1 count to a category if it classifies there.
    # If a patent has multiple codes in the same subclass, does it count once or multiple times?
    # "Patent filings" usually refers to the number of patents. So one patent = 1 count per area.
    seen_in_this_patent = set()
    
    for entry in cpc_list:
        code = entry.get('code', '')
        # Map to level 5 (assuming 4 chars based on previous analysis)
        # If code is "C01B33/00", prefix is "C01B" (4 chars)
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in target_cpcs:
                seen_in_this_patent.add(prefix)
    
    for cpc in seen_in_this_patent:
        if cpc not in counts:
            counts[cpc] = {}
        counts[cpc][year] = counts[cpc].get(year, 0) + 1

# Calculate EMA
# alpha = 0.2
alpha = 0.2
results = []

for cpc, year_counts in counts.items():
    if not year_counts:
        continue
    
    sorted_years = sorted(year_counts.keys())
    # Fill in missing years with 0? 
    # EMA is time-series. If a year has 0 filings, it should affect EMA.
    # Range from min_year to max_year (or 2022/2023?)
    # "Identify the CPC technology areas with the highest exponential moving average ... each year"
    # "return only the CPC group codes ... whose best year is 2022"
    
    min_year = sorted_years[0]
    max_year = sorted_years[-1] # or 2022? Assuming data goes up to at least 2022.
    
    # We need to check if 2022 is the best year. We should compute up to 2022 (or later if data exists).
    # If max_year < 2022, then best year cannot be 2022 (unless we assume EMA decays and 2022 isn't the best).
    # But strictly, if data ends in 2019, we don't know about 2022.
    # Assuming the database contains recent data.
    
    full_years = range(min_year, max(max_year, 2022) + 1)
    
    ema = 0
    best_ema = -1
    best_year = -1
    
    first = True
    for y in full_years:
        count = year_counts.get(y, 0)
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    if best_year == 2022:
        results.append(cpc)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4228191098478004752': 'file_storage/function-call-4228191098478004752.json', 'var_function-call-4228191098478002445': 'file_storage/function-call-4228191098478002445.json'}

exec(code, env_args)
