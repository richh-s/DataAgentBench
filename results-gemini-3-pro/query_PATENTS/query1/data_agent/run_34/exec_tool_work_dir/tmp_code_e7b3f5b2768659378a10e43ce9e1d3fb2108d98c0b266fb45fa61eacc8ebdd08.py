code = """import json
import re

# Access file paths from local variables
# These variables contain the file path strings
level5_file_path = locals()['var_function-call-17141822990107305310']
patent_file_path = locals()['var_function-call-12961292587599410676']

# Load Level 5 CPC codes
with open(level5_file_path, 'r') as f:
    level5_data = json.load(f)

level5_codes = set()
for item in level5_data:
    if 'symbol' in item:
        level5_codes.add(item['symbol'])

# Load Patent Data
with open(patent_file_path, 'r') as f:
    patent_data = json.load(f)

def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

counts = {}
years = set()

lengths = set(len(c) for c in level5_codes)

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
        
        # Check against level 5 codes
        # Priority to longest match? Or just any match?
        # Assuming distinct hierarchy, matching longest prefix in the set is safest.
        # Check lengths descending
        sorted_lengths = sorted(list(lengths), reverse=True)
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

alpha = 0.2
results = []

for code, year_counts in counts.items():
    ema = 0
    best_ema = -1.0 # Use float
    best_year = -1
    initialized = False
    
    # Iterate through all years to handle smoothing correctly over time gaps
    for y in range(min_year, max_year + 1):
        val = year_counts.get(y, 0)
        
        if not initialized:
            if val > 0:
                ema = float(val)
                initialized = True
                if ema > best_ema:
                    best_ema = ema
                    best_year = y
        else:
            ema = (val * alpha) + (ema * (1 - alpha))
            if ema > best_ema:
                best_ema = ema
                best_year = y
    
    # Check if best year is 2022
    if best_year == 2022:
        results.append(code)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16843621957294656966': 'file_storage/function-call-16843621957294656966.json', 'var_function-call-6909709033955517173': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-17141822990107305310': 'file_storage/function-call-17141822990107305310.json', 'var_function-call-12961292587599410676': 'file_storage/function-call-12961292587599410676.json'}

exec(code, env_args)
