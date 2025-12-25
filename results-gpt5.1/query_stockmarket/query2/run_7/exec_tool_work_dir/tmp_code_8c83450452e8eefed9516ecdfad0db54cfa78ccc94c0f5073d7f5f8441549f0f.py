code = """import json, pandas as pd

path = var_call_QYTpf2HRspf40sypf2dGjtvI
etfs = pd.read_json(path)
symbols = etfs['Symbol'].tolist()

batches = [symbols[i:i+200] for i in range(0, len(symbols), 200)]

queries = []
for batch in batches:
    in_list = ",".join([f'"{s}"' for s in batch])
    q = f"SELECT symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM read_parquet('stocktrade_database', hive_partitioning=1) WHERE strftime('%Y', Date) = '2015' AND symbol IN ({in_list}) GROUP BY symbol HAVING max_adj_close_2015 > 200;"
    queries.append(q)

result = {"queries": queries}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QYTpf2HRspf40sypf2dGjtvI': 'file_storage/call_QYTpf2HRspf40sypf2dGjtvI.json', 'var_call_UmlkwJgqouxjxNKaEFCzRbH4': 'file_storage/call_UmlkwJgqouxjxNKaEFCzRbH4.json'}

exec(code, env_args)
