code = """import json
import re

# Load data again (lighter version for debug)
with open(locals()['var_function-call-9506971857936168120'], 'r') as f:
    level5_data = json.load(f)
valid_level5 = set(item['symbol'] for item in level5_data)

with open(locals()['var_function-call-16148835938051840028'], 'r') as f:
    pub_data = json.load(f)

print(f"Total level 5 symbols: {len(valid_level5)}")
print(f"Sample level 5: {list(valid_level5)[:5]}")

year_pattern = re.compile(r'\b(19|20)\d{2}\b')
years_found = set()
cpc_sample_counts = 0

for record in pub_data[:100]:
    f_date = record.get('filing_date', '')
    match = year_pattern.search(f_date)
    if match:
        years_found.add(int(match.group(0)))
    
    cpc_str = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
        if cpc_list:
            cpc_sample_counts += 1
            # Check matching
            for entry in cpc_list:
                code = entry.get('code', '')
                if len(code) >= 4:
                    sub = code[:4]
                    if sub in valid_level5:
                        # Found a match
                        pass
    except:
        pass

# Check all years in the dataset
all_years = set()
for record in pub_data:
    f_date = record.get('filing_date', '')
    match = year_pattern.search(f_date)
    if match:
        all_years.add(int(match.group(0)))

print(f"Years found: {sorted(list(all_years))}")
print(f"Records with parsed CPCs in first 100: {cpc_sample_counts}")

print("__RESULT__:")
print("DEBUG_DONE")"""

env_args = {'var_function-call-9506971857936168120': 'file_storage/function-call-9506971857936168120.json', 'var_function-call-16148835938051840028': 'file_storage/function-call-16148835938051840028.json', 'var_function-call-17364678478425837483': []}

exec(code, env_args)
