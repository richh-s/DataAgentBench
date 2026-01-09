code = """import json

# Load nyse arca ETFs
with open(var_call_NZ0JfUmxkUXZtZhMlGbm0tDu, 'r', encoding='utf-8') as f:
    etfs = json.load(f)

# Load trade table names
with open(var_call_eXF2jCX9vVN63ZeYWX46HRZb, 'r', encoding='utf-8') as f:
    tables = json.load(f)

tables_set = {r['table_name'] for r in tables}

tickers = sorted({r['Symbol'] for r in etfs if r.get('Symbol') in tables_set})

# Build UNION ALL query in chunks
chunks = [tickers[i:i+150] for i in range(0, len(tickers), 150)]
queries = []
for chunk in chunks:
    parts = []
    for t in chunk:
        parts.append("SELECT '{}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(t, t))
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'n_tickers': len(tickers), 'n_chunks': len(chunks), 'queries': queries}))"""

env_args = {'var_call_NZ0JfUmxkUXZtZhMlGbm0tDu': 'file_storage/call_NZ0JfUmxkUXZtZhMlGbm0tDu.json', 'var_call_aTsh1In8HMrOaUxRKitJk4wo': 'file_storage/call_aTsh1In8HMrOaUxRKitJk4wo.json', 'var_call_U9EfGLpOkTlayKj1ozkxcQcY': {'n_tickers': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_call_eXF2jCX9vVN63ZeYWX46HRZb': 'file_storage/call_eXF2jCX9vVN63ZeYWX46HRZb.json'}

exec(code, env_args)
