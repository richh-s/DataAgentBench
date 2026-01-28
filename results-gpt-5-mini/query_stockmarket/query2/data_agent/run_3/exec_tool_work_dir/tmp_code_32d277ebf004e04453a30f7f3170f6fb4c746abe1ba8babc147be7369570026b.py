code = """import json
# Load symbols list from previous step
v = var_call_3NGY6ia1TYDV28YzTsJ47bg5
if isinstance(v, str):
    with open(v, 'r') as f:
        data = json.load(f)
else:
    data = v
symbols = data.get('symbols_in_trade', [])
# create batches of 100
batch_size = 100
batches = [symbols[i:i+batch_size] for i in range(0, len(symbols), batch_size)]
batch_queries = []
for batch in batches:
    parts = []
    for s in batch:
        part = ("SELECT '{s}' AS Symbol, sub.max_adj_close FROM (SELECT MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" "
                "WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') sub WHERE sub.max_adj_close > 200").format(s=s)
        parts.append(part)
    q = ' UNION ALL '.join(parts) + ' ORDER BY Symbol;'
    batch_queries.append(q)
print('__RESULT__:')
print(json.dumps({'num_batches': len(batch_queries), 'batch_queries': batch_queries}))"""

env_args = {'var_call_XuluQuL9bhjymtKjFC7XCB4i': 'file_storage/call_XuluQuL9bhjymtKjFC7XCB4i.json', 'var_call_tVILwlranVjeUxQC74j9olYj': 'file_storage/call_tVILwlranVjeUxQC74j9olYj.json', 'var_call_3NGY6ia1TYDV28YzTsJ47bg5': 'file_storage/call_3NGY6ia1TYDV28YzTsJ47bg5.json', 'var_call_gNjKSQ8NrIs8YxHuOuss1949': 'file_storage/call_gNjKSQ8NrIs8YxHuOuss1949.json'}

exec(code, env_args)
