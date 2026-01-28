code = """import json

with open(var_call_NZ0JfUmxkUXZtZhMlGbm0tDu, 'r', encoding='utf-8') as f:
    etfs = json.load(f)

tickers = sorted({r['Symbol'] for r in etfs})

# Build 2015-over-200 predicate per ticker using Close (no quoting issues)
chunks = [tickers[i:i+120] for i in range(0, len(tickers), 120)]
queries = []
for chunk in chunks:
    parts = []
    for t in chunk:
        parts.append("SELECT '{}' AS symbol, MAX(Close) AS max_close_2015 FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(t, t))
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'n_tickers': len(tickers), 'n_chunks': len(chunks), 'queries': queries}))"""

env_args = {'var_call_NZ0JfUmxkUXZtZhMlGbm0tDu': 'file_storage/call_NZ0JfUmxkUXZtZhMlGbm0tDu.json', 'var_call_aTsh1In8HMrOaUxRKitJk4wo': 'file_storage/call_aTsh1In8HMrOaUxRKitJk4wo.json', 'var_call_U9EfGLpOkTlayKj1ozkxcQcY': {'n_tickers': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_call_eXF2jCX9vVN63ZeYWX46HRZb': 'file_storage/call_eXF2jCX9vVN63ZeYWX46HRZb.json', 'var_call_idLqIfVWfUT0SaiEtbRhgVzc': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_call_7b54IpID7GntJHh06TKnktb1': [{'symbol': 'AAAU', 'max_adj_close_2015': 'nan'}], 'var_call_sQVD6FKG4ELMbhSXVMWrgtPO': "SELECT 'AAAU' AS symbol", 'var_call_DU7qi2lOvmjq70kT21Gv6GLm': "SELECT 'AAAU' AS symbol, MAX('x') AS m", 'var_call_fqoW3iUFP5BUE6wkKAkaRu3q': [{'symbol': 'AADR', 'max_adj_close_2015': '39.58057403564453'}], 'var_call_ZrL7MmPrCSAeMZ2pMbzwB1yY': 'MAX("Adj Close")', 'var_call_vJnScincntnL8B0dCZQ5ewYV': "SELECT 'AAAU' AS symbol", 'var_call_cSniBx6XZ1yqDe28nTa3KOX4': 'MAX("Close")', 'var_call_apU9WgAdyS7dkMpBrAiE7jOj': "SELECT 'AAAU' AS symbol, MAX(Close) AS m", 'var_call_G0Zl01pj7SZ3X4kOlSrFVsrb': [{'symbol': 'AADR', 'max_adj_close_2015': 'nan'}]}

exec(code, env_args)
