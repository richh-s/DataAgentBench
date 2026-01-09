code = """import json
path = var_call_o12akxaYuEB1Fv7HiBkYhkab
with open(path,'r') as f:
    obj=json.load(f)
nyse_syms=set(obj['symbols'])

path2 = var_call_opCijmaeUXZdRBS5lKhefJMz
with open(path2,'r') as f:
    trade_tables=json.load(f)

avail=[s for s in trade_tables if s in nyse_syms]
print('__RESULT__:')
print(json.dumps({'avail_symbols': avail, 'company_map': obj['company_map']}))"""

env_args = {'var_call_FQnZeeqY6jpP92SSHDkMcZsR': 'file_storage/call_FQnZeeqY6jpP92SSHDkMcZsR.json', 'var_call_o12akxaYuEB1Fv7HiBkYhkab': 'file_storage/call_o12akxaYuEB1Fv7HiBkYhkab.json', 'var_call_opCijmaeUXZdRBS5lKhefJMz': 'file_storage/call_opCijmaeUXZdRBS5lKhefJMz.json'}

exec(code, env_args)
