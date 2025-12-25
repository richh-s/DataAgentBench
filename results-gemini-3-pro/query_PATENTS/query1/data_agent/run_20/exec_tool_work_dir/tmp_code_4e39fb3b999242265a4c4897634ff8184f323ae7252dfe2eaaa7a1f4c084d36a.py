code = """import json
import re

# Load level 5 codes
with open(locals()['var_function-call-5770235724509795009'], 'r') as f:
    l5_data = json.load(f)
valid_l5 = set(item['symbol'] for item in l5_data)

# Process publications
counts = {} # (code, year) -> count
min_year_global = 3000
max_year_global = 0

with open(locals()['var_function-call-499717155122339469'], 'r') as f:
    data = json.load(f)

for row in data:
    fdate = row.get('filing_date', '')
    cpc_json = row.get('cpc', '[]')
    
    # Extract year
    match = re.search(r'\b(19|20)\d{2}\b', fdate)
    if not match:
        continue
    year = int(match.group(0))
    
    if year < 1900 or year > 2024:
        continue
        
    min_year_global = min(min_year_global, year)
    max_year_global = max(max_year_global, year)
    
    # Extract CPC
    try:
        cpcs = json.loads(cpc_json)
    except:
        continue
        
    seen_codes = set()
    for entry in cpcs:
        code = entry.get('code', '')
        if len(code) >= 4:
            l5_code = code[:4]
            if l5_code in valid_l5:
                seen_codes.add(l5_code)
    
    for c in seen_codes:
        if (c, year) not in counts:
            counts[(c, year)] = 0
        counts[(c, year)] += 1

# Calculate EMA and find best year
alpha = 0.2
final_codes = []
all_codes = set(k[0] for k in counts.keys())

# Ensure we cover up to 2022 if max_year_global < 2022 (unlikely but possible)
max_year_check = max(max_year_global, 2022)

for code in all_codes:
    # Get years this code exists
    code_years = [y for c, y in counts.keys() if c == code]
    if not code_years:
        continue
    
    start_year = min(code_years)
    # End at max_year_check to compare fairly up to 2022 and beyond if data exists
    # If the dataset goes up to 2023 or 2024, we should consider those.
    # The user asks for "best year is 2022". 
    # If EMA in 2023 is higher, then best year is 2023, so it shouldn't be included.
    end_year = max_year_check 
    
    ema = 0
    first = True
    best_ema = -1.0
    best_y = -1
    
    # Iterate
    for y in range(start_year, end_year + 1):
        count = counts.get((code, y), 0)
        
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        # Track max EMA
        # Use >= to update to later year if equal? "best year". Usually first or last.
        # But float comparison exact match is rare.
        if ema > best_ema:
            best_ema = ema
            best_y = y
            
    if best_y == 2022:
        final_codes.append(code)

final_codes.sort()
print("__RESULT__:")
print(json.dumps(final_codes))"""

env_args = {'var_function-call-8960863123887240605': 'file_storage/function-call-8960863123887240605.json', 'var_function-call-9121606955539458114': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-14205884976276555357': [{'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-8893913274727555308': [{'symbol': 'A62B', 'level': '5.0'}, {'symbol': 'A63G', 'level': '5.0'}, {'symbol': 'A63K', 'level': '5.0'}, {'symbol': 'A63B', 'level': '5.0'}, {'symbol': 'A63J', 'level': '5.0'}, {'symbol': 'A63C', 'level': '5.0'}, {'symbol': 'A63D', 'level': '5.0'}, {'symbol': 'A63F', 'level': '5.0'}, {'symbol': 'C25D', 'level': '5.0'}, {'symbol': 'A63H', 'level': '5.0'}], 'var_function-call-12910028673437125087': [{'symbol': 'C01B', 'level': '5.0'}], 'var_function-call-5759197899414802183': [{'count(*)': '277813'}], 'var_function-call-5770235724509795009': 'file_storage/function-call-5770235724509795009.json', 'var_function-call-499717155122339469': 'file_storage/function-call-499717155122339469.json'}

exec(code, env_args)
