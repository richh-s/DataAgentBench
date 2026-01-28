code = """import json
with open(var_call_d6OF5lNHFpCkdROe3WXhSEIn, 'r') as f:
    etf_list = json.load(f)
with open(var_call_pWaf7Rt5WZqXxRrWb0Xhaa1p, 'r') as f:
    trade_tables = json.load(f)

etf_symbols = [r['Symbol'] for r in etf_list]
trade_set = set(trade_tables)
common_symbols = [s for s in etf_symbols if s in trade_set]
print("__RESULT__:")
print(json.dumps(common_symbols))"""

env_args = {'var_call_d6OF5lNHFpCkdROe3WXhSEIn': 'file_storage/call_d6OF5lNHFpCkdROe3WXhSEIn.json', 'var_call_pWaf7Rt5WZqXxRrWb0Xhaa1p': 'file_storage/call_pWaf7Rt5WZqXxRrWb0Xhaa1p.json'}

exec(code, env_args)
