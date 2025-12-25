code = """import json
import re

cpc_file_path = locals()['var_function-call-15748739634169971950']
with open(cpc_file_path, 'r') as f:
    cpc_data = json.load(f)

level5_symbols = set()
for item in cpc_data:
    if item.get('symbol'):
        level5_symbols.add(item['symbol'])

print("DEBUG: Number of level 5 symbols:", len(level5_symbols))
print("DEBUG: Sample level 5 symbols:", list(level5_symbols)[:10])

pub_file_path = locals()['var_function-call-14833157841070883006']
with open(pub_file_path, 'r') as f:
    pub_data = json.load(f)

print("DEBUG: Number of publication records:", len(pub_data))

year_pattern = re.compile(r'\b(?:19|20)\d{2}\b')
matched_years = 0
matched_cpcs = 0
total_cpcs_checked = 0

sample_dates = []
sample_cpcs = []

for i, row in enumerate(pub_data):
    if i < 5:
        sample_dates.append(row.get('filing_date'))
        sample_cpcs.append(row.get('cpc'))
        
    f_date = row.get('filing_date', '')
    y_matches = year_pattern.findall(f_date)
    if y_matches:
        matched_years += 1
        year = int(y_matches[-1])
        
        cpc_json = row.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_json)
            if cpc_list:
                total_cpcs_checked += 1
                found = False
                for entry in cpc_list:
                    code = entry.get('code', '')
                    if len(code) >= 4:
                        prefix = code[:4]
                        if prefix in level5_symbols:
                            matched_cpcs += 1
                            found = True
                            break # Count once per patent
        except:
            pass

print("DEBUG: Matched Years:", matched_years)
print("DEBUG: Total CPCs (patents with valid CPC json) Checked:", total_cpcs_checked)
print("DEBUG: Matched CPCs (patents matching a level 5 symbol):", matched_cpcs)
print("DEBUG: Sample Dates:", sample_dates)

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-15748739634169971950': 'file_storage/function-call-15748739634169971950.json', 'var_function-call-15365107857304262203': 'file_storage/function-call-15365107857304262203.json', 'var_function-call-14487137383779015423': [{'COUNT(*)': '277813'}], 'var_function-call-14833157841070883006': 'file_storage/function-call-14833157841070883006.json', 'var_function-call-9103271946905956666': []}

exec(code, env_args)
