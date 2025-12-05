code = """import json, pandas as pd

path = var_call_DgcbuFyj7ymKsIl6EiXFmi7n
with open(path, 'r') as f:
    etfs = json.load(f)
syms = [row['Symbol'] for row in etfs]

chunks = [syms[i:i+200] for i in range(0, len(syms), 200)]

queries = []
for chunk in chunks:
    tickers = ", ".join([f'"{s}"' for s in chunk])
    q = f"SELECT '{','.join(chunk)}' as tickers;"
    queries.append(q)

result = json.dumps({'symbols_sample': syms[:50], 'count': len(syms)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_DgcbuFyj7ymKsIl6EiXFmi7n': 'file_storage/call_DgcbuFyj7ymKsIl6EiXFmi7n.json', 'var_call_XXZDX8pYejDzGEANbkEUyHpI': 'file_storage/call_XXZDX8pYejDzGEANbkEUyHpI.json'}

exec(code, env_args)
