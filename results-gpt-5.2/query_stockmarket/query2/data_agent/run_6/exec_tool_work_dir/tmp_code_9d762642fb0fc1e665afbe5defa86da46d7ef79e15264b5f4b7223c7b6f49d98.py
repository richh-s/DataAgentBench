code = """import json

path = var_call_HB4X7789w5RugKPxR8cyQbNE
with open(path, 'r') as f:
    etfs = json.load(f)

tickers = sorted({r['Symbol'] for r in etfs if r.get('Symbol')})

path2 = var_call_IxW6haiTFueyDjZZpfh1Pko3
with open(path2, 'r') as f:
    tables = set(json.load(f))

trade_tickers = [t for t in tickers if t in tables]

chunks = [trade_tickers[i:i+200] for i in range(0, len(trade_tickers), 200)]

union_queries = []
for ch in chunks:
    parts = []
    for t in ch:
        parts.append("SELECT '{t}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{t}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(t=t))
    union_queries.append(' UNION ALL '.join(parts))

full_query = "SELECT Symbol FROM (" + " UNION ALL ".join(union_queries) + ") WHERE max_adj_close > 200 ORDER BY Symbol;"

print('__RESULT__:')
print(json.dumps({"full_query": full_query, "tickers_considered": len(trade_tickers)}))"""

env_args = {'var_call_IGFXHUnqBZxLEESlaW1VjsQS': ['stockinfo'], 'var_call_HB4X7789w5RugKPxR8cyQbNE': 'file_storage/call_HB4X7789w5RugKPxR8cyQbNE.json', 'var_call_IxW6haiTFueyDjZZpfh1Pko3': 'file_storage/call_IxW6haiTFueyDjZZpfh1Pko3.json'}

exec(code, env_args)
