code = """import json
import re

path_symbols = locals()['var_function-call-4195696039592522231']
path_patents = locals()['var_function-call-4195696039592525610']

with open(path_symbols, 'r') as f:
    symbols_data = json.load(f)

# Create a set of valid level 5 symbols
valid_symbols = set(item['symbol'] for item in symbols_data)

with open(path_patents, 'r') as f:
    patents_data = json.load(f)

counts = {s: {} for s in valid_symbols}
all_years = set()

# Use the simpler regex that worked
year_pattern = re.compile(r'(19|20)\d{2}')

for row in patents_data:
    filing_date = row.get('filing_date', '')
    match = year_pattern.search(filing_date)
    if not match:
        continue
    year = int(match.group(0))
    all_years.add(year)
    
    cpc_str = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_symbols = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Check if valid
        if len(code) >= 4:
            sub = code[:4]
            if sub in valid_symbols:
                patent_symbols.add(sub)
    
    for s in patent_symbols:
        counts[s][year] = counts[s].get(year, 0) + 1

if not all_years:
    print("__RESULT__:")
    print("[]")
else:
    min_year = min(all_years)
    max_year = max(all_years)
    
    # Ensure range covers up to 2022
    if max_year < 2022:
        max_year = 2022
        
    alpha = 0.2
    results = []
    
    # Process each symbol
    for symbol in valid_symbols:
        # If no data at all for this symbol, skip
        if not counts[symbol]:
            continue
            
        # EMA calculation
        # Initialize EMA.
        # Option A: EMA_0 = count_0 (at min_year).
        # Option B: EMA_0 = 0.
        # "Smoothing factor 0.2" usually implies standard EMA formula.
        # Initialization is often the first observation.
        # I'll use the first year in the global range (min_year) as the starting point.
        
        ema = counts[symbol].get(min_year, 0)
        
        # We need to track the max EMA and the year it occurred
        best_ema = ema
        best_year = min_year
        
        # Iterate through the years
        for y in range(min_year + 1, max_year + 1):
            count = counts[symbol].get(y, 0)
            ema = alpha * count + (1 - alpha) * ema
            
            if ema > best_ema:
                best_ema = ema
                best_year = y
            elif ema == best_ema:
                # Tie-breaking? Usually latest year or keep first.
                # "best year is 2022" implies strict inequality or checking if 2022 is the max.
                # If tied, and one is 2022, is it the best?
                # Usually max() finds the first one. 
                # Let's assume strict greater for update, so earlier year wins ties, unless we want the latest.
                # If we want to check if 2022 is the *highest*, and it's tied with 2021, is it the best?
                # I'll update on strictly greater.
                pass
        
        if best_year == 2022:
            results.append(symbol)

    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-1606092503254054957': ['cpc_definition'], 'var_function-call-1606092503254055080': ['publicationinfo'], 'var_function-call-49990340508428720': [{'count': '677'}], 'var_function-call-49990340508428761': 'file_storage/function-call-49990340508428761.json', 'var_function-call-11885506798250293123': [{'count(*)': '277813'}], 'var_function-call-4195696039592522231': 'file_storage/function-call-4195696039592522231.json', 'var_function-call-4195696039592525610': 'file_storage/function-call-4195696039592525610.json', 'var_function-call-937466644733390942': [], 'var_function-call-6650574053773001958': {'min_year': None, 'max_year': None, 'total_patents_with_year': 0, 'matched_patents': 0, 'sample_counts': {'B27G': {}, 'A62B': {}, 'H02J': {}, 'F21S': {}, 'A46D': {}}}, 'var_function-call-1359902107072342899': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019'], 'var_function-call-9023967366760371923': [{'date': 'dated 5th March 2019', 'match_b': None, 'match_simple': '2019'}, {'date': 'March the 18th, 2019', 'match_b': None, 'match_simple': '2019'}, {'date': '29th March 2019', 'match_b': None, 'match_simple': '2019'}, {'date': 'on March 29th, 2019', 'match_b': None, 'match_simple': '2019'}]}

exec(code, env_args)
