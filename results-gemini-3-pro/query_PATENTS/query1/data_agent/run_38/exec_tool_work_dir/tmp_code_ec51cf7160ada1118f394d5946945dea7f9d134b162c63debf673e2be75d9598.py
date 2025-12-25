code = """import json
import re
import pandas as pd

# Load Level 5 symbols
with open(locals()['var_function-call-11252670295542494115'], 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

# Load Patent Filings
# The file contains a list of dicts.
# We will process it line by line if it's a JSONL or load the whole JSON if it's a JSON list.
# The tool output suggests it's a JSON list "[{...}, {...}]"
with open(locals()['var_function-call-2797324583492744393'], 'r') as f:
    filings_data = json.load(f)

# Helper to extract year
def extract_year(date_str):
    if not date_str:
        return None
    # Look for 4 digits in the range 1900-2025
    match = re.search(r'\b(19|20)\d{2}\b', str(date_str))
    if match:
        return int(match.group(0))
    return None

records = []

for entry in filings_data:
    year = extract_year(entry.get('filing_date'))
    if year is None:
        continue
    
    cpc_json = entry.get('cpc')
    if not cpc_json:
        continue
    
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Extract unique Level 5 codes for this patent
    # A patent might map to multiple codes. 
    # Usually we count it once per code per year? 
    # Or should we count all occurrences? 
    # "Patents filings each year" -> Number of patents filed.
    # If a patent has multiple CPC codes falling into the same Level 5 group, it counts as 1 filing for that group.
    # If it has codes in different groups, it counts for each group.
    
    seen_codes = set()
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        # Check if code maps to a Level 5 symbol
        # Assumption: Level 5 symbol is the first 4 chars (Subclass)
        # We need to verify if the extracted 4-char code is in our level5_codes set
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in level5_codes:
                seen_codes.add(subclass)
    
    for c in seen_codes:
        records.append({'year': year, 'code': c})

df = pd.DataFrame(records)

# Aggregate
# Count patents per code per year
counts = df.groupby(['code', 'year']).size().reset_index(name='count')

# Pivot to have years as index (or just iterate per code)
# We need to calculate EMA for each code over years.
# Ensure all years are present? Or just present years?
# "exponential moving average ... each year"
# Typically EMA runs over a continuous time series. 
# If a year is missing, the count is 0. 
# I should fill missing years with 0.

# Determine year range
min_year = counts['year'].min()
max_year = counts['year'].max()
all_years = range(min_year, max_year + 1)

codes = counts['code'].unique()

results = []

for code in codes:
    code_data = counts[counts['code'] == code].set_index('year').reindex(all_years, fill_value=0)
    
    # Calculate EMA
    # smoothing factor 0.2 -> alpha=0.2
    # adjust=False for recursive formula
    code_data['ema'] = code_data['count'].ewm(alpha=0.2, adjust=False).mean()
    
    # Find year with highest EMA
    best_year = code_data['ema'].idxmax()
    max_ema = code_data['ema'].max()
    
    if best_year == 2022:
        results.append(code)

# Sort results to be deterministic? 
results.sort()

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11252670295542494115': 'file_storage/function-call-11252670295542494115.json', 'var_function-call-11252670295542493418': 'file_storage/function-call-11252670295542493418.json', 'var_function-call-1816704933838744903': [{'count(*)': '277813'}], 'var_function-call-3705720165070456970': [{'level': '4.0', 'symbol': 'B04', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B23', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B30', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B21', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B25', 'parents': '[\n  "B"\n]'}], 'var_function-call-2797324583492744393': 'file_storage/function-call-2797324583492744393.json'}

exec(code, env_args)
