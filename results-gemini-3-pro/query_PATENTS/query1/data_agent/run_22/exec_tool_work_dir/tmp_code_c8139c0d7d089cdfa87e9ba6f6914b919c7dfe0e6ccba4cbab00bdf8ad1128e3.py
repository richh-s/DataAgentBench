code = """import json
import re
import pandas as pd

# Load Level 5 CPC symbols
cpc_file_path = locals()['var_function-call-15748739634169971950']
with open(cpc_file_path, 'r') as f:
    cpc_data = json.load(f)

# The result is a list of dicts: [{"symbol": "A01H"}, ...]
level5_symbols = set()
symbol_length = 0
for item in cpc_data:
    sym = item.get('symbol', '')
    if sym:
        level5_symbols.add(sym)
        if symbol_length == 0:
            symbol_length = len(sym)

# Load Patent Data
pub_file_path = locals()['var_function-call-14833157841070883006']
with open(pub_file_path, 'r') as f:
    pub_data = json.load(f)

# Dictionary to store counts: counts[symbol][year] = count
counts = {}

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for row in pub_data:
    f_date = row.get('filing_date', '')
    cpc_json = row.get('cpc', '[]')
    
    # Extract Year
    # Dates are like "dated 5th March 2019"
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    # matches returns list of tuples if groups, or strings.
    # regex (19|20)\d{2} has a group. findall returns the group.
    # We want the full match.
    # Let's use search or adjust regex.
    # Adjust regex to capture full year.
    # Actually matches will contain the capture group (19 or 20).
    # Let's use a simpler regex or iterate.
    
    # Better regex for year:
    y_matches = re.findall(r'\b(?:19|20)\d{2}\b', f_date)
    if not y_matches:
        continue
    year = int(y_matches[-1]) # Take the last one found, likely the year
    
    if year < 1900 or year > 2025:
        continue
        
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Get unique symbols for this patent that match level 5
    patent_symbols = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        # Check against level 5 symbols
        # If level 5 symbols are 4 chars (Subclass), we match prefix.
        # If they are longer, we might need exact match or prefix.
        # Based on preview, they are 4 chars.
        # Let's try matching the length of sample level 5 symbol.
        if len(code) >= symbol_length:
            candidate = code[:symbol_length]
            if candidate in level5_symbols:
                patent_symbols.add(candidate)
    
    for sym in patent_symbols:
        if sym not in counts:
            counts[sym] = {}
        counts[sym][year] = counts[sym].get(year, 0) + 1

# Calculate EMA and find best year
results = []
alpha = 0.2

for sym, year_counts in counts.items():
    if not year_counts:
        continue
    
    years = sorted(year_counts.keys())
    min_year = years[0]
    max_year = years[-1]
    
    # We should probably fill gaps? 
    # EMA is sensitive to time gaps.
    # Let's fill gaps with 0 from min_year to max_year.
    
    ema = 0
    best_year = -1
    max_ema = -1.0
    
    # Initialize EMA with first year's count
    # Or start from 0?
    # Standard: EMA_0 = Price_0
    
    current_ema = None
    
    # Create full range of years for this symbol
    full_years = range(min_year, 2023) # Go up to 2022 at least
    
    for y in full_years:
        count = year_counts.get(y, 0)
        if current_ema is None:
            current_ema = count
        else:
            current_ema = alpha * count + (1 - alpha) * current_ema
            
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
    if best_year == 2022:
        results.append(sym)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15748739634169971950': 'file_storage/function-call-15748739634169971950.json', 'var_function-call-15365107857304262203': 'file_storage/function-call-15365107857304262203.json', 'var_function-call-14487137383779015423': [{'COUNT(*)': '277813'}], 'var_function-call-14833157841070883006': 'file_storage/function-call-14833157841070883006.json'}

exec(code, env_args)
