code = """import json

with open(var_call_NZ0JfUmxkUXZtZhMlGbm0tDu, 'r', encoding='utf-8') as f:
    etfs = json.load(f)

with open(var_call_eXF2jCX9vVN63ZeYWX46HRZb, 'r', encoding='utf-8') as f:
    tables = json.load(f)

tables_set = {r['table_name'] for r in tables}

tickers = sorted({r['Symbol'] for r in etfs if r.get('Symbol') in tables_set})

print('__RESULT__:')
print(json.dumps(tickers[:5]))"""

env_args = {'var_call_NZ0JfUmxkUXZtZhMlGbm0tDu': 'file_storage/call_NZ0JfUmxkUXZtZhMlGbm0tDu.json', 'var_call_aTsh1In8HMrOaUxRKitJk4wo': 'file_storage/call_aTsh1In8HMrOaUxRKitJk4wo.json', 'var_call_U9EfGLpOkTlayKj1ozkxcQcY': {'n_tickers': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_call_eXF2jCX9vVN63ZeYWX46HRZb': 'file_storage/call_eXF2jCX9vVN63ZeYWX46HRZb.json'}

exec(code, env_args)
