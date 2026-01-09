code = """import json, pandas as pd

info = var_call_wgw92BVAntb683am8PU9CuoP
if isinstance(info, str):
    with open(info, 'r') as f:
        info = json.load(f)

trade_tables = var_call_1ua2Y7QX3q0bbYnH7DZgKC2b
if isinstance(trade_tables, str):
    with open(trade_tables, 'r') as f:
        trade_tables = json.load(f)

etf_symbols = sorted(set(pd.DataFrame(info)['symbol']).intersection(trade_tables))

# Chunk union queries to manageable size
chunks = [etf_symbols[i:i+150] for i in range(0, len(etf_symbols), 150)]
queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        parts.append("SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'".format(s=sym))
    q = "SELECT symbol, max_adj_close FROM (" + " UNION ALL ".join(parts) + ") t WHERE max_adj_close > 200"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'num_candidate_etfs': len(etf_symbols), 'num_chunks': len(queries), 'chunk_sizes': [len(c) for c in chunks], 'queries': queries[:3]}))"""

env_args = {'var_call_wgw92BVAntb683am8PU9CuoP': 'file_storage/call_wgw92BVAntb683am8PU9CuoP.json', 'var_call_1ua2Y7QX3q0bbYnH7DZgKC2b': 'file_storage/call_1ua2Y7QX3q0bbYnH7DZgKC2b.json', 'var_call_LcZdQORHsdFywW8kfXLs8ogr': {'test': 'ok'}, 'var_call_Xfvd67ZxRXS1nJxPeBIqrjpb': 'file_storage/call_Xfvd67ZxRXS1nJxPeBIqrjpb.json', 'var_call_s7asqScoZqD7HnSZF7Y06mHX': [], 'var_call_ZrZYcvabocduQmgMH4vatf0f': {'num_candidate_etfs': 1435, 'num_needs_quote': 0, 'examples_needs_quote': []}}

exec(code, env_args)
