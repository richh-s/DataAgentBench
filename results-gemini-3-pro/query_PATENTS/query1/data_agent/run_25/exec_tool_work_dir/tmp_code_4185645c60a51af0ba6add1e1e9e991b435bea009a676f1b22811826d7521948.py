code = """import json
import re

# Load data again (reuse keys)
with open(locals()['var_function-call-11747405801204171974'], 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

with open(locals()['var_function-call-6610964282860133498'], 'r') as f:
    pub_data = json.load(f)

counts = {}
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

debug_years = set()

for row in pub_data:
    f_date = row.get('filing_date')
    if not f_date: continue
    full_matches = [m for m in re.findall(r'\b(19|20)\d{2}\b', f_date)]
    if not full_matches: continue
    year = int(full_matches[-1])
    debug_years.add(year)
    
    cpc_json = row.get('cpc')
    if not cpc_json: continue
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                patent_codes.add(prefix)
    
    if year not in counts:
        counts[year] = {}
    for pc in patent_codes:
        counts[year][pc] = counts[year].get(pc, 0) + 1

debug_info = {
    "min_year": min(debug_years) if debug_years else None,
    "max_year": max(debug_years) if debug_years else None,
    "total_cpcs": len(counts.get(2022, {})) if 2022 in counts else 0,
    "sample_years": list(debug_years)[:10]
}

# Check EMA for a few top codes
alpha = 0.2
all_cpcs = set()
for y in counts:
    all_cpcs.update(counts[y].keys())

min_year = min(counts.keys()) if counts else 0
max_year = max(counts.keys()) if counts else 0

cpc_timeline = {cpc: {} for cpc in all_cpcs}
for y in range(min_year, max_year + 1):
    curr_counts = counts.get(y, {})
    for cpc in all_cpcs:
        cpc_timeline[cpc][y] = curr_counts.get(cpc, 0)

best_years_dist = {}

for cpc in list(all_cpcs)[:100]: # Check first 100
    timeline = cpc_timeline[cpc]
    sorted_years = sorted(timeline.keys())
    ema = 0
    max_ema = -1.0
    best_year = -1
    first = True
    for y in sorted_years:
        count = timeline[y]
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        if ema > max_ema:
            max_ema = ema
            best_year = y
    best_years_dist[best_year] = best_years_dist.get(best_year, 0) + 1

print("__RESULT__:")
print(json.dumps({"debug": debug_info, "best_years_sample": best_years_dist}))"""

env_args = {'var_function-call-16849742418819018650': 'file_storage/function-call-16849742418819018650.json', 'var_function-call-2105601753514837134': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_function-call-15924435190051233990': [{'symbol': 'A62B', 'level': '5.0'}, {'symbol': 'A63G', 'level': '5.0'}, {'symbol': 'A63K', 'level': '5.0'}, {'symbol': 'A63B', 'level': '5.0'}, {'symbol': 'C13B50/00', 'level': '7.0'}, {'symbol': 'H04Q2213/296', 'level': '8.0'}, {'symbol': 'A63J', 'level': '5.0'}, {'symbol': 'A63C', 'level': '5.0'}, {'symbol': 'A63D', 'level': '5.0'}, {'symbol': 'A63F', 'level': '5.0'}, {'symbol': 'C25D', 'level': '5.0'}, {'symbol': 'A63H', 'level': '5.0'}, {'symbol': 'A99Z', 'level': '5.0'}, {'symbol': 'B01J', 'level': '5.0'}, {'symbol': 'B01B', 'level': '5.0'}, {'symbol': 'B01D', 'level': '5.0'}, {'symbol': 'B01L', 'level': '5.0'}, {'symbol': 'C13B40/00', 'level': '7.0'}, {'symbol': 'B01F', 'level': '5.0'}, {'symbol': 'B02C', 'level': '5.0'}], 'var_function-call-14819640206453325990': [{'len': '4', 'cnt': '677'}], 'var_function-call-11747405801204171974': 'file_storage/function-call-11747405801204171974.json', 'var_function-call-6610964282860133498': 'file_storage/function-call-6610964282860133498.json', 'var_function-call-14715050367573468631': []}

exec(code, env_args)
