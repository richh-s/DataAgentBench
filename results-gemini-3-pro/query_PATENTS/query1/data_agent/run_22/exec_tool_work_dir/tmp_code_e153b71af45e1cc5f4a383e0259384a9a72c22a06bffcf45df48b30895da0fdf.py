code = """import json
import re

cpc_file_path = locals()['var_function-call-15748739634169971950']
with open(cpc_file_path, 'r') as f:
    cpc_data = json.load(f)

level5_symbols = set()
for item in cpc_data:
    if item.get('symbol'):
        level5_symbols.add(item['symbol'])

debug_info = {}
debug_info["num_level5"] = len(level5_symbols)
debug_info["sample_level5"] = list(level5_symbols)[:10]

pub_file_path = locals()['var_function-call-14833157841070883006']
with open(pub_file_path, 'r') as f:
    pub_data = json.load(f)

debug_info["num_records"] = len(pub_data)

year_pattern = re.compile(r'\b(?:19|20)\d{2}\b')
matched_years = 0
matched_cpcs = 0
counts = {}

for i, row in enumerate(pub_data):
    f_date = row.get('filing_date', '')
    y_matches = year_pattern.findall(f_date)
    if y_matches:
        matched_years += 1
        year = int(y_matches[-1])
        
        cpc_json = row.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_json)
            found_syms = set()
            for entry in cpc_list:
                code = entry.get('code', '')
                if len(code) >= 4:
                    prefix = code[:4]
                    if prefix in level5_symbols:
                        found_syms.add(prefix)
            
            if found_syms:
                matched_cpcs += 1
                for s in found_syms:
                    if s not in counts:
                        counts[s] = {}
                    counts[s][year] = counts[s].get(year, 0) + 1
        except:
            pass

debug_info["matched_years"] = matched_years
debug_info["matched_cpcs_patents"] = matched_cpcs
debug_info["sample_counts_keys"] = list(counts.keys())[:5]
if counts:
    first_key = list(counts.keys())[0]
    debug_info["sample_counts_values"] = counts[first_key]

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-15748739634169971950': 'file_storage/function-call-15748739634169971950.json', 'var_function-call-15365107857304262203': 'file_storage/function-call-15365107857304262203.json', 'var_function-call-14487137383779015423': [{'COUNT(*)': '277813'}], 'var_function-call-14833157841070883006': 'file_storage/function-call-14833157841070883006.json', 'var_function-call-9103271946905956666': [], 'var_function-call-18064361241579381342': 'Done'}

exec(code, env_args)
