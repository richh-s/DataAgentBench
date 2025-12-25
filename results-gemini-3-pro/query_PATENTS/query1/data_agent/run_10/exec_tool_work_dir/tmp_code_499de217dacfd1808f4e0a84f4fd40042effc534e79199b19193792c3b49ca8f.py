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
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

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
        # Check if code matches any level 5 symbol
        # Assuming level 5 symbols are prefixes like "A01B" (4 chars)
        # We try to match the prefix.
        # But wait, some level 5 symbols might be different length?
        # Let's check the length of symbols in level5_symbols.
        # Based on preview, they are 4 chars.
        # But to be safe, we can try to find if the code starts with any level 5 symbol.
        # However, checking against 677 symbols for every code is slow.
        # Optimization: keys in level 5 are likely 4 chars.
        # Let's assume standard CPC Subclass is 4 chars.
        candidate = code[:4]
        if candidate in level5_symbols:
            seen_symbols.add(candidate)
    
    for s in seen_symbols:
        counts[s][year] += 1

# Calculate EMA and find best year
final_results = []
alpha = 0.2

for symbol, year_data in counts.items():
    if not year_data:
        continue
        
    years = sorted(year_data.keys())
    min_year = years[0]
    max_year = years[-1]
    
    # We might need to go up to 2022 even if data stops earlier? 
    # Or just consider the years present?
    # "whose best year is 2022" implies 2022 must be in the range considered.
    # If max_year < 2022, it can't be 2022.
    # But if data exists for 2023, we should check that too.
    # We'll just iterate from min_year to max_year.
    
    ema = year_data[min_year] # Initialize with first year count
    max_ema = ema
    best_year = min_year
    
    current_ema = ema
    
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

env_args = {'var_function-call-2156360617671993543': 'file_storage/function-call-2156360617671993543.json', 'var_function-call-2156360617671993474': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-13197801515955793315': [{'count(*)': '277813'}], 'var_function-call-13197801515955789834': [{'count': '677'}], 'var_function-call-7269545379291600604': 'file_storage/function-call-7269545379291600604.json', 'var_function-call-7269545379291602853': 'file_storage/function-call-7269545379291602853.json'}

exec(code, env_args)
