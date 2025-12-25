code = """import json
import re

cpc_defs_path = locals()['var_function-call-8775067390743093543']
patents_path = locals()['var_function-call-17651004867622027777']

with open(cpc_defs_path, 'r') as f:
    cpc_defs = json.load(f)

level_5_codes = set()
for item in cpc_defs:
    try:
        lvl = float(item.get('level', 0))
        if int(lvl) == 5:
            level_5_codes.add(item['symbol'])
    except:
        pass

# Verify length of Level 5 codes
lengths = set(len(c) for c in level_5_codes)
print(f"DEBUG: Lengths of Level 5 codes: {lengths}")
# If all are 4, then slicing [:4] is safe.

with open(patents_path, 'r') as f:
    patents = json.load(f)

counts = {}
year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')

for p in patents:
    f_date = p.get('filing_date', '')
    match = year_pattern.search(f_date)
    if not match: continue
    year = int(match.group(1))
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    unique_lvl5 = set()
    for c in cpc_list:
        code = c.get('code', '')
        # Try matching prefix
        # We can iterate through length 4 prefixes
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level_5_codes:
                unique_lvl5.add(prefix)
    
    for c in unique_lvl5:
        if c not in counts:
            counts[c] = {}
        counts[c][year] = counts[c].get(year, 0) + 1

debug_info = {}
debug_info['codes_found_in_patents'] = len(counts)
if counts:
    s_code = list(counts.keys())[0]
    debug_info['sample_code'] = s_code
    debug_info['sample_counts'] = counts[s_code]

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-6641923460859800772': 'file_storage/function-call-6641923460859800772.json', 'var_function-call-6641923460859799993': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-4289607868665699138': [{'count': '260808'}], 'var_function-call-4289607868665698023': [{'count(*)': '277813'}], 'var_function-call-8775067390743093543': 'file_storage/function-call-8775067390743093543.json', 'var_function-call-17651004867622027777': 'file_storage/function-call-17651004867622027777.json', 'var_function-call-5059798945412610512': [], 'var_function-call-15245929960655701249': [], 'var_function-call-11939134990751395154': 'DONE', 'var_function-call-7224638551277790076': {'level_5_count': 677, 'codes_with_filings': 0}, 'var_function-call-8938606408172290764': {'sample_patent_codes': ['H01L21/50', 'F25J1/0022', 'B60Y2306/05', 'B65B35/38', 'B32B29/02', 'H01L27/148', 'A61F2/4425', 'H04N5/232', 'H02J7/342', 'A61K31/7052'], 'levels_found_in_patents': ['10.0', '9.0', '8.0', '10.0', '8.0', '11.0', '12.0', '9.0', '10.0', '9.0', '10.0', '8.0', '9.0', '8.0', '8.0', '9.0', '11.0', '11.0', '13.0', '10.0'], 'sample_level_5_from_db': ['A01H', 'A01F', 'A01C', 'A01G', 'A23J', 'A01N', 'A01P', 'A01D', 'A01L', 'A01K']}}

exec(code, env_args)
