code = """import json, pandas as pd
path = var_call_SEKBA9byMVj76eE10UOZ2XdI
with open(path) as f:
    etfs = json.load(f)
syms = [r['Symbol'] for r in etfs]
chunks = []
for s in syms:
    chunks.append(f"SELECT '{s}' AS Symbol, Date, \"Adj Close\" FROM '{s}' WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200")
query = " UNION ALL ".join(chunks)
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_SEKBA9byMVj76eE10UOZ2XdI': 'file_storage/call_SEKBA9byMVj76eE10UOZ2XdI.json', 'var_call_l8YPy87yLJMntN0pkvCGOKhA': 'file_storage/call_l8YPy87yLJMntN0pkvCGOKhA.json'}

exec(code, env_args)
