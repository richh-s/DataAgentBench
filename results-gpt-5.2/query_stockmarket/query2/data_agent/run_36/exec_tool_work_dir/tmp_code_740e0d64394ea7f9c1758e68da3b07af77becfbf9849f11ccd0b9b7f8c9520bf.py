code = """import json

arca_path = var_call_0RegFbqKvSG6fyuxaJLSGIv0
with open(arca_path, 'r') as f:
    arca = json.load(f)

trade_tables_path = var_call_o0oobMrJCXq4NbWowswYruJG
with open(trade_tables_path, 'r') as f:
    trade_tables = set(json.load(f))

arca_symbols = [r['Symbol'] for r in arca]
symbols = [s for s in arca_symbols if s in trade_tables]

parts = []
for s in symbols:
    parts.append("SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym=s))

union_query = "\nUNION ALL\n".join(parts)
query = "SELECT Symbol, max_adj_close FROM (\n{u}\n) t WHERE max_adj_close > 200 ORDER BY Symbol;".format(u=union_query)

print('__RESULT__:')
print(json.dumps({'query': query, 'n_candidate_symbols': len(symbols)}))"""

env_args = {'var_call_0RegFbqKvSG6fyuxaJLSGIv0': 'file_storage/call_0RegFbqKvSG6fyuxaJLSGIv0.json', 'var_call_o0oobMrJCXq4NbWowswYruJG': 'file_storage/call_o0oobMrJCXq4NbWowswYruJG.json'}

exec(code, env_args)
