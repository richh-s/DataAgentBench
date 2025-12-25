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
    if not fdate: continue
    
    # Extract year: search for 4 digits
    match = re.search(r'\d{4}', fdate)
    if not match:
        continue
    year = int(match.group(0))
    
    if year < 1900 or year > 2024:
        continue
        
    min_year_global = min(min_year_global, year)
    max_year_global = max(max_year_global, year)
    
    cpc_str = row.get('cpc', '[]')
    try:
        cpcs = json.loads(cpc_str)
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

# Calculate EMA
alpha = 0.2
final_codes = []
best_years_dist = {}

all_codes = set(k[0] for k in counts.keys())
# Range: from min_year_global to max_year_global?
# Or per code?
# "Identify the CPC technology areas with the highest exponential moving average of patent filings each year"
# This suggests we compare EMAs in each year.
# But then "whose best year is 2022".
# This implies we look at the history of a code and find its peak.
# I will use the code's data range, but extend to 2022 if the data goes that far.

# Wait, if max_year_global is 2020, then "best year 2022" is impossible.
# Let's verify max_year_global first.

if not all_codes:
    result = {"error": "No codes found", "max_year_global": max_year_global}
else:
    for code in all_codes:
        code_years = [y for c, y in counts.keys() if c == code]
        start_year = min(code_years)
        # End year: we should go up to at least 2022 if possible, or max_year_global.
        # If max_year_global < 2022, we can't find 2022.
        end_year = max(max_year_global, 2022) 
        
        # If data only goes to 2019, 2022 will have 0 counts -> EMA decays.
        # Unless the user implies 2022 is in the dataset.
        
        ema = 0
        first = True
        best_ema = -1.0
        best_y = -1
        
        # We must iterate sequentially
        for y in range(start_year, end_year + 1):
            count = counts.get((code, y), 0)
            if first:
                ema = count
                first = False
            else:
                ema = alpha * count + (1 - alpha) * ema
            
            if ema > best_ema:
                best_ema = ema
                best_y = y
        
        best_years_dist[best_y] = best_years_dist.get(best_y, 0) + 1
        
        if best_y == 2022:
            final_codes.append(code)
    
    final_codes.sort()
    result = final_codes
    # debug info
    # result = {"codes": final_codes, "max_year": max_year_global, "best_years_dist": best_years_dist}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8960863123887240605': 'file_storage/function-call-8960863123887240605.json', 'var_function-call-9121606955539458114': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-14205884976276555357': [{'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-8893913274727555308': [{'symbol': 'A62B', 'level': '5.0'}, {'symbol': 'A63G', 'level': '5.0'}, {'symbol': 'A63K', 'level': '5.0'}, {'symbol': 'A63B', 'level': '5.0'}, {'symbol': 'A63J', 'level': '5.0'}, {'symbol': 'A63C', 'level': '5.0'}, {'symbol': 'A63D', 'level': '5.0'}, {'symbol': 'A63F', 'level': '5.0'}, {'symbol': 'C25D', 'level': '5.0'}, {'symbol': 'A63H', 'level': '5.0'}], 'var_function-call-12910028673437125087': [{'symbol': 'C01B', 'level': '5.0'}], 'var_function-call-5759197899414802183': [{'count(*)': '277813'}], 'var_function-call-5770235724509795009': 'file_storage/function-call-5770235724509795009.json', 'var_function-call-499717155122339469': 'file_storage/function-call-499717155122339469.json', 'var_function-call-8433321875573929793': [], 'var_function-call-10247650089982872301': {'error': 'No years found'}, 'var_function-call-5869860868040122757': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019'], 'var_function-call-14270117871806660202': ['2019', '2019', '2019', '2019']}

exec(code, env_args)
