code = """import json

symbols_path = var_call_GHbjn5edvAV2zNRHx7OO8wPW
with open(symbols_path, 'r') as f:
    symbols_recs = json.load(f)

symbols = sorted({r['Symbol'] for r in symbols_recs if r.get('Symbol')})

trade_tables_path = var_call_hipFBLjhlaj5HXfnBGqtGwWK
with open(trade_tables_path, 'r') as f:
    trade_tables = set(json.load(f))

symbols = [s for s in symbols if s in trade_tables]

parts = []
for s in symbols:
    parts.append("SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'".format(sym=s))

union_query = "\nUNION ALL\n".join(parts)
query = "SELECT Symbol, max_adj_close FROM (\n{u}\n) WHERE max_adj_close > 200 ORDER BY Symbol;".format(u=union_query)

print('__RESULT__:')
print(json.dumps({'query': query, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_jcdWCss9A9d2aT3nkcLSVYab': ['stockinfo'], 'var_call_GHbjn5edvAV2zNRHx7OO8wPW': 'file_storage/call_GHbjn5edvAV2zNRHx7OO8wPW.json', 'var_call_hipFBLjhlaj5HXfnBGqtGwWK': 'file_storage/call_hipFBLjhlaj5HXfnBGqtGwWK.json'}

exec(code, env_args)
