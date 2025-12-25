code = """import json
import re
import pandas as pd

# Load Level 5 CPC symbols
# var_function-call-15650209111599627391 contains the path to cpc_definition result
with open(locals()['var_function-call-15650209111599627391'], 'r') as f:
    cpc_defs = json.load(f)

# Extract symbols into a set
# The result structure is [{"symbol": "B28D"}, ...]
level_5_codes = set(item['symbol'] for item in cpc_defs)

# Load Publication Info
# var_function-call-13092592968484268973 contains the path to publicationinfo result
with open(locals()['var_function-call-13092592968484268973'], 'r') as f:
    pubs = json.load(f)

# Dictionary to store counts: counts[code][year] = count
counts = {}
years_seen = set()

date_pattern = re.compile(r'\b(19|20)\d{2}\b')

for p in pubs:
    # Extract Year
    f_date = p.get('filing_date', '')
    if not f_date:
        continue
    match = date_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    years_seen.add(year)
    
    # Extract CPC codes
    cpc_str = p.get('cpc', '')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Get unique Level 5 codes for this patent
    patent_codes = set()
    for entry in cpc_list:
        full_code = entry.get('code', '')
        if len(full_code) >= 4:
            subclass = full_code[:4] # Level 5 seems to be 4 chars (Subclass)
            if subclass in level_5_codes:
                patent_codes.add(subclass)
    
    # Increment counts
    for code in patent_codes:
        if code not in counts:
            counts[code] = {}
        counts[code][year] = counts[code].get(year, 0) + 1

if not counts:
    print("__RESULT__:")
    print("[]")
else:
    # Prepare for EMA calculation
    min_year = min(years_seen)
    max_year = max(years_seen)
    
    # Ensure 2022 is in range if data allows, otherwise data limits apply
    # The query specifically asks for 2022, so we hope data goes up to there.
    
    results = []
    
    for code, year_counts in counts.items():
        # Build time series
        series = []
        year_range = range(min_year, max_year + 1)
        
        # Calculate EMA
        ema_series = []
        prev_ema = None
        alpha = 0.2
        
        # Store (Year, EMA) pairs
        ema_values = []
        
        for y in year_range:
            val = year_counts.get(y, 0)
            if prev_ema is None:
                current_ema = val # Start with the first value (or 0 if start of range)
                # Correction: Often EMA starts at the first observation. 
                # If we start from min_year (global), and this code has no data yet, 
                # prev_ema = 0? Or should we wait for first data?
                # Standard Pandas ewm uses 'adjust=False' or 'adjust=True'.
                # Let's stick to simple recursive definition. 
                # Initialize with the count of the first year in the global range.
                # If 0, it starts at 0.
            else:
                current_ema = (val * alpha) + (prev_ema * (1 - alpha))
            
            prev_ema = current_ema
            ema_values.append((y, current_ema))
        
        # Find best year
        # Sort by EMA desc, then Year desc (latest year preferred? or just max)
        # "Best year" = Year with max EMA.
        best_year, max_ema = max(ema_values, key=lambda x: x[1])
        
        if best_year == 2022:
            results.append(code)

    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-15650209111599627391': 'file_storage/function-call-15650209111599627391.json', 'var_function-call-13092592968484268973': 'file_storage/function-call-13092592968484268973.json'}

exec(code, env_args)
