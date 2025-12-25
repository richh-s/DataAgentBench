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

with open(patents_path, 'r') as f:
    patents = json.load(f)

debug_info = {}
debug_info['patents_count'] = len(patents)

# Find a patent with H01L
target_prefix = 'H01L'
found_patent = None

for p in patents:
    cpc_str = p.get('cpc', '[]')
    if target_prefix in cpc_str:
        found_patent = p
        break

if found_patent:
    debug_info['found_patent_cpc_str'] = found_patent['cpc']
    
    # Try to parse and match
    cpc_str = found_patent['cpc']
    try:
        cpc_list = json.loads(cpc_str)
        debug_info['parsed_codes'] = [c.get('code') for c in cpc_list]
        
        matches = []
        for c in cpc_list:
            code = c.get('code', '')
            if len(code) >= 4:
                prefix = code[:4]
                if prefix in level_5_codes:
                    matches.append(prefix)
                else:
                    # Check if prefix matches target
                    if prefix == target_prefix:
                        matches.append(f"{prefix} (FOUND but not in set?)")
        
        debug_info['matches'] = matches
        debug_info['is_target_in_set'] = target_prefix in level_5_codes
        
    except Exception as e:
        debug_info['error'] = str(e)

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-6641923460859800772': 'file_storage/function-call-6641923460859800772.json', 'var_function-call-6641923460859799993': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-4289607868665699138': [{'count': '260808'}], 'var_function-call-4289607868665698023': [{'count(*)': '277813'}], 'var_function-call-8775067390743093543': 'file_storage/function-call-8775067390743093543.json', 'var_function-call-17651004867622027777': 'file_storage/function-call-17651004867622027777.json', 'var_function-call-5059798945412610512': [], 'var_function-call-15245929960655701249': [], 'var_function-call-11939134990751395154': 'DONE', 'var_function-call-7224638551277790076': {'level_5_count': 677, 'codes_with_filings': 0}, 'var_function-call-8938606408172290764': {'sample_patent_codes': ['H01L21/50', 'F25J1/0022', 'B60Y2306/05', 'B65B35/38', 'B32B29/02', 'H01L27/148', 'A61F2/4425', 'H04N5/232', 'H02J7/342', 'A61K31/7052'], 'levels_found_in_patents': ['10.0', '9.0', '8.0', '10.0', '8.0', '11.0', '12.0', '9.0', '10.0', '9.0', '10.0', '8.0', '9.0', '8.0', '8.0', '9.0', '11.0', '11.0', '13.0', '10.0'], 'sample_level_5_from_db': ['A01H', 'A01F', 'A01C', 'A01G', 'A23J', 'A01N', 'A01P', 'A01D', 'A01L', 'A01K']}, 'var_function-call-14311176162521282890': {'codes_found_in_patents': 0}, 'var_function-call-5852688278291348107': {'level_5_count': 677, 'sample_level_5': ['F21H', 'C07C', 'E05D', 'C07F', 'G16Y', 'B60P', 'D10B', 'B24C', 'C12P', 'F24B'], 'lengths': [4], 'H01L_in_level5': True, 'sample_repr': ["'F21H'", "'C07C'", "'E05D'", "'C07F'", "'G16Y'"]}}

exec(code, env_args)
