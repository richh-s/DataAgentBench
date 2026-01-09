code = """import json

# load symbols and map
p = var_call_vQCNJzyENM60Hw8gh67BUjca
with open(p,'r') as f:
    obj = json.load(f)
symbols = obj['symbols']
company_map = obj['company_map']

# load available tables
p2 = var_call_FalNVgCpdE2Qn9pqgDr3kxkE
with open(p2,'r') as f:
    tables = json.load(f)

table_set = set(tables)
syms_avail = [s for s in symbols if s in table_set]
res = {'symbols_avail': syms_avail, 'n_avail': len(syms_avail), 'n_missing': len(symbols)-len(syms_avail)}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_hSnm5hkMQxk7jSRLKxP3Bsak': 'file_storage/call_hSnm5hkMQxk7jSRLKxP3Bsak.json', 'var_call_vQCNJzyENM60Hw8gh67BUjca': 'file_storage/call_vQCNJzyENM60Hw8gh67BUjca.json', 'var_call_FalNVgCpdE2Qn9pqgDr3kxkE': 'file_storage/call_FalNVgCpdE2Qn9pqgDr3kxkE.json'}

exec(code, env_args)
