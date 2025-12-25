code = """import json
import re

# Load Level 5 CPC symbols
level5_file = locals()['var_function-call-13650408886884758128']
with open(level5_file, 'r') as f:
    level5_data = json.load(f)

# Create a set of Level 5 symbols
level5_symbols = set()
for item in level5_data:
    level5_symbols.add(item['symbol'])

# Check format of Level 5 symbols
print("Sample Level 5 symbols:", list(level5_symbols)[:5])
lengths = set(len(s) for s in level5_symbols)
print("Lengths of Level 5 symbols:", lengths)

# Load Publication Data
pub_file = locals()['var_function-call-17751803970902191593']
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

# Aggregation: { symbol: { year: count } }
# Using sets to ensure distinct patent counts per symbol per year (if needed)
# But simply iterating: 
counts = {}

for record in pub_data:
    f_date = record.get('filing_date')
    cpc_str = record.get('cpc')
    
    if not f_date or not cpc_str:
        continue
        
    # Extract year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Parse CPC
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Extract unique Level 5 symbols for this patent
    patent_symbols = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        # Try to match with level 5 symbols
        # Assumption: Level 5 symbols are prefixes (e.g. Subclasses like "A01B")
        # I need to check if the code *starts with* a Level 5 symbol.
        # Since Level 5 symbols seem to be 4 chars, I'll take the first 4 chars.
        # BUT I should verify if any Level 5 symbol is longer.
        
        # Heuristic: iterate over all lengths present in level5_symbols
        # Optimized: if all are length 4, just take [:4]
        
        # Let's handle generic matching if lengths vary
        # But based on previous print, I expect length 4.
        
        # Start with simple prefix check
        # Assuming most are 4 chars (Subclass)
        # But technically, I should check if the code belongs to the symbol.
        # For Subclasses (4 chars), `A01B...` belongs to `A01B`.
        
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_symbols:
                patent_symbols.add(prefix)
            
    # Update counts
    for sym in patent_symbols:
        if sym not in counts:
            counts[sym] = {}
        counts[sym][year] = counts[sym].get(year, 0) + 1

# Calculate EMA and find best year
alpha = 0.2
result_symbols = []

for sym, year_counts in counts.items():
    if not year_counts:
        continue
        
    years = sorted(year_counts.keys())
    # Fill in missing years with 0? 
    # Usually EMA is calculated over a continuous time series.
    # I should find min and max year.
    min_year = years[0]
    max_year = years[-1]
    
    # Range of years to consider. 
    # If the question implies "filings each year", zero filings should be 0.
    
    ema = 0
    max_ema = -1.0
    best_year = -1
    
    # Initialize EMA with the first year's count (or 0 if started earlier)
    # Let's start from the first year with data for this symbol
    
    # However, to be robust, maybe start from a global min year? 
    # But usually per-series start is fine.
    
    # First value
    # EMA_t1 = Count_t1
    # EMA_t2 = alpha * Count_t2 + (1-alpha) * EMA_t1
    
    current_ema = None
    
    # Iterate through all years from min to max (filling gaps with 0)
    for y in range(min_year, max_year + 1):
        count = year_counts.get(y, 0)
        
        if current_ema is None:
            current_ema = count
        else:
            current_ema = alpha * count + (1 - alpha) * current_ema
            
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
    # Check if best year is 2022
    if best_year == 2022:
        result_symbols.append(sym)

# Format for output
print("__RESULT__:")
print(json.dumps(result_symbols))"""

env_args = {'var_function-call-9665950342090287602': 'file_storage/function-call-9665950342090287602.json', 'var_function-call-9665950342090285761': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-16928258735931206764': [{'COUNT(*)': '277813'}], 'var_function-call-13650408886884758128': 'file_storage/function-call-13650408886884758128.json', 'var_function-call-17751803970902191593': 'file_storage/function-call-17751803970902191593.json'}

exec(code, env_args)
