code = """import json, pandas as pd

# load nyse non-etf symbols
nyse_path = var_call_ZdWPDvJsiGQUvsbhRsbNAhtY
with open(nyse_path,'r') as f:
    nyse = json.load(f)
nyse_syms = {r['Symbol'] for r in nyse}

# load available trade tables
trade_path = var_call_MTr9gFZz4B2KKNiHop1lrTqq
with open(trade_path,'r') as f:
    trade_tables = json.load(f)
trade_set = set(trade_tables)

syms = sorted(list(nyse_syms & trade_set))
print('__RESULT__:')
print(json.dumps({'symbols': syms, 'count': len(syms)}))"""

env_args = {'var_call_ZdWPDvJsiGQUvsbhRsbNAhtY': 'file_storage/call_ZdWPDvJsiGQUvsbhRsbNAhtY.json', 'var_call_MTr9gFZz4B2KKNiHop1lrTqq': 'file_storage/call_MTr9gFZz4B2KKNiHop1lrTqq.json'}

exec(code, env_args)
