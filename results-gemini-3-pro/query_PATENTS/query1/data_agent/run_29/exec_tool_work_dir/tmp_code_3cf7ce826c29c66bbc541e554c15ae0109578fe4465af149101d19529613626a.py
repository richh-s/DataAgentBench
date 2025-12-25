code = """import json
import re

level5_file = locals()['var_function-call-13650408886884758128']
pub_file = locals()['var_function-call-17751803970902191593']

with open(level5_file, 'r') as f:
    level5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_data)

print(f"Level 5 Sample: {list(level5_symbols)[:5]}")
print(f"Level 5 Lengths: {set(len(s) for s in level5_symbols)}")

with open(pub_file, 'r') as f:
    pub_data = json.load(f)

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

years_found = set()
matched_records = 0
total_records = len(pub_data)

counts = {} # sym -> year -> count

for i, record in enumerate(pub_data):
    f_date = record.get('filing_date')
    cpc_str = record.get('cpc')
    
    if not f_date or not cpc_str:
        continue
    
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    years_found.add(year)
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    for entry in cpc_list:
        code = entry.get('code', '')
        # Check matching
        # Try 4 chars
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_symbols:
                if prefix not in counts:
                    counts[prefix] = {}
                counts[prefix][year] = counts[prefix].get(year, 0) + 1
                matched_records += 1

print(f"Years found: {sorted(list(years_found))}")
print(f"Total records processed: {total_records}")
print(f"Records with valid year: {len(years_found)}") # Wait, this is count of unique years
print(f"Matched CPC entries: {matched_records}")
print(f"Unique symbols matched: {len(counts)}")

if counts:
    sample_sym = list(counts.keys())[0]
    print(f"Sample counts for {sample_sym}: {counts[sample_sym]}")

print("__RESULT__:")
print("done")"""

env_args = {'var_function-call-9665950342090287602': 'file_storage/function-call-9665950342090287602.json', 'var_function-call-9665950342090285761': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-16928258735931206764': [{'COUNT(*)': '277813'}], 'var_function-call-13650408886884758128': 'file_storage/function-call-13650408886884758128.json', 'var_function-call-17751803970902191593': 'file_storage/function-call-17751803970902191593.json', 'var_function-call-2714896827906959896': []}

exec(code, env_args)
