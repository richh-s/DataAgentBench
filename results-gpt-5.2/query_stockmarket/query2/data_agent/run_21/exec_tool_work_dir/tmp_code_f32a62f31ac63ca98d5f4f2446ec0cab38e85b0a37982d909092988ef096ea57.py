code = """import json

path = var_call_NZ0JfUmxkUXZtZhMlGbm0tDu
with open(path, 'r', encoding='utf-8') as f:
    etfs = json.load(f)

tables = var_call_aTsh1In8HMrOaUxRKitJk4wo
if isinstance(tables, str):
    with open(tables, 'r', encoding='utf-8') as f:
        tables = json.load(f)

tickers = sorted({r['Symbol'] for r in etfs if r.get('Symbol') in set(tables)})

print('__RESULT__:')
print(json.dumps({'n_tickers': len(tickers), 'sample': tickers[:20]}))"""

env_args = {'var_call_NZ0JfUmxkUXZtZhMlGbm0tDu': 'file_storage/call_NZ0JfUmxkUXZtZhMlGbm0tDu.json', 'var_call_aTsh1In8HMrOaUxRKitJk4wo': 'file_storage/call_aTsh1In8HMrOaUxRKitJk4wo.json'}

exec(code, env_args)
