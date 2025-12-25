code = """import json, pandas as pd
path = var_call_GJ65B0zFrs2lMKT5L5Zod9RU
with open(path,'r') as f:
    tables = json.load(f)

etf_path = var_call_4UfIxOFUNz9yoOJgRBfo26dC
with open(etf_path,'r') as f:
    etfs = json.load(f)

etf_set = {e['Symbol'] for e in etfs}
available = sorted(list(etf_set.intersection(tables)))

batches = [available[i:i+200] for i in range(0,len(available),200)]
queries = []
for batch in batches:
    syms = ', '.join([f'"{s}"' for s in batch])
    q = f"SELECT symbol FROM (" + " UNION ALL ".join([f'SELECT DISTINCT \"Adj Close\" AS max_adj, " + repr(s) + " AS symbol FROM \"{s}\" WHERE substr(Date,1,4)=\'2015\' AND \"Adj Close\" > 200' for s in batch]) + ") WHERE max_adj IS NOT NULL;"
    queries.append(q)

res = json.dumps({'available_count': len(available), 'sample_query': queries[0] if queries else None})
print("__RESULT__:")
print(res)"""

env_args = {'var_call_4UfIxOFUNz9yoOJgRBfo26dC': 'file_storage/call_4UfIxOFUNz9yoOJgRBfo26dC.json', 'var_call_wtty6HKUIYHrOzVDWedf3wUK': 'file_storage/call_wtty6HKUIYHrOzVDWedf3wUK.json', 'var_call_GJ65B0zFrs2lMKT5L5Zod9RU': 'file_storage/call_GJ65B0zFrs2lMKT5L5Zod9RU.json'}

exec(code, env_args)
