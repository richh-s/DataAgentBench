code = """import json
import re

level5_file_path = locals()['var_function-call-17141822990107305310']
patent_file_path = locals()['var_function-call-12961292587599410676']

with open(level5_file_path, 'r') as f:
    level5_data = json.load(f)

level5_codes = set()
for item in level5_data:
    if 'symbol' in item:
        level5_codes.add(item['symbol'])

with open(patent_file_path, 'r') as f:
    patent_data = json.load(f)

def extract_year(date_str):
    if not date_str:
        return None
    # Removed \b to be more robust
    match = re.search(r'(19|20)\d{2}', date_str)
    if match:
        return int(match.group(0))
    return None

counts = {}
years = set()
lengths = set(len(c) for c in level5_codes)
sorted_lengths = sorted(list(lengths), reverse=True)

for row in patent_data:
    f_date = row.get('filing_date')
    year = extract_year(f_date)
    if year is None:
        continue
    
    years.add(year)
    
    cpc_json = row.get('cpc')
    if not cpc_json:
        continue
    
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    patent_codes = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        if not code:
            continue
        
        # Match level 5
        for l in sorted_lengths:
            if len(code) >= l:
                prefix = code[:l]
                if prefix in level5_codes:
                    patent_codes.add(prefix)
                    break 

    for p_code in patent_codes:
        if p_code not in counts:
            counts[p_code] = {}
        counts[p_code][year] = counts[p_code].get(year, 0) + 1

if not years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(years)
max_year = max(years)

# Ensure 2022 is in range. If max_year < 2022, result is empty.
if max_year < 2022:
    print("__RESULT__:")
    print("[]")
    exit()

alpha = 0.2
results = []

for code, year_counts in counts.items():
    ema = 0
    best_ema = -1.0
    best_year = -1
    initialized = False
    
    for y in range(min_year, max_year + 1):
        val = year_counts.get(y, 0)
        
        if not initialized:
            if val > 0:
                ema = float(val)
                initialized = True
                best_ema = ema
                best_year = y
            # Else remains uninitialized
        else:
            ema = (val * alpha) + (ema * (1 - alpha))
            if ema > best_ema:
                best_ema = ema
                best_year = y
            elif ema == best_ema:
                # Tie-breaking? Usually earliest or latest?
                # "best year" usually implies the peak.
                # If equal, does it matter? Maybe the later one?
                # Let's keep the first one found (earliest) to be conservative, 
                # or strictly greater `>`.
                pass

    if best_year == 2022:
        results.append(code)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16843621957294656966': 'file_storage/function-call-16843621957294656966.json', 'var_function-call-6909709033955517173': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-17141822990107305310': 'file_storage/function-call-17141822990107305310.json', 'var_function-call-12961292587599410676': 'file_storage/function-call-12961292587599410676.json', 'var_function-call-15227026791012080898': [], 'var_function-call-11403077282351278082': {'min_year': None, 'max_year': None, 'matched_codes_sample_count': 2685110, 'sample_dates': [['dated 5th March 2019', None], ['March the 18th, 2019', None], ['29th March 2019', None], ['on March 29th, 2019', None], ['2nd April 2019', None], ['on April 8th, 2019', None], ['15th April 2019', None], ['April 19th, 2019', None], ['2019, April 24th', None], ['April 26th, 2019', None]], 'level5_sample': ['G01N', 'C12N', 'E06C', 'C10L', 'B82Y']}}

exec(code, env_args)
