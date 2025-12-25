code = """import json
import re

# Load paths
l5_path = locals()['var_function-call-15361020114366599726']
pubs_path = locals()['var_function-call-16075540632948786396']

with open(l5_path, 'r') as f:
    l5_data = json.load(f)
l5_symbols = set(item['symbol'] for item in l5_data)
l5_lengths = set(len(s) for s in l5_symbols)

with open(pubs_path, 'r') as f:
    pubs = json.load(f)

years = []
matched_symbols_count = 0
total_processed = 0

year_pattern = re.compile(r'\b((?:19|20)\d{2})\b')

debug_counts = {}

for p in pubs[:10000]: # Check first 10k for speed
    f_date = p.get('filing_date', '')
    if not isinstance(f_date, str):
        continue
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(1))
    years.append(year)
    total_processed += 1
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    if not isinstance(cpc_list, list):
        continue

    for entry in cpc_list:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in l5_symbols:
                matched_symbols_count += 1
                debug_counts[prefix] = debug_counts.get(prefix, 0) + 1

print("__RESULT__:")
debug_info = {
    "l5_lengths": list(l5_lengths),
    "min_year": min(years) if years else None,
    "max_year": max(years) if years else None,
    "total_processed": total_processed,
    "matched_symbols_count": matched_symbols_count,
    "sample_matched_counts": {k: debug_counts[k] for k in list(debug_counts)[:5]}
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-15361020114366599726': 'file_storage/function-call-15361020114366599726.json', 'var_function-call-15361020114366601035': [{'count(*)': '277813'}], 'var_function-call-16075540632948786396': 'file_storage/function-call-16075540632948786396.json', 'var_function-call-8499156135441771268': []}

exec(code, env_args)
