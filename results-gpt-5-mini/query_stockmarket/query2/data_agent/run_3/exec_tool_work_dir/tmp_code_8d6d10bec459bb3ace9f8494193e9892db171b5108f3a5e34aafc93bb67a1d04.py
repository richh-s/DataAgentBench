code = """import json
# Load symbols from previous execute_python result
v = var_call_3NGY6ia1TYDV28YzTsJ47bg5
if isinstance(v, str):
    with open(v, 'r') as f:
        data = json.load(f)
else:
    data = v
symbols = data.get('symbols_in_trade', [])
parts = []
for s in symbols:
    part = (
        "SELECT '" + s + "' AS Symbol, "
        "(SELECT MAX(\"Adj Close\") FROM \"" + s + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') AS max_adj_close "
        "WHERE (SELECT MAX(\"Adj Close\") FROM \"" + s + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') > 200"
    )
    parts.append(part)
if parts:
    query = ' UNION ALL '.join(parts) + ' ORDER BY Symbol;'
else:
    query = ''
print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_XuluQuL9bhjymtKjFC7XCB4i': 'file_storage/call_XuluQuL9bhjymtKjFC7XCB4i.json', 'var_call_tVILwlranVjeUxQC74j9olYj': 'file_storage/call_tVILwlranVjeUxQC74j9olYj.json', 'var_call_3NGY6ia1TYDV28YzTsJ47bg5': 'file_storage/call_3NGY6ia1TYDV28YzTsJ47bg5.json'}

exec(code, env_args)
