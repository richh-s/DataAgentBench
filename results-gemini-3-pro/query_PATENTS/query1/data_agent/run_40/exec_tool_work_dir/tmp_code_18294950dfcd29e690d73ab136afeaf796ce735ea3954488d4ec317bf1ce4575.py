code = """import json
import re

pubs_path = locals()['var_function-call-16075540632948786396']
with open(pubs_path, 'r') as f:
    pubs = json.load(f)

print("__RESULT__:")
debug_list = []
# Simpler regex
simple_pattern = re.compile(r'(\d{4})')

for p in pubs[:5]:
    f_date = p.get('filing_date', '')
    match = simple_pattern.search(str(f_date))
    debug_list.append({
        "raw_date_repr": repr(f_date),
        "match": match.group(1) if match else "None"
    })

print(json.dumps(debug_list))"""

env_args = {'var_function-call-15361020114366599726': 'file_storage/function-call-15361020114366599726.json', 'var_function-call-15361020114366601035': [{'count(*)': '277813'}], 'var_function-call-16075540632948786396': 'file_storage/function-call-16075540632948786396.json', 'var_function-call-8499156135441771268': [], 'var_function-call-7188278383105203727': {'l5_lengths': [4], 'min_year': None, 'max_year': None, 'total_processed': 0, 'matched_symbols_count': 0, 'sample_matched_counts': {}}, 'var_function-call-15565508724976364663': [{'raw_date': 'dated 5th March 2019', 'match': 'None'}, {'raw_date': 'March the 18th, 2019', 'match': 'None'}, {'raw_date': '29th March 2019', 'match': 'None'}, {'raw_date': 'on March 29th, 2019', 'match': 'None'}, {'raw_date': '2nd April 2019', 'match': 'None'}, {'raw_date': 'on April 8th, 2019', 'match': 'None'}, {'raw_date': '15th April 2019', 'match': 'None'}, {'raw_date': 'April 19th, 2019', 'match': 'None'}, {'raw_date': '2019, April 24th', 'match': 'None'}, {'raw_date': 'April 26th, 2019', 'match': 'None'}]}

exec(code, env_args)
