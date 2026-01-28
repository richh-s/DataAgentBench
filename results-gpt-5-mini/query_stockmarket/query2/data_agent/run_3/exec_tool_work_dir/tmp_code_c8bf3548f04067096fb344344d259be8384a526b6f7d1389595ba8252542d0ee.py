code = """import json
# read the generated query from var_call_gNjKSQ8NrIs8YxHuOuss1949
v = var_call_gNjKSQ8NrIs8YxHuOuss1949
if isinstance(v, str):
    with open(v, 'r') as f:
        data = json.load(f)
else:
    data = v
query = data.get('query', '')
# To avoid sending an overly long query, we'll split symbols into batches of 200 and run sequentially
symbols = []
# extract symbols by parsing the query parts
for part in query.split('UNION ALL'):
    part = part.strip()
    if part.startswith("SELECT '"):
        sym = part.split("SELECT '")[1].split("' AS Symbol")[0]
        symbols.append(sym)

# create batches
batch_size = 200
batches = [symbols[i:i+batch_size] for i in range(0, len(symbols), batch_size)]
results = []
from functions import query_db
for batch in batches:
    parts = []
    for s in batch:
        part = ("SELECT '{s}' AS Symbol, sub.max_adj_close FROM (SELECT MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') sub WHERE sub.max_adj_close > 200").format(s=s)
        parts.append(part)
    batch_query = ' UNION ALL '.join(parts) + ' ORDER BY Symbol;'
    res = query_db(db_name='stocktrade_database', query=batch_query)
    results.append(res)

print('__RESULT__:')
print(json.dumps({'num_batches': len(batches), 'batch_count_results': [len(r) if not isinstance(r,str) else 0 for r in results]}))"""

env_args = {'var_call_XuluQuL9bhjymtKjFC7XCB4i': 'file_storage/call_XuluQuL9bhjymtKjFC7XCB4i.json', 'var_call_tVILwlranVjeUxQC74j9olYj': 'file_storage/call_tVILwlranVjeUxQC74j9olYj.json', 'var_call_3NGY6ia1TYDV28YzTsJ47bg5': 'file_storage/call_3NGY6ia1TYDV28YzTsJ47bg5.json', 'var_call_gNjKSQ8NrIs8YxHuOuss1949': 'file_storage/call_gNjKSQ8NrIs8YxHuOuss1949.json'}

exec(code, env_args)
