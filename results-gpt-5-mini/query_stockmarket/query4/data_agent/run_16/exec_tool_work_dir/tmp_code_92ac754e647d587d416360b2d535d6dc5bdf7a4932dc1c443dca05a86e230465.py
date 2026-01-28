code = """import json
with open(var_call_nELGdyvPXxMt9K3rUNiloF4h, 'r') as f:
    info = json.load(f)
with open(var_call_OxR5V4zYOQmYrDGwhBhWPqi7, 'r') as f:
    tables = json.load(f)

symbols_from_info = [rec['Symbol'] for rec in info]
tables_set = set(tables)

symbols = [s for s in symbols_from_info if s in tables_set]

print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_call_nELGdyvPXxMt9K3rUNiloF4h': 'file_storage/call_nELGdyvPXxMt9K3rUNiloF4h.json', 'var_call_OxR5V4zYOQmYrDGwhBhWPqi7': 'file_storage/call_OxR5V4zYOQmYrDGwhBhWPqi7.json', 'var_call_LhZBRkhnWZtgcltCUmMOfIF7': {'n_info': 234, 'n_tables': 2753}}

exec(code, env_args)
