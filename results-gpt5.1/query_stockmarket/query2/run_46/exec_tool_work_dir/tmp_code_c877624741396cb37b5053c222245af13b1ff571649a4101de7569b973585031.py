code = """import json
import pandas as pd

path = var_call_wNTw7gYFSEJzzCuix1qldmg1
with open(path, 'r') as f:
    etfs = json.load(f)

symbols = [row['Symbol'] for row in etfs]
chunks = [symbols[i:i+200] for i in range(0, len(symbols), 200)]

queries = []
for chunk in chunks:
    tickers = ', '.join(["'" + s.replace("'", "''") + "'" for s in chunk])
    q = f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'main' AND table_name IN ({tickers});"
    queries.append(q)

result = {'chunks': queries}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wNTw7gYFSEJzzCuix1qldmg1': 'file_storage/call_wNTw7gYFSEJzzCuix1qldmg1.json', 'var_call_798bid9wAmFJMdpJnsknNmYS': 'file_storage/call_798bid9wAmFJMdpJnsknNmYS.json'}

exec(code, env_args)
