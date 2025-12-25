code = """import json
import pandas as pd
import re

# Load Level 5 CPC Codes
with open(locals()['var_function-call-15598239778960788131'], 'r') as f:
    cpc_def_data = json.load(f)
level5_codes = list(item['symbol'] for item in cpc_def_data)

# Load Publication Data
with open(locals()['var_function-call-2589434273534193107'], 'r') as f:
    pub_data = json.load(f)

debug_info = {}
debug_info["level5_sample"] = level5_codes[:10]
debug_info["total_level5"] = len(level5_codes)

years = set()
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

sample_cpcs = []
match_count = 0
level5_set = set(level5_codes)

for i, row in enumerate(pub_data):
    f_date = row.get('filing_date', '')
    if f_date:
        match = year_pattern.search(f_date)
        if match:
            years.add(int(match.group(0)))
    
    if i < 100: # Check first 100 patents
        cpc_str = row.get('cpc', '')
        if cpc_str:
            try:
                cpc_list = json.loads(cpc_str)
                for item in cpc_list:
                    code = item.get('code', '')
                    sample_cpcs.append(code)
                    if len(code) >= 4 and code[:4] in level5_set:
                        match_count += 1
            except:
                pass

debug_info["years_found"] = sorted(list(years))
debug_info["sample_cpcs"] = sample_cpcs[:10]
debug_info["matches_in_sample"] = match_count

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-15598239778960788131': 'file_storage/function-call-15598239778960788131.json', 'var_function-call-15598239778960788336': [{'count(*)': '277813'}], 'var_function-call-2589434273534193107': 'file_storage/function-call-2589434273534193107.json', 'var_function-call-6086116679698044266': []}

exec(code, env_args)
