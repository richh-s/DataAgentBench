code = """import json
import re

l5_path = locals()['var_function-call-15361020114366599726']
pubs_path = locals()['var_function-call-16075540632948786396']

with open(l5_path, 'r') as f:
    l5_data = json.load(f)
l5_symbols = set(item['symbol'] for item in l5_data)

with open(pubs_path, 'r') as f:
    pubs = json.load(f)

counts = {}
year_pattern = re.compile(r'(\d{4})')

for p in pubs:
    f_date = p.get('filing_date', '')
    if not isinstance(f_date, str):
        continue
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(1))
    
    # Filter reasonable years to avoid noise
    if year < 1900 or year > 2025:
        continue
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    if not isinstance(cpc_list, list):
        continue

    patent_symbols = set()
    for entry in cpc_list:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in l5_symbols:
                patent_symbols.add(prefix)
    
    for sym in patent_symbols:
        if sym not in counts:
            counts[sym] = {}
        counts[sym][year] = counts[sym].get(year, 0) + 1

alpha = 0.2
result_symbols = []
debug_best_years = {}

for sym, year_counts in counts.items():
    if not year_counts:
        continue
        
    min_year = min(year_counts.keys())
    max_year = max(year_counts.keys())
    
    # Range: from min_year to max(max_year, 2022)
    # We want to check if 2022 is the best year.
    # If the data stops at 2021, we assume 0 for 2022.
    # The EMA will decay. It's unlikely to be the best year if count is 0, unless previous EMA was high and decay is slow?
    # No, if count is 0, EMA decreases. So best year won't be 2022 if it was 2021.
    # But if max_year is 2022, we have data.
    
    end_year = max(max_year, 2022)
    years = sorted(range(min_year, end_year + 1))
    
    ema = year_counts.get(min_year, 0)
    best_ema = ema
    best_year = min_year
    
    for y in years[1:]:
        val = year_counts.get(y, 0)
        ema = alpha * val + (1 - alpha) * ema
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    debug_best_years[best_year] = debug_best_years.get(best_year, 0) + 1
    
    if best_year == 2022:
        result_symbols.append(sym)

print("__RESULT__:")
# print(f"DEBUG: Best year distribution: {debug_best_years}")
print(json.dumps(result_symbols))"""

env_args = {'var_function-call-15361020114366599726': 'file_storage/function-call-15361020114366599726.json', 'var_function-call-15361020114366601035': [{'count(*)': '277813'}], 'var_function-call-16075540632948786396': 'file_storage/function-call-16075540632948786396.json', 'var_function-call-8499156135441771268': [], 'var_function-call-7188278383105203727': {'l5_lengths': [4], 'min_year': None, 'max_year': None, 'total_processed': 0, 'matched_symbols_count': 0, 'sample_matched_counts': {}}, 'var_function-call-15565508724976364663': [{'raw_date': 'dated 5th March 2019', 'match': 'None'}, {'raw_date': 'March the 18th, 2019', 'match': 'None'}, {'raw_date': '29th March 2019', 'match': 'None'}, {'raw_date': 'on March 29th, 2019', 'match': 'None'}, {'raw_date': '2nd April 2019', 'match': 'None'}, {'raw_date': 'on April 8th, 2019', 'match': 'None'}, {'raw_date': '15th April 2019', 'match': 'None'}, {'raw_date': 'April 19th, 2019', 'match': 'None'}, {'raw_date': '2019, April 24th', 'match': 'None'}, {'raw_date': 'April 26th, 2019', 'match': 'None'}], 'var_function-call-11758929023964371950': [{'raw_date_repr': "'dated 5th March 2019'", 'match': '2019'}, {'raw_date_repr': "'March the 18th, 2019'", 'match': '2019'}, {'raw_date_repr': "'29th March 2019'", 'match': '2019'}, {'raw_date_repr': "'on March 29th, 2019'", 'match': '2019'}, {'raw_date_repr': "'2nd April 2019'", 'match': '2019'}]}

exec(code, env_args)
