code = """import json
import pandas as pd
import re
from datetime import datetime

# Load CPC Definitions
with open(locals()['var_function-call-644042778612486334'], 'r') as f:
    cpc_defs = json.load(f)

# Create a map of symbol to title and store symbol lengths to determine mapping
cpc_map = {}
symbol_lengths = set()
for item in cpc_defs:
    sym = item['symbol']
    cpc_map[sym] = item['titleFull']
    symbol_lengths.add(len(sym))

print(f"DEBUG: CPC Level 4 Symbol lengths: {symbol_lengths}")
# Assuming typical lengths. If mixed, we might need a better matching strategy.
# If lengths are 3 (e.g. A01), we truncate patent codes to 3 chars.
# If lengths are 4 (e.g. A01B), we truncate to 4 chars.
target_len = list(symbol_lengths)[0] if len(symbol_lengths) == 1 else 4 
# Default to 4 if mixed or uncertain, but let's see debug output.

# Load Publication Info
with open(locals()['var_function-call-644042778612486557'], 'r') as f:
    pubs = json.load(f)

print(f"DEBUG: Loaded {len(pubs)} publications.")

filtered_pubs = []
germany_pattern = re.compile(r'\bDE\b|Germany|German', re.IGNORECASE)
de_code_pattern = re.compile(r'\bDE[- ]', re.IGNORECASE) # Matches DE- or DE followed by space

for p in pubs:
    # 1. Filter by Grant Date (July 1, 2019 to Dec 31, 2019)
    g_date_str = p.get('grant_date', '')
    if not g_date_str:
        continue
    
    # Parse natural language date
    # Formats seen: "3rd August 2021", "dated 6th October 2020", "14th Mar 2019", "2013, June 17th"
    # "Mar 19th, 2019", "2019 on Jul 12th"
    # Cleaning the string to make it parseable
    # Remove 'dated', 'on', 'of', 'the'
    clean_date = re.sub(r'(dated|on|of|the|rd|st|nd|th|,)', '', g_date_str, flags=re.IGNORECASE)
    # Result: "3 August 2021", "6 October 2020", "14 Mar 2019", "2013 June 17", "Mar 19 2019", "2019 Jul 12"
    
    try:
        # Try different formats
        # We need to handle mixed order
        # Let's use dateutil if available, but it's not standard.
        # Manual parsing: split by whitespace. find year (4 digits), month (alpha), day (digits)
        parts = clean_date.split()
        year = None
        month = None
        day = None
        
        for part in parts:
            if part.isdigit():
                if len(part) == 4:
                    year = int(part)
                else:
                    day = int(part)
            else:
                # Month?
                try:
                    dt = datetime.strptime(part, "%B") # Full name
                    month = dt.month
                except:
                    try:
                        dt = datetime.strptime(part, "%b") # Abbr
                        month = dt.month
                    except:
                        pass
        
        if year and month and day:
             g_date = datetime(year, month, day)
        else:
             continue # Skip if date parse fails

    except:
        continue

    if year != 2019:
        continue
    if month < 7:
        continue

    # 2. Filter for Germany
    # Check Patents_info
    p_info = p.get('Patents_info', '')
    # Check for DE- or "from DE"
    is_germany = False
    if "from DE" in p_info or "In DE" in p_info:
        is_germany = True
    elif de_code_pattern.search(p_info):
        is_germany = True
    
    if not is_germany:
        continue

    filtered_pubs.append(p)

print(f"DEBUG: Filtered to {len(filtered_pubs)} Germany patents in H2 2019.")

# Process Filings
cpc_filings = {} # cpc_code -> {year: count}

for p in filtered_pubs:
    # Filing Date
    f_date_str = p.get('filing_date', '')
    if not f_date_str:
        continue
    
    # Parse filing year
    clean_f_date = re.sub(r'(dated|on|of|the|rd|st|nd|th|,)', '', f_date_str, flags=re.IGNORECASE)
    parts = clean_f_date.split()
    f_year = None
    for part in parts:
        if part.isdigit() and len(part) == 4:
            f_year = int(part)
            break
    
    if not f_year:
        continue

    # Extract CPCs
    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue

    seen_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Map to Level 4
        # Use target_len from earlier
        if len(code) >= target_len:
            mapped_code = code[:target_len]
            # Check if this mapped code is in our Level 4 definitions
            if mapped_code in cpc_map:
                if mapped_code not in seen_codes:
                    seen_codes.add(mapped_code)
                    if mapped_code not in cpc_filings:
                        cpc_filings[mapped_code] = {}
                    cpc_filings[mapped_code][f_year] = cpc_filings[mapped_code].get(f_year, 0) + 1

# Calculate EMA
results = []
alpha = 0.1

for code, filings in cpc_filings.items():
    if not filings:
        continue
    
    years = sorted(filings.keys())
    min_year = years[0]
    max_year = years[-1]
    
    # Fill range
    ema_series = []
    current_ema = None
    best_ema = -1
    best_year = None
    
    # Iterate through all years in range
    for y in range(min_year, max_year + 1):
        count = filings.get(y, 0)
        if current_ema is None:
            current_ema = count # Initialize with first data point
        else:
            current_ema = alpha * count + (1 - alpha) * current_ema
        
        if current_ema > best_ema:
            best_ema = current_ema
            best_year = y
            
    results.append({
        "CPC Group Code": code,
        "Full Title": cpc_map[code],
        "Best Year": best_year,
        "Max EMA": best_ema
    })

# Sort by Max EMA descending
results.sort(key=lambda x: x['Max EMA'], reverse=True)

# Limit output if needed, but query asks for "The CPC technology areas...", implying all relevant ones.
# However, if the list is huge, I should probably limit it.
# Let's print top 20 for the answer, or check size.
print("__RESULT__:")
print(json.dumps(results[:20])) # Return top 20"""

env_args = {'var_function-call-10772616922719850629': 'file_storage/function-call-10772616922719850629.json', 'var_function-call-644042778612486334': 'file_storage/function-call-644042778612486334.json', 'var_function-call-644042778612486557': 'file_storage/function-call-644042778612486557.json'}

exec(code, env_args)
