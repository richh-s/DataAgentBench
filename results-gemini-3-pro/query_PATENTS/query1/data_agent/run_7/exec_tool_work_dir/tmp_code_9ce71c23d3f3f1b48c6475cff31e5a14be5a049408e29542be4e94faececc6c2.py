code = """import json
import re

with open(locals()['var_function-call-7168665038669852193'], 'r') as f:
    definitions = json.load(f)
valid_cpcs = set(d['symbol'] for d in definitions)

with open(locals()['var_function-call-12636907471574372890'], 'r') as f:
    patents = json.load(f)

counts = {}
year_pattern = re.compile(r'\b(19|20)\d{2}\b')
all_years = set()

for p in patents:
    cpc = p.get('cpc_l5')
    date_str = p.get('filing_date')
    if not cpc or not date_str: continue
    if cpc not in valid_cpcs: continue
    
    match = year_pattern.search(date_str)
    if match:
        year = int(match.group(0))
        all_years.add(year)
        if cpc not in counts: counts[cpc] = {}
        counts[cpc][year] = counts[cpc].get(year, 0) + 1

# Calculate EMA
alpha = 0.2
cpc_best_year = []

if all_years:
    global_min_year = min(all_years)
    global_max_year = max(all_years)
else:
    global_min_year = 0
    global_max_year = 0

for cpc, year_data in counts.items():
    years = sorted(year_data.keys())
    start_year = years[0] # Start from first available year for this CPC?
    
    # Let's start from start_year
    ema = year_data[start_year]
    best_ema = ema
    best_year = start_year
    
    # Iterate up to global_max_year (assuming we want to check 2022)
    # If the data goes up to 2023, we check up to 2023.
    # If the data stops at 2019, we stop at 2019.
    
    current_max_year = years[-1]
    
    # If we want to strictly emulate "each year", we should iterate year by year.
    for y in range(start_year + 1, global_max_year + 1):
        cnt = year_data.get(y, 0)
        ema = alpha * cnt + (1 - alpha) * ema
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    cpc_best_year.append({"cpc": cpc, "best_year": best_year, "max_ema": best_ema})

# Filter for 2022
results_2022 = [item['cpc'] for item in cpc_best_year if item['best_year'] == 2022]
results_2022.sort()

print("__RESULT__:")
print(json.dumps({
    "global_max_year": global_max_year,
    "count_results_2022": len(results_2022),
    "sample_best_years": cpc_best_year[:5],
    "results_2022": results_2022
}))"""

env_args = {'var_function-call-7168665038669852193': 'file_storage/function-call-7168665038669852193.json', 'var_function-call-10792060600082410393': 'file_storage/function-call-10792060600082410393.json', 'var_function-call-17520737272150592810': [{'symbol': 'C01B', 'level': '5.0'}, {'symbol': 'C', 'level': '2.0'}, {'symbol': 'C01', 'level': '4.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-1418283475394270998': [{'count(*)': '277813'}], 'var_function-call-6985419727303954916': [{'code': 'C01B33/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01B35/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0565', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0562', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01G45/006', 'filing_date': 'dated 5th March 2019'}], 'var_function-call-12636907471574372890': 'file_storage/function-call-12636907471574372890.json', 'var_function-call-6477679623935836888': [], 'var_function-call-1446217851243151572': {'min_year': None, 'max_year': None, 'sample_counts': []}, 'var_function-call-16194099183484994991': {'sample_defs': ['A01H', 'A01F', 'A01C', 'A01G', 'A23J', 'A01N', 'A01P', 'A01D', 'A01L', 'A01K'], 'sample_patents': ['C01B', 'H01M', 'C01G', 'C01P', 'Y02E', 'F16H', 'B29C', 'C08J', 'B32B', 'C09D'], 'patents_count': 544204, 'defs_count': 677}, 'var_function-call-8791923892856555197': {'intersection_count': 669, 'sample_intersection': ['B27D', 'A63H', 'A01D', 'C09G', 'E01F', 'B60J', 'F42B', 'D01C', 'B27G', 'A23G'], 'is_C01B_valid': True, 'is_H01M_valid': True}}

exec(code, env_args)
