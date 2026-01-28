code = """import json
with open(var_call_gS4FSnUcnhKgrZzAmEzsMtuc, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_Ddl9uDLtMJpf1r6JrUODvNuK, 'r') as f:
    trade_tables = json.load(f)

symbol_set = set(rec['Symbol'] for rec in stockinfo)
available = [t for t in trade_tables if t in symbol_set]
available.sort()

out = {'available': available}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gS4FSnUcnhKgrZzAmEzsMtuc': 'file_storage/call_gS4FSnUcnhKgrZzAmEzsMtuc.json', 'var_call_Ddl9uDLtMJpf1r6JrUODvNuK': 'file_storage/call_Ddl9uDLtMJpf1r6JrUODvNuK.json', 'var_call_oXVCb3OKjyhRkTCgKdVFJwnZ': {'available_count': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)
