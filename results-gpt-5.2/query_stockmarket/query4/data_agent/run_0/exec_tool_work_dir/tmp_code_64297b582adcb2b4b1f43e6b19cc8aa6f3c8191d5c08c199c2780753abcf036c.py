code = """import json, pandas as pd

# Load NYSE non-ETF symbols list
src = var_call_hFq6I53XeNlAkxnEkZP1xzrx
if isinstance(src, str):
    with open(src, 'r') as f:
        nyse_nonetf = json.load(f)
else:
    nyse_nonetf = src

# Load available trade tables
src2 = var_call_CfjeqRGQmPapUxnTCX4sKbdF
if isinstance(src2, str):
    with open(src2, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = src2

nyse_df = pd.DataFrame(nyse_nonetf)
nyse_symbols = set(nyse_df['Symbol'].astype(str))
trade_set = set(trade_tables)
syms = sorted(list(nyse_symbols.intersection(trade_set)))

# Return list for next step
result = json.dumps({'symbols': syms, 'n': len(syms)})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_hFq6I53XeNlAkxnEkZP1xzrx': 'file_storage/call_hFq6I53XeNlAkxnEkZP1xzrx.json', 'var_call_CfjeqRGQmPapUxnTCX4sKbdF': 'file_storage/call_CfjeqRGQmPapUxnTCX4sKbdF.json'}

exec(code, env_args)
