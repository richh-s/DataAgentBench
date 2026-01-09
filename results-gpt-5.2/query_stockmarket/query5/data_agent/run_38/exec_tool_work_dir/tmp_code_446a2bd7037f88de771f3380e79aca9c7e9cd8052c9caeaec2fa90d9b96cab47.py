code = """import json, pandas as pd

path = var_call_H2hcxVjddyl5n2L4MVpMNrjI
with open(path, 'r', encoding='utf-8') as f:
    info = json.load(f)

tickers = sorted({r['Symbol'] for r in info if r.get('Symbol')})

print('__RESULT__:')
print(json.dumps({'tickers': tickers, 'n': len(tickers)}))"""

env_args = {'var_call_H2hcxVjddyl5n2L4MVpMNrjI': 'file_storage/call_H2hcxVjddyl5n2L4MVpMNrjI.json'}

exec(code, env_args)
