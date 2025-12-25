code = """import json
import re

pubs_path = locals()['var_function-call-16075540632948786396']
with open(pubs_path, 'r') as f:
    pubs = json.load(f)

print("__RESULT__:")
debug_list = []
year_pattern = re.compile(r'\b((?:19|20)\d{2})\b')

for p in pubs[:10]:
    f_date = p.get('filing_date', 'MISSING')
    match = year_pattern.search(str(f_date))
    debug_list.append({
        "raw_date": f_date,
        "match": match.group(1) if match else "None"
    })

print(json.dumps(debug_list))"""

env_args = {'var_function-call-15361020114366599726': 'file_storage/function-call-15361020114366599726.json', 'var_function-call-15361020114366601035': [{'count(*)': '277813'}], 'var_function-call-16075540632948786396': 'file_storage/function-call-16075540632948786396.json', 'var_function-call-8499156135441771268': [], 'var_function-call-7188278383105203727': {'l5_lengths': [4], 'min_year': None, 'max_year': None, 'total_processed': 0, 'matched_symbols_count': 0, 'sample_matched_counts': {}}}

exec(code, env_args)
