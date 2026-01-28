code = """import json, pandas as pd

info = var_call_wgw92BVAntb683am8PU9CuoP
if isinstance(info, str):
    with open(info, 'r') as f:
        info = json.load(f)

trade_tables = var_call_1ua2Y7QX3q0bbYnH7DZgKC2b
if isinstance(trade_tables, str):
    with open(trade_tables, 'r') as f:
        trade_tables = json.load(f)

etf_df = pd.DataFrame(info)
etf_symbols = sorted(set(etf_df['symbol']).intersection(trade_tables))

# Build query without embedding double quotes to avoid syntax issues in this environment
parts = []
for sym in etf_symbols:
    stmt = "SELECT '{s}' AS symbol, MAX(Adj Close) AS max_adj_close FROM {s} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(s=sym)
    parts.append(stmt)

query = "SELECT symbol, max_adj_close FROM (" + " UNION ALL ".join(parts) + ") AS t WHERE max_adj_close > 200 ORDER BY symbol"

print('__RESULT__:')
print(json.dumps({'duckdb_query': query, 'num_candidate_etfs': len(etf_symbols)}))"""

env_args = {'var_call_wgw92BVAntb683am8PU9CuoP': 'file_storage/call_wgw92BVAntb683am8PU9CuoP.json', 'var_call_1ua2Y7QX3q0bbYnH7DZgKC2b': 'file_storage/call_1ua2Y7QX3q0bbYnH7DZgKC2b.json', 'var_call_LcZdQORHsdFywW8kfXLs8ogr': {'test': 'ok'}}

exec(code, env_args)
