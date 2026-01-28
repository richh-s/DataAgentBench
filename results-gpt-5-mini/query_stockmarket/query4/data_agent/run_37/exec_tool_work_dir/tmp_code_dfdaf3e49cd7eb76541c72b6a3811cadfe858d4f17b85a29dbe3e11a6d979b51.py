code = """import json
with open(var_call_gS4FSnUcnhKgrZzAmEzsMtuc, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_Ddl9uDLtMJpf1r6JrUODvNuK, 'r') as f:
    trade_tables = json.load(f)

symbols = [rec['Symbol'] for rec in stockinfo]
symbol_set = set(symbols)
available = [t for t in trade_tables if t in symbol_set]
available_sorted = sorted(available)

out = {'available_count': len(available_sorted), 'sample_symbols': available_sorted[:10]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gS4FSnUcnhKgrZzAmEzsMtuc': 'file_storage/call_gS4FSnUcnhKgrZzAmEzsMtuc.json', 'var_call_Ddl9uDLtMJpf1r6JrUODvNuK': 'file_storage/call_Ddl9uDLtMJpf1r6JrUODvNuK.json'}

exec(code, env_args)
