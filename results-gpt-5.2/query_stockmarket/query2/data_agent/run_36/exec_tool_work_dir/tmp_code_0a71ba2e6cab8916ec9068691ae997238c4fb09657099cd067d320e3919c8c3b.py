code = """import json

arca_path = var_call_0RegFbqKvSG6fyuxaJLSGIv0
with open(arca_path, 'r') as f:
    arca = json.load(f)

trade_tables_path = var_call_o0oobMrJCXq4NbWowswYruJG
with open(trade_tables_path, 'r') as f:
    trade_tables = set(json.load(f))

arca_symbols = [r['Symbol'] for r in arca]
symbols = [s for s in arca_symbols if s in trade_tables]

batches = []
batch = []
char_count = 0
for s in symbols:
    part = "SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(sym=s)
    # rough length including UNION ALL
    add_len = len(part) + (11 if batch else 0)
    if char_count + add_len > 80000 and batch:
        batches.append(batch)
        batch = [s]
        char_count = len(part)
    else:
        batch.append(s)
        char_count += add_len
if batch:
    batches.append(batch)

print('__RESULT__:')
print(json.dumps({'n_batches': len(batches), 'batch_sizes': [len(b) for b in batches[:5]], 'max_batch_size': max(len(b) for b in batches)}))"""

env_args = {'var_call_0RegFbqKvSG6fyuxaJLSGIv0': 'file_storage/call_0RegFbqKvSG6fyuxaJLSGIv0.json', 'var_call_o0oobMrJCXq4NbWowswYruJG': 'file_storage/call_o0oobMrJCXq4NbWowswYruJG.json', 'var_call_O5IqNdtgrUBtbVOTzIhtZjw2': {'n_candidate_symbols': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
