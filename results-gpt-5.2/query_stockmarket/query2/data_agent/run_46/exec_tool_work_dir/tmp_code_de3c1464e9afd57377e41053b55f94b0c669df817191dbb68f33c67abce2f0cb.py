code = """import json
path = var_call_8BRy2xXU5qjQcBQIHostXyf0
with open(path,'r') as f:
    etfs=json.load(f)
syms=sorted({r['Symbol'] for r in etfs if r.get('Symbol')})
pt_path = var_call_sNc7LSyyo3Q8oR8uQ2zyBJlI
with open(pt_path,'r') as f:
    price_tables=set(json.load(f))
syms_in_db=[s for s in syms if s in price_tables]
print('__RESULT__:')
print(json.dumps({'symbols_in_metadata':len(syms),'symbols_with_price_table':len(syms_in_db)}))"""

env_args = {'var_call_8BRy2xXU5qjQcBQIHostXyf0': 'file_storage/call_8BRy2xXU5qjQcBQIHostXyf0.json', 'var_call_sNc7LSyyo3Q8oR8uQ2zyBJlI': 'file_storage/call_sNc7LSyyo3Q8oR8uQ2zyBJlI.json'}

exec(code, env_args)
