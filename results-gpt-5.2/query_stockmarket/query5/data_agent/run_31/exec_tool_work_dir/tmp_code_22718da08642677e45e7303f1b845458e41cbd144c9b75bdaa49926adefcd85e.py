code = """import json, pandas as pd

# Load NASDAQ Capital Market symbols
path = var_call_5VDv5iBeOE5vhvQB62TrsIWA
with open(path, 'r') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)
cap_symbols = cap_df['symbol'].dropna().unique().tolist()

# Load available trade tables
path2 = var_call_FrYDajh5fEHjmSKZ3dsDVewJ
with open(path2, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# Symbols that have trade data
symbols = sorted([s for s in cap_symbols if s in tables_set])

# Keep it manageable in SQL by passing an IN list per-query later.
result = {
    'n_cap_symbols': int(len(cap_symbols)),
    'n_symbols_with_trade_data': int(len(symbols)),
    'symbols_with_trade_data': symbols
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5VDv5iBeOE5vhvQB62TrsIWA': 'file_storage/call_5VDv5iBeOE5vhvQB62TrsIWA.json', 'var_call_FrYDajh5fEHjmSKZ3dsDVewJ': 'file_storage/call_FrYDajh5fEHjmSKZ3dsDVewJ.json'}

exec(code, env_args)
