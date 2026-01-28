code = """import json
with open(var_call_ew9VLDirbm4RMvpPwbqpbkGx) as f:
    stockinfo = json.load(f)
with open(var_call_XHnP7G8F1ai6OXCc44J1pueW) as f:
    trade_tables = json.load(f)

symbols = [rec['Symbol'] for rec in stockinfo]
trade_set = set(trade_tables)
symbols_in_both = [s for s in symbols if s in trade_set]

print("__RESULT__:")
print(json.dumps(symbols_in_both))"""

env_args = {'var_call_ew9VLDirbm4RMvpPwbqpbkGx': 'file_storage/call_ew9VLDirbm4RMvpPwbqpbkGx.json', 'var_call_XHnP7G8F1ai6OXCc44J1pueW': 'file_storage/call_XHnP7G8F1ai6OXCc44J1pueW.json'}

exec(code, env_args)
