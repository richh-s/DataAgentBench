code = """import json
import re
import pandas as pd

# Load Level 5 CPC symbols
with open('var_function-call-17682530284056883508.json', 'r') as f:
    cpc_defs = json.load(f)

level_5_symbols = set()
for item in cpc_defs:
    if 'symbol' in item:
        level_5_symbols.add(item['symbol'])

# Inspect format of level 5 symbols to determine how to match
sample_symbols = list(level_5_symbols)[:10]
print("Sample Level 5 Symbols:", sample_symbols)

# Determine if we should match exact codes or prefixes
# If symbols are 4 chars (e.g. A01B), we match first 4 chars of patent CPC.
# If symbols are like A01B1/00, we match full string.
match_length = 0
if all(len(s) == 4 for s in sample_symbols):
    match_mode = 'subclass'
    match_length = 4
else:
    match_mode = 'exact'

print(f"Match mode: {match_mode}")

# Load Patent Data
with open('var_function-call-1425838539260044447.json', 'r') as f:
    patents = json.load(f)

# Structure to hold counts: {cpc_code: {year: count}}
counts = {}

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for p in patents:
    f_date = p.get('filing_date', '')
    cpc_json = p.get('cpc', '[]')
    
    # Extract Year
    # Dates are like "dated 5th March 2019", "March the 18th, 2019"
    # We look for a 4 digit number starting with 19 or 20
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    year = int(matches[-1]) # Take the last one if multiple, usually just one
    
    # Extract CPC codes
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        if not code:
            continue
            
        target_code = None
        if match_mode == 'subclass':
            if len(code) >= 4:
                target_code = code[:4]
        else:
            # If match_mode is exact, we check if the code (or prefix) is in our set
            # But the set might contain codes of varying lengths? 
            # Let's assume the set defines the granularity.
            # If level 5 is "Group", it might be "A01B33/00".
            # The patent code might be "A01B33/00" or more specific.
            # We should probably check if any symbol in level_5_symbols matches the patent code.
            # Optimization: If all level 5 symbols are standard length or we can hash lookup.
            # For now, let's look at the sample symbols output to decide.
            target_code = code 

        if target_code and target_code in level_5_symbols:
            if target_code not in counts:
                counts[target_code] = {}
            counts[target_code][year] = counts[target_code].get(year, 0) + 1

# Calculate EMA
# Smoothing factor alpha = 0.2
alpha = 0.2
results = []

for code, year_counts in counts.items():
    if not year_counts:
        continue
        
    years = sorted(year_counts.keys())
    min_year = years[0]
    max_year = years[-1]
    
    # We need to process strictly from the first year of activity?
    # Or for all years in range? Usually EMA updates every period.
    # If there are gaps (years with 0 filings), EMA decays.
    # So we should iterate from min_year to max_year (or current year).
    # Let's iterate from min_year to 2022 (since we care about 2022).
    # Or just min_year to max_year_in_data.
    # But if max_year < 2022, then EMA in 2022 will be lower.
    # The query asks for "best year is 2022".
    
    # Let's assume we range from min_year to max(years) or 2022 (if we want to consider 2022 as a candidate).
    # If the latest data is 2023, we go to 2023.
    # Let's find the global max year in the dataset to define the timeline? 
    # Or just local.
    
    end_year = max(years)
    # If 2022 is not reached, then 2022 count is 0, EMA decays.
    if end_year < 2022:
        end_year = 2022
    
    ema = 0
    first = True
    best_ema = -1.0
    best_year = -1
    
    # EMA calculation
    # "EMA of patent filings each year"
    
    for y in range(min_year, end_year + 1):
        count = year_counts.get(y, 0)
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > best_ema:
            best_ema = ema
            best_year = y
        elif ema == best_ema:
            # If equal, do we prefer the later year? Or just keep the first found?
            # Or is it ambiguous?
            # Let's keep the earlier one or handle ties. 
            # If tie, and one is 2022, does it count?
            # Let's strictly update if ema > best_ema to keep the first occurrence of max?
            # Or updated if >= ?
            # Usually "best year" implies the peak.
            pass
            
    if best_year == 2022:
        results.append(code)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-17682530284056883508': 'file_storage/function-call-17682530284056883508.json', 'var_function-call-1425838539260044447': 'file_storage/function-call-1425838539260044447.json'}

exec(code, env_args)
