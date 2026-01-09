code = """import json, pandas as pd

# load symbols list from file if needed
sym_data = var_call_mO6KgQoztucnkZrYAtJwnebP
if isinstance(sym_data, str):
    with open(sym_data, 'r') as f:
        sym_data = json.load(f)

symbols = sorted({r['Symbol'] for r in sym_data if r.get('Symbol')})

# Build a UNION ALL query across existing ticker tables for 2019 with condition (High-Low)/Low > 0.2
# Need to check which symbol tables exist in stocktrade_database

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'n': len(symbols)}))"""

env_args = {'var_call_mO6KgQoztucnkZrYAtJwnebP': 'file_storage/call_mO6KgQoztucnkZrYAtJwnebP.json'}

exec(code, env_args)
