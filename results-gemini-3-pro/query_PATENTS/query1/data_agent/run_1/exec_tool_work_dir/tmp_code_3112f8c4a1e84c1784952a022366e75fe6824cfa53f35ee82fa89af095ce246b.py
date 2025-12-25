code = """import json
import re

# Load CPC Definitions
with open('var_function-call-8775067390743093543.json', 'r') as f:
    cpc_defs = json.load(f)

level_5_codes = set()
for item in cpc_defs:
    try:
        lvl = float(item.get('level', 0))
        if int(lvl) == 5:
            level_5_codes.add(item['symbol'])
    except:
        pass

print(f"DEBUG: Found {len(level_5_codes)} Level 5 CPC codes.")
if len(level_5_codes) > 0:
    print(f"DEBUG: Sample Level 5 code: {list(level_5_codes)[0]}")

# Load Patent Filings
with open('var_function-call-17651004867622027777.json', 'r') as f:
    patents = json.load(f)

counts = {}
year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')

debug_date_count = 0
debug_parsed_years = set()

for p in patents[:1000]: # Check first 1000
    f_date = p.get('filing_date', '')
    match = year_pattern.search(f_date)
    if match:
        debug_date_count += 1
        debug_parsed_years.add(int(match.group(1)))

print(f"DEBUG: Parsed dates in {debug_date_count} out of first 1000 patents.")
print(f"DEBUG: Sample parsed years: {list(debug_parsed_years)[:10]}")

# Check full counts
global_counts = {}
for p in patents:
    f_date = p.get('filing_date', '')
    match = year_pattern.search(f_date)
    if not match: continue
    year = int(match.group(1))
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    for c in cpc_list:
        code = c.get('code')
        if code in level_5_codes:
            if code not in global_counts:
                global_counts[code] = {}
            global_counts[code][year] = global_counts[code].get(year, 0) + 1

print(f"DEBUG: Found {len(global_counts)} Level 5 codes with filings.")
if global_counts:
    sample_code = list(global_counts.keys())[0]
    print(f"DEBUG: Counts for {sample_code}: {global_counts[sample_code]}")
    
    # Check max year
    all_years = set()
    for c in global_counts:
        all_years.update(global_counts[c].keys())
    print(f"DEBUG: Year range: {min(all_years)} to {max(all_years)}")

print("__RESULT__:")
print("DEBUG DONE")"""

env_args = {'var_function-call-6641923460859800772': 'file_storage/function-call-6641923460859800772.json', 'var_function-call-6641923460859799993': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-4289607868665699138': [{'count': '260808'}], 'var_function-call-4289607868665698023': [{'count(*)': '277813'}], 'var_function-call-8775067390743093543': 'file_storage/function-call-8775067390743093543.json', 'var_function-call-17651004867622027777': 'file_storage/function-call-17651004867622027777.json', 'var_function-call-5059798945412610512': []}

exec(code, env_args)
