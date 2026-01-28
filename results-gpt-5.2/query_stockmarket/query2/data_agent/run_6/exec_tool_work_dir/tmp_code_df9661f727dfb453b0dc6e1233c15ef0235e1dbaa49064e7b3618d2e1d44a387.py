code = """import json

path = var_call_HB4X7789w5RugKPxR8cyQbNE
with open(path, 'r') as f:
    etfs = json.load(f)

tickers = sorted({r['Symbol'] for r in etfs if r.get('Symbol')})

path2 = var_call_IxW6haiTFueyDjZZpfh1Pko3
with open(path2, 'r') as f:
    tables = set(json.load(f))

trade_tickers = [t for t in tickers if t in tables]

# build first 5 sample query parts
parts = []
for t in trade_tickers[:5]:
    parts.append("SELECT '{t}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{t}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(t=t))

full_query = ' UNION ALL '.join(parts)

print('__RESULT__:')
print(json.dumps({"sample": full_query, "n": len(trade_tickers)}))"""

env_args = {'var_call_IGFXHUnqBZxLEESlaW1VjsQS': ['stockinfo'], 'var_call_HB4X7789w5RugKPxR8cyQbNE': 'file_storage/call_HB4X7789w5RugKPxR8cyQbNE.json', 'var_call_IxW6haiTFueyDjZZpfh1Pko3': 'file_storage/call_IxW6haiTFueyDjZZpfh1Pko3.json', 'var_call_SbEU7E8vKUtf8YIKBmQDT6p9': 'ok'}

exec(code, env_args)
