code = """import json
import pandas as pd

path = var_call_4UfIxOFUNz9yoOJgRBfo26dC
with open(path, 'r') as f:
    etfs = json.load(f)

tickers = [row['Symbol'] for row in etfs]

batches = [tickers[i:i+200] for i in range(0, len(tickers), 200)]

queries = []
for batch in batches:
    symbols_list = ', '.join(["'" + s.replace("'", "''") + "'" for s in batch])
    q = f"SELECT table_name FROM information_schema.tables WHERE table_name IN ({symbols_list});"
    queries.append(q)

result = json.dumps(queries)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_4UfIxOFUNz9yoOJgRBfo26dC': 'file_storage/call_4UfIxOFUNz9yoOJgRBfo26dC.json'}

exec(code, env_args)
