code = """import json
import re

# Load Level 5 symbols
with open(locals()['var_function-call-3343180408967186434'], 'r') as f:
    l5_data = json.load(f)
    valid_l5 = set(item['symbol'] for item in l5_data)

# Load Patent Data
with open(locals()['var_function-call-18240871321988872143'], 'r') as f:
    patents = json.load(f)

# Data Structures
counts = {} # {cpc_code: {year: count}}
years_all = set()

# Process
for p in patents:
    f_date = p.get('filing_date', '')
    cpc_json = p.get('cpc', '[]')
    
    # Parse Year
    # Look for 4 digits starting with 19 or 20
    match = re.search(r'\b(19|20)\d{2}\b', f_date)
    if not match:
        continue
    year = int(match.group(0))
    years_all.add(year)
    
    # Parse CPC
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Extract unique valid Level 5 codes for this patent
    # A patent can have multiple codes. 
    # If it has "A01B 1/00", it counts for "A01B".
    # If it has "A01B 1/00" and "A01B 2/00", does it count once or twice for "A01B"?
    # Usually "patent filings" implies counting the patent once per category.
    # So I'll use a set of categories per patent.
    
    patent_cats = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        # Truncate to 4 chars
        if len(code) >= 4:
            sub = code[:4]
            if sub in valid_l5:
                patent_cats.add(sub)
    
    for c in patent_cats:
        if c not in counts:
            counts[c] = {}
        counts[c][year] = counts[c].get(year, 0) + 1

if not years_all:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(years_all)
max_year = max(years_all)

# Ensure 2022 is covered if it's within range or relevant
if 2022 > max_year:
    # If data doesn't reach 2022, then no CPC can have best year 2022 (unless we extrapolate, but we shouldn't)
    pass 

result_codes = []

alpha = 0.2

for cpc, year_counts in counts.items():
    # Construct time series
    # Start from the first year this CPC appeared? Or from min_year?
    # Usually EMA is path dependent. Starting from global min_year is safer to avoid bias 
    # but computationally slightly heavier. Given < 1000 CPCs and ~20-50 years, it's cheap.
    # However, if a CPC didn't exist (0 counts) for 50 years, EMA stays 0.
    
    # Let's start from min_year of the whole dataset to be consistent.
    
    ema_prev = None
    best_ema = -1.0
    best_y = -1
    
    # To handle "best year is 2022", we need to check the EMA for every year up to max_year.
    # We especially care if 2022 is the max.
    
    for y in range(min_year, max_year + 1):
        val = year_counts.get(y, 0)
        
        if ema_prev is None:
            # First value initialization
            # If we start at min_year and val is 0, EMA is 0.
            # If we strictly follow "EMA each year", we calculate for every year.
            ema = float(val) # Simple initialization: EMA_0 = val_0
            # Alternative: EMA_0 is undefined until first data point? 
            # If we assume 0 for years before first appearance, EMA stays 0 until first appearance.
            # So ema = val is fine if val is 0.
            ema_prev = ema
        else:
            ema = (val * alpha) + (ema_prev * (1 - alpha))
            ema_prev = ema
            
        if ema > best_ema:
            best_ema = ema
            best_y = y
        elif ema == best_ema:
            # Tie-breaking? Usually later year or just keep first found?
            # If tie, strictly speaking both are best. 
            # If 2022 is one of them, should we include? 
            # Let's update to most recent year if equal? Or keep first?
            # Standard "argmax" keeps first. Let's stick to strict inequality.
            pass
            
    if best_y == 2022:
        result_codes.append(cpc)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-17338831529942296706': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_function-call-14545777970731802458': 'file_storage/function-call-14545777970731802458.json', 'var_function-call-1814896835029975198': [{'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B1/02', 'level': '8.0', 'titleFull': 'Spades; Shovels'}], 'var_function-call-3343180408967186434': 'file_storage/function-call-3343180408967186434.json', 'var_function-call-7569759603939423118': [{'COUNT(*)': '277813'}], 'var_function-call-18240871321988872143': 'file_storage/function-call-18240871321988872143.json'}

exec(code, env_args)
