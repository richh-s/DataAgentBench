code = """import json
import re
import pandas as pd

# Load the Level 5 CPC symbols
with open(locals()['var_function-call-9506971857936168120'], 'r') as f:
    level5_data = json.load(f)

# Create a set of valid level 5 symbols
valid_level5 = set(item['symbol'] for item in level5_data)

# Load the publication info
with open(locals()['var_function-call-16148835938051840028'], 'r') as f:
    pub_data = json.load(f)

# Data structure to hold counts: {cpc_code: {year: count}}
cpc_counts = {}
all_years = set()

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for record in pub_data:
    # Extract Year
    f_date = record.get('filing_date', '')
    if not f_date:
        continue
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    all_years.add(year)
    
    # Extract CPCs
    cpc_str = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # specific to this record
    record_cpcs = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        # Map to level 5 (first 4 chars)
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in valid_level5:
                record_cpcs.add(subclass)
    
    # Update counts
    for cpc in record_cpcs:
        if cpc not in cpc_counts:
            cpc_counts[cpc] = {}
        cpc_counts[cpc][year] = cpc_counts[cpc].get(year, 0) + 1

if not all_years:
    print("__RESULT__:")
    print("[]")
else:
    min_year = min(all_years)
    max_year = max(all_years)
    
    # Calculate EMA
    # Smoothing factor alpha = 0.2
    alpha = 0.2
    
    # Store best year for each CPC
    target_cpcs = []
    
    sorted_years = sorted(list(all_years))
    
    for cpc, year_counts in cpc_counts.items():
        ema = 0
        best_ema = -1.0
        best_year = None
        
        # Initialize with the first year in the global range? 
        # Or the first year the CPC appears?
        # The prompt says "exponential moving average ... each year".
        # Usually one iterates through time.
        # If I start from min_year of the whole dataset:
        
        # Handling the first year:
        # If year == min_year, EMA = count.
        # Else EMA = alpha * count + (1-alpha) * prev_ema
        
        # Let's iterate through all years in the dataset to be consistent across technologies
        
        # First year logic
        first_y = sorted_years[0]
        ema = year_counts.get(first_y, 0)
        
        if ema > best_ema:
            best_ema = ema
            best_year = first_y
            
        for y in sorted_years[1:]:
            count = year_counts.get(y, 0)
            ema = alpha * count + (1 - alpha) * ema
            
            if ema > best_ema:
                best_ema = ema
                best_year = y
        
        if best_year == 2022:
            target_cpcs.append(cpc)
            
    print("__RESULT__:")
    print(json.dumps(target_cpcs))"""

env_args = {'var_function-call-9506971857936168120': 'file_storage/function-call-9506971857936168120.json', 'var_function-call-16148835938051840028': 'file_storage/function-call-16148835938051840028.json'}

exec(code, env_args)
