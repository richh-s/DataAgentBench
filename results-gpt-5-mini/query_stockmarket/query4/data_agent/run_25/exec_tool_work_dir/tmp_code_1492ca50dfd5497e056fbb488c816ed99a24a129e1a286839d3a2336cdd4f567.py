code = """import json
# var_call_Siv61kM1ZxxjZL6JwTXRBBKD and var_call_o5pJhfiSiYi7fwlfUC1c4YWm are available
with open(var_call_Siv61kM1ZxxjZL6JwTXRBBKD, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_o5pJhfiSiYi7fwlfUC1c4YWm, 'r') as f:
    trade_tables = json.load(f)

symbols_stockinfo = [rec['Symbol'] for rec in stockinfo]
# intersection
symbols_in_trade = [s for s in symbols_stockinfo if s in trade_tables]

# output the list
result = {'count_stockinfo_symbols': len(symbols_stockinfo), 'count_intersection': len(symbols_in_trade), 'symbols': symbols_in_trade}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Siv61kM1ZxxjZL6JwTXRBBKD': 'file_storage/call_Siv61kM1ZxxjZL6JwTXRBBKD.json', 'var_call_o5pJhfiSiYi7fwlfUC1c4YWm': 'file_storage/call_o5pJhfiSiYi7fwlfUC1c4YWm.json'}

exec(code, env_args)
