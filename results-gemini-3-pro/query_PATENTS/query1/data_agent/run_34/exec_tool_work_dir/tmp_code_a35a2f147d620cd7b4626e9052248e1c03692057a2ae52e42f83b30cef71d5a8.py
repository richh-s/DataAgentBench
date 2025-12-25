code = """import json
import re

# Load Level 5 CPC codes
with open('var_function-call-17141822990107305310.json', 'r') as f:
    level5_data = json.load(f)

# Create a set of level 5 codes for fast lookup
# Also store them in a list to check lengths
level5_codes = set()
for item in level5_data:
    if 'symbol' in item:
        level5_codes.add(item['symbol'])

# Load Patent Data
with open('var_function-call-12961292587599410676.json', 'r') as f:
    patent_data = json.load(f)

# Helper to extract year
def extract_year(date_str):
    if not date_str:
        return None
    # Look for 4 digits starting with 19 or 20
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

# Aggregation
counts = {} # {cpc_code: {year: count}}
years = set()

# Pre-computation: sort level5 codes by length descending to match longest prefix first? 
# Or just finding which level 5 code is a prefix.
# Optimization: Most level 5 codes seem to be 4 chars.
# Let's check length distribution
lengths = set(len(c) for c in level5_codes)
# print(f"DEBUG: Level 5 code lengths: {lengths}")

# If multiple lengths, we need to be careful. 
# A patent code "A01B1/00" matches "A01B" (len 4).
# Does it match "A01" (len 3)? If "A01" is level 5.
# We should assign to the most specific level 5 code? Or all? 
# "CPC group codes at level 5". Each code in definition is distinct.
# The hierarchy is strict. A symbol is at level 5.
# If "A01B" is level 5, then "A01B..." belongs to it.
# If "A01" is level 5, "A01..." belongs to it.
# We can check if `code` starts with `l5_code`.
# To avoid ambiguity, we can assume the one that matches is the correct one.
# Usually levels don't overlap like that (e.g. if A01B is level 5, A01 isn't).
# But just in case, if we match, we take it.

for row in patent_data:
    f_date = row.get('filing_date')
    year = extract_year(f_date)
    if year is None:
        continue
    
    years.add(year)
    
    cpc_json = row.get('cpc')
    if not cpc_json:
        continue
    
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Extract codes from this patent
    patent_codes = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        if not code:
            continue
        # Find which level 5 code this belongs to
        # Optimization: Check prefixes.
        # Since we have many level 5 codes, checking all is slow.
        # But if most are 4 chars, we can slice.
        # Let's try slicing 4 chars first.
        prefix4 = code[:4]
        if prefix4 in level5_codes:
            patent_codes.add(prefix4)
        else:
            # Fallback: check other lengths if exist
            # This part depends on `lengths`. 
            # If `lengths` has only 4, we are done.
            # If not, we iterate.
            found = False
            for l in lengths:
                if l == 4: continue
                prefix = code[:l]
                if prefix in level5_codes:
                    patent_codes.add(prefix)
                    found = True
                    break # Assuming one match per level
            if not found:
                pass 

    for p_code in patent_codes:
        if p_code not in counts:
            counts[p_code] = {}
        counts[p_code][year] = counts[p_code].get(year, 0) + 1

# Calculate EMA
if not years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(years)
max_year = max(years)
all_years = sorted(list(years))

# Filter max_year to 2022? "best year is 2022".
# We should include 2022 in the range.
# If data goes beyond 2022, we consider that.
# If data stops before 2022, no code will have best year 2022 (unless it's the last year and max).

alpha = 0.2
results = []

for code, year_counts in counts.items():
    # Calculate EMA over the full range of years present in the data? 
    # Or just for the years the code exists?
    # Usually EMA is time-series. Better to run from min_year to max_year.
    
    ema = 0
    best_ema = -1
    best_year = -1
    
    # Initialize EMA?
    # Option 1: EMA_0 = value_0
    # Option 2: EMA starts at 0.
    # Given "exponential moving average of patent filings each year", usually implies a continuous update.
    # We will iterate from min_year to max_year.
    
    # Handling initialization:
    # If we start from min_year, EMA_previous is 0 initially? 
    # Or we skip until first data point?
    # Standard: EMA_today = alpha * Value + (1-alpha) * EMA_prev
    # If first point, EMA = Value.
    
    initialized = False
    
    for y in range(min_year, max_year + 1):
        val = year_counts.get(y, 0)
        
        if not initialized:
            if val > 0:
                ema = val
                initialized = True
                if ema > best_ema:
                    best_ema = ema
                    best_year = y
            # If val is 0 and not initialized, we stay not initialized (or ema=0)
        else:
            ema = (val * alpha) + (ema * (1 - alpha))
            if ema > best_ema:
                best_ema = ema
                best_year = y
                
        # We need to track the best year.
        # Note: if multiple years have same max, usually take the first or last?
        # Floating point comparison.
        # But strict inequality `>` takes the first one.
        # The query asks "whose best year is 2022".
        # We should check if best_year == 2022.
    
    # Edge case: If 2022 is not in the range, it can't be best.
    if best_year == 2022:
        results.append(code)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16843621957294656966': 'file_storage/function-call-16843621957294656966.json', 'var_function-call-6909709033955517173': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-17141822990107305310': 'file_storage/function-call-17141822990107305310.json', 'var_function-call-12961292587599410676': 'file_storage/function-call-12961292587599410676.json'}

exec(code, env_args)
