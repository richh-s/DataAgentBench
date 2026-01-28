code = """import json

path = var_call_yGpAynzIoSqSe9wxFVL88TgL
with open(path, 'r') as f:
    etf_recs = json.load(f)
etf_symbols = sorted({r['Symbol'] for r in etf_recs if r.get('Symbol')})

path2 = var_call_v5GUXnTyPU6cpGhiSLYg0wi4
with open(path2, 'r') as f:
    trade_tables = set(json.load(f))

symbols = [s for s in etf_symbols if s in trade_tables]

parts = []
for s in symbols:
    parts.append("SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s))

queries = []
max_len = 800000
current = []
cur_len = 0
for p in parts:
    add_len = len(p) + (11 if current else 0)
    if cur_len + add_len > max_len:
        queries.append("SELECT symbol, max_adj_close FROM (" + " UNION ALL ".join(current) + ") WHERE max_adj_close > 200 ORDER BY symbol")
        current = [p]
        cur_len = len(p)
    else:
        if current:
            cur_len += 11
        current.append(p)
        cur_len += len(p)
if current:
    queries.append("SELECT symbol, max_adj_close FROM (" + " UNION ALL ".join(current) + ") WHERE max_adj_close > 200 ORDER BY symbol")

out = {'symbols_considered': len(symbols), 'chunks': len(queries), 'first_query_preview': queries[0][:5000] if queries else ''}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_a4jDHUOrnVwDbmbC1dsIe3Wg': ['stockinfo'], 'var_call_yGpAynzIoSqSe9wxFVL88TgL': 'file_storage/call_yGpAynzIoSqSe9wxFVL88TgL.json', 'var_call_v5GUXnTyPU6cpGhiSLYg0wi4': 'file_storage/call_v5GUXnTyPU6cpGhiSLYg0wi4.json'}

exec(code, env_args)
