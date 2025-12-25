code = """import json
import re

# Load data again (reuse paths)
with open(locals()['var_function-call-4228191098478002445'], 'r') as f:
    l5_data = json.load(f)
target_cpcs = set(item['symbol'] for item in l5_data)

with open(locals()['var_function-call-4228191098478004752'], 'r') as f:
    pub_data = json.load(f)

print(f"Total pub records: {len(pub_data)}")
print(f"Total target CPCs: {len(target_cpcs)}")

year_pattern = re.compile(r'\b(19|20)\d{2}\b')
years_found = {}
matched_cpcs_count = 0

sample_dates = []

for i, row in enumerate(pub_data):
    if i < 5:
        sample_dates.append(row.get('filing_date'))

    f_date = row.get('filing_date', '')
    match = year_pattern.search(f_date)
    if match:
        y = int(match.group(0))
        years_found[y] = years_found.get(y, 0) + 1
        
        cpc_json = row.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_json)
        except:
            continue
            
        for entry in cpc_list:
            code = entry.get('code', '')
            if len(code) >= 4:
                prefix = code[:4]
                if prefix in target_cpcs:
                    matched_cpcs_count += 1

print(f"Sample dates: {sample_dates}")
print(f"Years distribution (top 10): {sorted(years_found.items(), key=lambda x: x[1], reverse=True)[:10]}")
print(f"Total matched CPC occurrences: {matched_cpcs_count}")
print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-4228191098478004752': 'file_storage/function-call-4228191098478004752.json', 'var_function-call-4228191098478002445': 'file_storage/function-call-4228191098478002445.json', 'var_function-call-1200149957190319519': []}

exec(code, env_args)
