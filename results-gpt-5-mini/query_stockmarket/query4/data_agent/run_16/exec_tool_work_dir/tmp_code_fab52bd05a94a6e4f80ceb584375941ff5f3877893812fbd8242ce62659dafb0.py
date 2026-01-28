code = """import json
with open(var_call_nELGdyvPXxMt9K3rUNiloF4h, 'r') as f:
    info = json.load(f)
with open(var_call_OxR5V4zYOQmYrDGwhBhWPqi7, 'r') as f:
    tables = json.load(f)

n_info = len(info)
n_tables = len(tables)

print('__RESULT__:')
print(json.dumps({'n_info': n_info, 'n_tables': n_tables}))"""

env_args = {'var_call_nELGdyvPXxMt9K3rUNiloF4h': 'file_storage/call_nELGdyvPXxMt9K3rUNiloF4h.json', 'var_call_OxR5V4zYOQmYrDGwhBhWPqi7': 'file_storage/call_OxR5V4zYOQmYrDGwhBhWPqi7.json'}

exec(code, env_args)
