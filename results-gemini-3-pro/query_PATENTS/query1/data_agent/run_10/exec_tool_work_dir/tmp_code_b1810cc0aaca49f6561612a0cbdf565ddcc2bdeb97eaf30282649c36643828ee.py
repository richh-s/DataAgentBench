code = """import json
import re
from collections import defaultdict

# Load level 5 symbols
with open(locals()['var_function-call-7269545379291600604'], 'r') as f:
    level5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_data)

# Load publications
with open(locals()['var_function-call-7269545379291602853'], 'r') as f:
    publications = json.load(f)

# Regex for year
year_pattern = re.compile(r'(19|20)\d{2}')

counts = defaultdict(lambda: defaultdict(int))

for pub in publications:
    # Extract year
    fdate = pub.get('filing_date', '')
    if not fdate:
        continue
    match = year_pattern.search(fdate)
    if not match:
        continue
    year = int(match.group(0))
    
    # Extract CPC codes
    cpc_str = pub.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    seen_symbols = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Check first 4 chars
        if len(code) >= 4:
            candidate = code[:4]
            if candidate in level5_symbols:
                seen_symbols.add(candidate)
    
    for s in seen_symbols:
        counts[s][year] += 1

final_results = []
alpha = 0.2

for symbol, year_data in counts.items():
    years = sorted(year_data.keys())
    if not years:
        continue
        
    min_year = years[0]
    max_year = years[-1]
    
    # We iterate year by year to simulate EMA correctly
    # If there are gaps in years, the count is 0.
    
    ema = year_data[min_year]
    max_ema = ema
    best_year = min_year
    
    current_ema = ema
    
    # We should cover up to at least 2022 if the data goes that far
    # Or just up to the max year present in data for that symbol?
    # Usually "best year" implies comparison over the observed period.
    # If data for a symbol ends in 2020, its best year can't be 2022.
    # If data extends to 2022 or 2023, we check 2022.
    
    # However, if other symbols have data up to 2023, we should consistent.
    # Let's just run up to the max year observed for this symbol.
    
    for y in range(min_year + 1, max_year + 1):
        count = year_data.get(y, 0)
        current_ema = alpha * count + (1 - alpha) * current_ema
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
    if best_year == 2022:
        final_results.append(symbol)

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-2156360617671993543': 'file_storage/function-call-2156360617671993543.json', 'var_function-call-2156360617671993474': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-13197801515955793315': [{'count(*)': '277813'}], 'var_function-call-13197801515955789834': [{'count': '677'}], 'var_function-call-7269545379291600604': 'file_storage/function-call-7269545379291600604.json', 'var_function-call-7269545379291602853': 'file_storage/function-call-7269545379291602853.json', 'var_function-call-5018208914705499515': [], 'var_function-call-5189175782737133234': {'lengths': [4], 'sample_symbols': ['A01H', 'A01F', 'A01C', 'A01G', 'A23J', 'A01N', 'A01P', 'A01D', 'A01L', 'A01K'], 'sample_years': [], 'max_year_sample': None, 'match_count_first_100': 100}, 'var_function-call-15279429834221810901': {'dates_preview': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019'], 'regex_test': 'No match'}}

exec(code, env_args)
