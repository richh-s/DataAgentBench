code = """import json, pandas as pd, os
stockinfo_path = var_call_6IJ97gnR2UJFBusSADOta3S1
with open(stockinfo_path, 'r') as f:
    stockinfo = json.load(f)
trade_symbols_path = var_call_ClBzZxwRmbNznzLwBaUNHlGs
with open(trade_symbols_path, 'r') as f:
    trade_symbols = set(json.load(f))

si_df = pd.DataFrame(stockinfo)
si_df = si_df[si_df['Symbol'].isin(trade_symbols)]

symbols = si_df['Symbol'].tolist()
print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_call_oWJH2e2TESGyf4ocBKpENPsu': 'file_storage/call_oWJH2e2TESGyf4ocBKpENPsu.json', 'var_call_6IJ97gnR2UJFBusSADOta3S1': 'file_storage/call_6IJ97gnR2UJFBusSADOta3S1.json', 'var_call_ClBzZxwRmbNznzLwBaUNHlGs': 'file_storage/call_ClBzZxwRmbNznzLwBaUNHlGs.json'}

exec(code, env_args)
