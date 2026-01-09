code = """import json, pandas as pd

# load nyse non-etf symbols
nyse_path = var_call_yPLs2L0YRgmwKL8lzGaeaqSW
with open(nyse_path,'r') as f:
    nyse = json.load(f)
nyse_syms = {r['Symbol'] for r in nyse}

# load available trade tables
trade_path = var_call_br1vDKPT5xjIHYIVwjhMix2z
with open(trade_path,'r') as f:
    trade_tables = set(json.load(f))

# intersection
symbols = sorted(list(nyse_syms & trade_tables))

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'n': len(symbols)}))"""

env_args = {'var_call_yPLs2L0YRgmwKL8lzGaeaqSW': 'file_storage/call_yPLs2L0YRgmwKL8lzGaeaqSW.json', 'var_call_br1vDKPT5xjIHYIVwjhMix2z': 'file_storage/call_br1vDKPT5xjIHYIVwjhMix2z.json'}

exec(code, env_args)
