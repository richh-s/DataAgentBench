code = """import json, pandas as pd

# load nyse non-etf symbols list
nyse_path = var_call_9CPAqMh5hMS1MUgyR7EUmPy4
with open(nyse_path, 'r') as f:
    nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)
nyse_syms = set(nyse_df['Symbol'].astype(str))

# load trade tables list
trade_path = var_call_ZTu1dibHgCDNzSy8ZmBcmlGI
with open(trade_path, 'r') as f:
    trade_tables = json.load(f)
trade_syms = set(trade_tables)

syms = sorted(nyse_syms & trade_syms)
# limit to 5 with most up-minus-down in 2017; compute per symbol via SQL in duckdb later
print('__RESULT__:')
print(json.dumps({'symbols': syms, 'count': len(syms)}))"""

env_args = {'var_call_9CPAqMh5hMS1MUgyR7EUmPy4': 'file_storage/call_9CPAqMh5hMS1MUgyR7EUmPy4.json', 'var_call_ZTu1dibHgCDNzSy8ZmBcmlGI': 'file_storage/call_ZTu1dibHgCDNzSy8ZmBcmlGI.json'}

exec(code, env_args)
