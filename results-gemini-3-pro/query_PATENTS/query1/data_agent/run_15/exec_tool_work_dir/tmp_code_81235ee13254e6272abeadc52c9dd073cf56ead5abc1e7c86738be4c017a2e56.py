code = """import json
import re

# Access file paths from variables
path_symbols = locals()['var_function-call-4195696039592522231']
path_patents = locals()['var_function-call-4195696039592525610']

# Load level 5 symbols
with open(path_symbols, 'r') as f:
    symbols_data = json.load(f)

valid_symbols = set(item['symbol'] for item in symbols_data)

# Load patent data
with open(path_patents, 'r') as f:
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
else:
    min_year = min(all_years)
    max_year = max(all_years)
    # Ensure 2022 is in range if not present (though prompt implies it should be)
    if 2022 > max_year:
        max_year = 2022
    
    alpha = 0.2
    results = []

    for symbol in valid_symbols:
        # Check if symbol has any data
        if not counts[symbol]:
            continue
            
        ema = counts[symbol].get(min_year, 0)
        best_year = min_year
        max_ema = ema
        
        # Calculate EMA for subsequent years
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
