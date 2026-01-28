code = """import json
# load the previous execute_python result which contains symbols_in_trade
v = var_call_3NGY6ia1TYDV28YzTsJ47bg5
if isinstance(v, str):
    with open(v, 'r') as f:
        data = json.load(f)
else:
    data = v
symbols = data.get('symbols_in_trade', [])
# build union query for DuckDB
parts = []
for s in symbols:
    part = f"SELECT '{s}' AS Symbol, max_adj_close FROM (SELECT MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') WHERE max_adj_close > 200"
    parts.append(part)
query = " UNION ALL ".join(parts)
query = query + " ORDER BY Symbol;"
out = {'query': query, 'num_symbols': len(symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_XuluQuL9bhjymtKjFC7XCB4i': 'file_storage/call_XuluQuL9bhjymtKjFC7XCB4i.json', 'var_call_tVILwlranVjeUxQC74j9olYj': 'file_storage/call_tVILwlranVjeUxQC74j9olYj.json', 'var_call_3NGY6ia1TYDV28YzTsJ47bg5': 'file_storage/call_3NGY6ia1TYDV28YzTsJ47bg5.json'}

exec(code, env_args)
