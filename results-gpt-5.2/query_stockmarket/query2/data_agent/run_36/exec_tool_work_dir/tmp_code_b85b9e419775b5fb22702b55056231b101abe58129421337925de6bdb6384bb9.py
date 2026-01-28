code = """import json

arca_path = var_call_0RegFbqKvSG6fyuxaJLSGIv0
with open(arca_path, 'r') as f:
    arca = json.load(f)

trade_tables_path = var_call_o0oobMrJCXq4NbWowswYruJG
with open(trade_tables_path, 'r') as f:
    trade_tables = set(json.load(f))

arca_symbols = [r['Symbol'] for r in arca]
symbols = [s for s in arca_symbols if s in trade_tables]

# limit query length safety by batching symbols later; for now just output candidate count
print('__RESULT__:')
print(json.dumps({'n_candidate_symbols': len(symbols), 'first10': symbols[:10]}))"""

env_args = {'var_call_0RegFbqKvSG6fyuxaJLSGIv0': 'file_storage/call_0RegFbqKvSG6fyuxaJLSGIv0.json', 'var_call_o0oobMrJCXq4NbWowswYruJG': 'file_storage/call_o0oobMrJCXq4NbWowswYruJG.json'}

exec(code, env_args)
