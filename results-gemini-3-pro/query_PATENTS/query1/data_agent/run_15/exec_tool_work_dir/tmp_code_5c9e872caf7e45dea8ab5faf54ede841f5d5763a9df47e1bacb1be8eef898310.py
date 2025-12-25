code = """import json
import re
import pandas as pd

# Load level 5 symbols
with open('var_function-call-4195696039592522231.json', 'r') as f:
    symbols_data = json.load(f)

valid_symbols = set(item['symbol'] for item in symbols_data)

# Load patent data
with open('var_function-call-4195696039592525610.json', 'r') as f:
    patents_data = json.load(f)

# Counts storage
counts = {s: {} for s in valid_symbols}
all_years = set()

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for row in patents_data:
    # Extract year
    filing_date = row.get('filing_date', '')
    match = year_pattern.search(filing_date)
    if not match:
        continue
    year = int(match.group(0))
    all_years.add(year)
    
    # Extract CPC symbols
    cpc_str = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Identify unique valid symbols for this patent
    patent_symbols = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Check if the code starts with any valid symbol
        # Since valid_symbols seem to be 4 chars (Subclass), we check code[:4]
        # But we must be careful if valid_symbols have different lengths.
        # Based on preview, they are 4 chars.
        # Let's check generally.
        if len(code) >= 4:
            sub = code[:4]
            if sub in valid_symbols:
                patent_symbols.add(sub)
    
    # Update counts
    for s in patent_symbols:
        counts[s][year] = counts[s].get(year, 0) + 1

# Prepare for EMA calculation
if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(all_years)
max_year = max(all_years)
years = sorted(list(range(min_year, max_year + 1)))

alpha = 0.2
results = []

for symbol in valid_symbols:
    if not counts[symbol]:
        continue
        
    ema = 0
    best_year = None
    max_ema = -1
    
    # Initialize EMA with the count of the first year in the range?
    # Or start from the first year where data exists?
    # Standard EMA usually starts with the first value.
    # We will iterate through all years in the global range to ensure comparable timelines?
    # Or just the years for the symbol?
    # "each year" implies a continuous timeline. 
    # Let's iterate from min_year to max_year.
    
    # Initialization:
    # If using the first year of data:
    # ema = counts[symbol].get(min_year, 0)
    # Then iterate from min_year + 1
    
    ema = counts[symbol].get(min_year, 0)
    
    # Track best year
    # We should consider the EMA of the first year too.
    if ema > max_ema:
        max_ema = ema
        best_year = min_year
        
    for y in range(min_year + 1, max_year + 1):
        count = counts[symbol].get(y, 0)
        ema = alpha * count + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    if best_year == 2022:
        results.append(symbol)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1606092503254054957': ['cpc_definition'], 'var_function-call-1606092503254055080': ['publicationinfo'], 'var_function-call-49990340508428720': [{'count': '677'}], 'var_function-call-49990340508428761': 'file_storage/function-call-49990340508428761.json', 'var_function-call-11885506798250293123': [{'count(*)': '277813'}], 'var_function-call-4195696039592522231': 'file_storage/function-call-4195696039592522231.json', 'var_function-call-4195696039592525610': 'file_storage/function-call-4195696039592525610.json'}

exec(code, env_args)
