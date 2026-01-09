code = """import json, pandas as pd

# load symbols from stockinfo query
symbols_path = var_call_GHbjn5edvAV2zNRHx7OO8wPW
with open(symbols_path, 'r') as f:
    symbols_recs = json.load(f)

symbols = sorted({r['Symbol'] for r in symbols_recs if r.get('Symbol')})

# load available tables list
trade_tables_path = var_call_hipFBLjhlaj5HXfnBGqtGwWK
with open(trade_tables_path, 'r') as f:
    trade_tables = set(json.load(f))

symbols = [s for s in symbols if s in trade_tables]

# build a UNION ALL query to find max Adj Close in 2015 for each symbol
parts = []
for s in symbols:
    parts.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'")

union_query = "\nUNION ALL\n".join(parts)
query = f"SELECT Symbol, max_adj_close FROM (\n{union_query}\n) WHERE max_adj_close > 200 ORDER BY Symbol;"

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'query': query}))"""

env_args = {'var_call_jcdWCss9A9d2aT3nkcLSVYab': ['stockinfo'], 'var_call_GHbjn5edvAV2zNRHx7OO8wPW': 'file_storage/call_GHbjn5edvAV2zNRHx7OO8wPW.json', 'var_call_hipFBLjhlaj5HXfnBGqtGwWK': 'file_storage/call_hipFBLjhlaj5HXfnBGqtGwWK.json'}

exec(code, env_args)
