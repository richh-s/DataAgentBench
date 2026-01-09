code = """import json
from pathlib import Path

# load tickers
obj = json.loads(Path(var_call_swtzwSQ1S4sF4VjwNFnli5ws).read_text())
tickers = [d['Symbol'] for d in obj['tickers']]
# load available tables
avail = json.loads(Path(var_call_jsXvi8EahP2fQEcI3BU84UB5).read_text())
avail_set = set(avail)
inter = [t for t in tickers if t in avail_set]
print('__RESULT__:')
print(json.dumps({'tickers_in_trade_db': inter, 'n': len(inter), 'missing': len(tickers)-len(inter)}))"""

env_args = {'var_call_Wpf4IymfEgb0zEcD2bqrB3Mg': 'file_storage/call_Wpf4IymfEgb0zEcD2bqrB3Mg.json', 'var_call_swtzwSQ1S4sF4VjwNFnli5ws': 'file_storage/call_swtzwSQ1S4sF4VjwNFnli5ws.json', 'var_call_jsXvi8EahP2fQEcI3BU84UB5': 'file_storage/call_jsXvi8EahP2fQEcI3BU84UB5.json'}

exec(code, env_args)
