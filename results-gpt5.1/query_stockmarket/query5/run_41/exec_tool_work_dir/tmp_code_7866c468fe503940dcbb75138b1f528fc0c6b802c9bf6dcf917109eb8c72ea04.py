code = """import json, pandas as pd
# load full results
with open(var_call_l6S6YV8up1Aj1G0Novs0qmMZ, 'r') as f:
    stockinfo_rows = json.load(f)
symbols_info = pd.DataFrame(stockinfo_rows)
with open(var_call_waxBfkre9FwRVcLW4RCJmTxC, 'r') as f:
    all_tables = json.load(f)
tradable = [s for s in symbols_info['Symbol'] if s in all_tables]
symbols_info = symbols_info[symbols_info['Symbol'].isin(tradable)].reset_index(drop=True)
result = symbols_info['Symbol'].tolist()
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_waxBfkre9FwRVcLW4RCJmTxC': 'file_storage/call_waxBfkre9FwRVcLW4RCJmTxC.json', 'var_call_l6S6YV8up1Aj1G0Novs0qmMZ': 'file_storage/call_l6S6YV8up1Aj1G0Novs0qmMZ.json'}

exec(code, env_args)
