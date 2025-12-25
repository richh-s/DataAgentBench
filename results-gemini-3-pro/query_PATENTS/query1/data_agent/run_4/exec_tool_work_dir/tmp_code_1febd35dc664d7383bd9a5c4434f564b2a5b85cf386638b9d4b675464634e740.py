code = """import json
import re

path_cpc = locals()['var_function-call-17682530284056883508']
path_patents = locals()['var_function-call-1425838539260044447']

with open(path_cpc, 'r') as f:
    cpc_defs = json.load(f)

level_5_symbols = set()
for item in cpc_defs:
    if 'symbol' in item:
        level_5_symbols.add(item['symbol'])

with open(path_patents, 'r') as f:
    patents = json.load(f)

# Determine matching strategy
sample_symbols = list(level_5_symbols)[:100]
# Check if they look like subclasses (4 chars)
if all(len(s) == 4 for s in sample_symbols):
    match_mode = 'subclass'
else:
    match_mode = 'exact'

counts = {}
year_pattern = re.compile(r'[12]\d{3}')

for p in patents:
    f_date = p.get('filing_date', '')
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    # Take the last year found
    year = int(matches[-1])
    
    # Filter years reasonably (e.g. 1900-2025) to avoid noise
    if year < 1900 or year > 2025:
        continue

    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        if not code:
            continue
            
        target_code = None
        if match_mode == 'subclass':
            if len(code) >= 4:
                target_code = code[:4]
        else:
            target_code = code
            
        if target_code and target_code in level_5_symbols:
            if target_code not in counts:
                counts[target_code] = {}
            counts[target_code][year] = counts[target_code].get(year, 0) + 1

# Calculate EMA
alpha = 0.2
results = []

# Determine global max year to ensure we process up to 2022
all_years = set()
for yc in counts.values():
    all_years.update(yc.keys())

if not all_years:
    limit_year = 2022
else:
    limit_year = max(max(all_years), 2022)

for code, year_counts in counts.items():
    years = sorted(year_counts.keys())
    min_year = years[0]
    
    ema = 0
    first = True
    best_ema = -1.0
    best_year = -1
    
    # Run EMA from min_year to limit_year
    for y in range(min_year, limit_year + 1):
        count = year_counts.get(y, 0)
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        # Track best year
        if ema > best_ema:
            best_ema = ema
            best_year = y
        # We can handle ties (prefer earlier? later?). 
        # Standard: strict inequality keeps the first one.
            
    if best_year == 2022:
        results.append(code)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-17682530284056883508': 'file_storage/function-call-17682530284056883508.json', 'var_function-call-1425838539260044447': 'file_storage/function-call-1425838539260044447.json', 'var_function-call-767001268371460585': [], 'var_function-call-2505620898448165995': 'DEBUG_DONE', 'var_function-call-4017213322786989118': {'sample_level_5': ['G01B', 'G21C', 'E02F', 'F41H', 'A22C', 'A24B', 'H99Z', 'A61Q', 'C21B', 'D05B'], 'match_mode': 'subclass', 'dates_preview': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'codes_preview': [], 'total_matches': 0, 'unique_matched_codes': 0}, 'var_function-call-18026136881528221405': {'cpc_raw_type': "<class 'str'>", 'cpc_raw_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n  ', 'cpc_parsed_type': "<class 'list'>", 'cpc_parsed_len': 38, 'first_item': {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}}, 'var_function-call-13507219659217068897': [], 'var_function-call-930117870880945134': {'min_year': None, 'max_year': None, 'matched_codes_count': 0, 'top_codes': []}, 'var_function-call-12355544548876501546': {'samples': [{'date': 'dated 5th March 2019', 'original': [], 'fixed': [], 'simple': ['2019']}, {'date': 'March the 18th, 2019', 'original': [], 'fixed': [], 'simple': ['2019']}, {'date': '29th March 2019', 'original': [], 'fixed': [], 'simple': ['2019']}, {'date': 'on March 29th, 2019', 'original': [], 'fixed': [], 'simple': ['2019']}, {'date': '2nd April 2019', 'original': [], 'fixed': [], 'simple': ['2019']}]}}

exec(code, env_args)
