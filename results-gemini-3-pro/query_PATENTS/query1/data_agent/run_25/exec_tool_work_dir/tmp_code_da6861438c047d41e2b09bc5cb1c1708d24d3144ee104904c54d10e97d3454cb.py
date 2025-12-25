code = """import json
import re
import pandas as pd

# Load Level 5 codes
with open(locals()['var_function-call-11747405801204171974'], 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

# Load Publication Data
with open(locals()['var_function-call-6610964282860133498'], 'r') as f:
    pub_data = json.load(f)

# Data Structures
# counts: {year: {cpc_code: count}}
counts = {}

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for row in pub_data:
    f_date = row.get('filing_date')
    cpc_json = row.get('cpc')
    
    if not f_date or not cpc_json:
        continue
        
    # Extract Year
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    # Assuming the year is the last 4-digit number if multiple (though 20xx is safer)
    # Re-running regex to get full match
    full_matches = [m for m in re.findall(r'\b(19|20)\d{2}\b', f_date)]
    if not full_matches:
        continue
    year = int(full_matches[-1]) # Use the last found year, commonly at the end "March 2019"
    
    # Extract CPC Codes
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Identify unique Level 5 codes for this patent
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Map to Level 5: First 4 chars?
        # Check if any level 5 code is a prefix of this code
        # Since all Level 5 codes are 4 chars, we can just take first 4 chars
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                patent_codes.add(prefix)
    
    # Update Counts
    if year not in counts:
        counts[year] = {}
    
    for pc in patent_codes:
        counts[year][pc] = counts[year].get(pc, 0) + 1

# Calculate EMA
# alpha = 0.2
alpha = 0.2

# Get all unique CPC codes encountered
all_cpcs = set()
for y in counts:
    all_cpcs.update(counts[y].keys())

if not counts:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(counts.keys())
max_year = max(counts.keys())

# Organize data by CPC: {cpc: {year: count}}
cpc_timeline = {cpc: {} for cpc in all_cpcs}
for y in range(min_year, max_year + 1):
    curr_counts = counts.get(y, {})
    for cpc in all_cpcs:
        cpc_timeline[cpc][y] = curr_counts.get(cpc, 0)

# Compute EMA and Find Best Year
result_codes = []

for cpc in all_cpcs:
    timeline = cpc_timeline[cpc]
    sorted_years = sorted(timeline.keys())
    
    ema = 0
    max_ema = -1.0
    best_year = -1
    
    # Initialize EMA
    # Option 1: EMA_0 = Count_0 (for the first year with data? or the global start?)
    # "each year" implies we should run through the years.
    # Standard: EMA_t = alpha * x_t + (1-alpha) * EMA_{t-1}
    # Initialize EMA with the first value.
    
    # Let's run from min_year to max_year
    first_year = True
    
    for y in sorted_years:
        count = timeline[y]
        if first_year:
            ema = count # Initialize with first data point
            first_year = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
        # Tie-breaking: if equal? Usually first or last. But max is float.
        # If strictly greater, we update.
    
    if best_year == 2022:
        result_codes.append(cpc)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-16849742418819018650': 'file_storage/function-call-16849742418819018650.json', 'var_function-call-2105601753514837134': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_function-call-15924435190051233990': [{'symbol': 'A62B', 'level': '5.0'}, {'symbol': 'A63G', 'level': '5.0'}, {'symbol': 'A63K', 'level': '5.0'}, {'symbol': 'A63B', 'level': '5.0'}, {'symbol': 'C13B50/00', 'level': '7.0'}, {'symbol': 'H04Q2213/296', 'level': '8.0'}, {'symbol': 'A63J', 'level': '5.0'}, {'symbol': 'A63C', 'level': '5.0'}, {'symbol': 'A63D', 'level': '5.0'}, {'symbol': 'A63F', 'level': '5.0'}, {'symbol': 'C25D', 'level': '5.0'}, {'symbol': 'A63H', 'level': '5.0'}, {'symbol': 'A99Z', 'level': '5.0'}, {'symbol': 'B01J', 'level': '5.0'}, {'symbol': 'B01B', 'level': '5.0'}, {'symbol': 'B01D', 'level': '5.0'}, {'symbol': 'B01L', 'level': '5.0'}, {'symbol': 'C13B40/00', 'level': '7.0'}, {'symbol': 'B01F', 'level': '5.0'}, {'symbol': 'B02C', 'level': '5.0'}], 'var_function-call-14819640206453325990': [{'len': '4', 'cnt': '677'}], 'var_function-call-11747405801204171974': 'file_storage/function-call-11747405801204171974.json', 'var_function-call-6610964282860133498': 'file_storage/function-call-6610964282860133498.json'}

exec(code, env_args)
