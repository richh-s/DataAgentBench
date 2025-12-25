code = """import json
import re
from collections import defaultdict

level5_file = locals()['var_function-call-4744927068419664464']
pub_file = locals()['var_function-call-4744927068419665303']

with open(level5_file, 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

with open(pub_file, 'r') as f:
    pub_data = json.load(f)

counts = defaultdict(lambda: defaultdict(int))
global_years = set()
year_pattern = re.compile(r'\b(?:19|20)\d{2}\b')

debug_dates = []
debug_cpcs = []
matches_count = 0

for i, row in enumerate(pub_data):
    f_date = row.get('filing_date')
    if i < 5:
        debug_dates.append(f_date)
        
    if not f_date:
        continue
    
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    year = int(matches[-1])
    global_years.add(year)
    matches_count += 1
    
    cpc_str = row.get('cpc')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue

    if i < 5:
        debug_cpcs.append([x.get('code') for x in cpc_list])

    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                counts[prefix][year] += 1

print('__RESULT__:')
debug_info = {
    "min_year": min(global_years) if global_years else None,
    "max_year": max(global_years) if global_years else None,
    "total_records": len(pub_data),
    "records_with_date_match": matches_count,
    "unique_cpcs_found": len(counts),
    "sample_dates": debug_dates,
    "sample_cpcs": debug_cpcs,
    "sample_level5": list(level5_codes)[:10],
    "sample_counts": {k: dict(v) for k, v in list(counts.items())[:2]}
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-18281922881261155290': ['publicationinfo'], 'var_function-call-18281922881261156991': ['cpc_definition'], 'var_function-call-3853867713196752715': 'file_storage/function-call-3853867713196752715.json', 'var_function-call-3853867713196752716': [{'count': '277813'}], 'var_function-call-3853867713196752717': [{'count': '677'}], 'var_function-call-4744927068419664464': 'file_storage/function-call-4744927068419664464.json', 'var_function-call-4744927068419665303': 'file_storage/function-call-4744927068419665303.json', 'var_function-call-4885472280726247165': []}

exec(code, env_args)
