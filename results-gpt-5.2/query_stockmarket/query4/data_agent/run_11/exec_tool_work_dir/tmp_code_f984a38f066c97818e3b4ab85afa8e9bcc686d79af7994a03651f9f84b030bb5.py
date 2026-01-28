code = """import json, pandas as pd

# Load NYSE non-ETF symbols
src = var_call_Ccu3gVLBYmt6aODTNoRLYShv
if isinstance(src, str):
    with open(src, 'r') as f:
        nyse = json.load(f)
else:
    nyse = src
nyse_df = pd.DataFrame(nyse)

# Load available trade tables
tbl_src = var_call_Vuu3fiiPc3q8j0Wv61fKeY8b
if isinstance(tbl_src, str):
    with open(tbl_src, 'r') as f:
        tables = json.load(f)
else:
    tables = tbl_src
trade_set = set(tables)

# Keep only symbols that have trade tables
nyse_df = nyse_df[nyse_df['symbol'].isin(trade_set)].copy()

# Return symbol list in chunks to query in SQL later (avoid huge SQL IN lists)
symbols = nyse_df['symbol'].tolist()
res = {
    'n_symbols': len(symbols),
    'symbols': symbols,
    'company_map': dict(zip(nyse_df['symbol'], nyse_df['company_name']))
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_Ccu3gVLBYmt6aODTNoRLYShv': 'file_storage/call_Ccu3gVLBYmt6aODTNoRLYShv.json', 'var_call_Vuu3fiiPc3q8j0Wv61fKeY8b': 'file_storage/call_Vuu3fiiPc3q8j0Wv61fKeY8b.json'}

exec(code, env_args)
