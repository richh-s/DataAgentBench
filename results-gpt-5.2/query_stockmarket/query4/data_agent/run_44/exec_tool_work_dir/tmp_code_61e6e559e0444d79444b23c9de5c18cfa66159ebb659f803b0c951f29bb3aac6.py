code = """import json, pandas as pd

# Load NYSE non-ETF symbols list from storage (may be a file path)
raw = var_call_gW5kr09FCdAx6MHwi7TXoO9D
if isinstance(raw, str):
    with open(raw, 'r') as f:
        nyse_meta = json.load(f)
else:
    nyse_meta = raw
meta_df = pd.DataFrame(nyse_meta)
meta_df = meta_df.dropna(subset=['Symbol'])
meta_df['Symbol'] = meta_df['Symbol'].astype(str)

# Load trade tables list
tbls_raw = var_call_wqc5pVlWdKE86AW7cN7fAR9N
if isinstance(tbls_raw, str):
    with open(tbls_raw, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = tbls_raw
trade_set = set(trade_tables)

symbols = [s for s in meta_df['Symbol'].unique().tolist() if s in trade_set]

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_vir4K2LyZTSfmZ0HrEUpLbdA': ['stockinfo'], 'var_call_gW5kr09FCdAx6MHwi7TXoO9D': 'file_storage/call_gW5kr09FCdAx6MHwi7TXoO9D.json', 'var_call_wqc5pVlWdKE86AW7cN7fAR9N': 'file_storage/call_wqc5pVlWdKE86AW7cN7fAR9N.json'}

exec(code, env_args)
