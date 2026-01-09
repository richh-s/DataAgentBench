code = """import json, pandas as pd

# load arca ETFs
arca_path = var_call_0RegFbqKvSG6fyuxaJLSGIv0
with open(arca_path, 'r') as f:
    arca = json.load(f)

# load available trade tables
trade_tables_path = var_call_o0oobMrJCXq4NbWowswYruJG
with open(trade_tables_path, 'r') as f:
    trade_tables = set(json.load(f))

arca_symbols = [r['Symbol'] for r in arca]
# keep only symbols that have a price table
symbols = [s for s in arca_symbols if s in trade_tables]

# create union query for max adj close in 2015
parts = []
for s in symbols:
    parts.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")

union_query = "\nUNION ALL\n".join(parts)
# wrap to filter >200
query = f"SELECT Symbol, max_adj_close FROM (\n{union_query}\n) t WHERE max_adj_close > 200 ORDER BY Symbol;"

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'query': query}))"""

env_args = {'var_call_0RegFbqKvSG6fyuxaJLSGIv0': 'file_storage/call_0RegFbqKvSG6fyuxaJLSGIv0.json', 'var_call_o0oobMrJCXq4NbWowswYruJG': 'file_storage/call_o0oobMrJCXq4NbWowswYruJG.json'}

exec(code, env_args)
