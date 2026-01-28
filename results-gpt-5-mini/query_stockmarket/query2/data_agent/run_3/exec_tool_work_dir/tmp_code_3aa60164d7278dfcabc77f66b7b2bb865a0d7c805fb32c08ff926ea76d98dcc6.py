code = """import json
# Read the large query dict produced earlier
qdict = var_call_gNjKSQ8NrIs8YxHuOuss1949
if isinstance(qdict, str):
    with open(qdict, 'r') as f:
        qdict = json.load(f)
query = qdict.get('query', '')
parts = [p.strip() for p in query.split('UNION ALL')]
symbols = []
for p in parts:
    if p.startswith("SELECT '"):
        try:
            sym = p.split("SELECT '")[1].split("' AS Symbol")[0]
            symbols.append(sym)
        except Exception:
            continue
# create batches of 200
batch_size = 200
batches = [symbols[i:i+batch_size] for i in range(0, len(symbols), batch_size)]
batch_queries = []
for batch in batches:
    parts2 = []
    for s in batch:
        part = ("SELECT '{s}' AS Symbol, sub.max_adj_close FROM (SELECT MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" "
                "WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') sub WHERE sub.max_adj_close > 200").format(s=s)
        parts2.append(part)
    q = ' UNION ALL '.join(parts2) + ' ORDER BY Symbol;'
    batch_queries.append(q)
print('__RESULT__:')
print(json.dumps({'num_symbols': len(symbols), 'num_batches': len(batch_queries), 'batch_queries': batch_queries}))"""

env_args = {'var_call_XuluQuL9bhjymtKjFC7XCB4i': 'file_storage/call_XuluQuL9bhjymtKjFC7XCB4i.json', 'var_call_tVILwlranVjeUxQC74j9olYj': 'file_storage/call_tVILwlranVjeUxQC74j9olYj.json', 'var_call_3NGY6ia1TYDV28YzTsJ47bg5': 'file_storage/call_3NGY6ia1TYDV28YzTsJ47bg5.json', 'var_call_gNjKSQ8NrIs8YxHuOuss1949': 'file_storage/call_gNjKSQ8NrIs8YxHuOuss1949.json'}

exec(code, env_args)
