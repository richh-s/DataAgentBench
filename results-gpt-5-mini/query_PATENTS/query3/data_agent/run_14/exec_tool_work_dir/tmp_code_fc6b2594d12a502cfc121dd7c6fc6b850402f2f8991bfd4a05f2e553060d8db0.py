code = """import json
fp = var_call_TcfLs4F5bIYb87m9py2HFqX8
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)
primary_codes = sorted(data.get('primary_codes', []))
print('__RESULT__:')
print(json.dumps(primary_codes))"""

env_args = {'var_call_MuJAaiO2PzoIYGskQYaoTn64': 'file_storage/call_MuJAaiO2PzoIYGskQYaoTn64.json', 'var_call_q57aScl073IRIRJqWMJOS9E9': 'file_storage/call_q57aScl073IRIRJqWMJOS9E9.json', 'var_call_lSeKCaJYvKmAFrQEd6Ri9Oy6': 'file_storage/call_lSeKCaJYvKmAFrQEd6Ri9Oy6.json', 'var_call_TcfLs4F5bIYb87m9py2HFqX8': 'file_storage/call_TcfLs4F5bIYb87m9py2HFqX8.json'}

exec(code, env_args)
