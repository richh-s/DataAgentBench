code = """import json, pandas as pd

# Load NYSE non-ETF symbols + company names
src = var_call_QTlIzelgD7c9YCeCM1DsmgUt
if isinstance(src, str):
    with open(src, 'r') as f:
        nyse = json.load(f)
else:
    nyse = src

tsrc = var_call_AceQkdmru6bj7QFVvVXiKhbC
if isinstance(tsrc, str):
    with open(tsrc, 'r') as f:
        tbls = json.load(f)
else:
    tbls = tsrc

nyse_df = pd.DataFrame(nyse)
tbls_df = pd.DataFrame(tbls)

# Intersection with available price tables
symbols = sorted(set(nyse_df['Symbol']).intersection(set(tbls_df['Symbol'])))

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_QTlIzelgD7c9YCeCM1DsmgUt': 'file_storage/call_QTlIzelgD7c9YCeCM1DsmgUt.json', 'var_call_AceQkdmru6bj7QFVvVXiKhbC': 'file_storage/call_AceQkdmru6bj7QFVvVXiKhbC.json'}

exec(code, env_args)
