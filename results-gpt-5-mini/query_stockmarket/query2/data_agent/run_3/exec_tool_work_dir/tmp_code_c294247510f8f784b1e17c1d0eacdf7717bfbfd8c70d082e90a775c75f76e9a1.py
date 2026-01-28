code = """import json
# Load symbols list
v = var_call_3NGY6ia1TYDV28YzTsJ47bg5
if isinstance(v, str):
    with open(v, 'r') as f:
        data = json.load(f)
else:
    data = v
symbols = data.get('symbols_in_trade', [])
parts = []
for s in symbols:
    # Use single-quoted Python strings to avoid escaping double quotes in SQL
    part = ('SELECT "{sym}" AS Symbol, t.max_adj_close FROM ('
            'SELECT MAX("Adj Close") AS max_adj_close FROM "{sym}" '
            "WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'") t "
            "WHERE t.max_adj_close > 200").format(sym=s)
    parts.append(part)
if parts:
    query = ' UNION ALL '.join(parts) + ' ORDER BY Symbol;'
else:
    query = ''
print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_XuluQuL9bhjymtKjFC7XCB4i': 'file_storage/call_XuluQuL9bhjymtKjFC7XCB4i.json', 'var_call_tVILwlranVjeUxQC74j9olYj': 'file_storage/call_tVILwlranVjeUxQC74j9olYj.json', 'var_call_3NGY6ia1TYDV28YzTsJ47bg5': 'file_storage/call_3NGY6ia1TYDV28YzTsJ47bg5.json'}

exec(code, env_args)
