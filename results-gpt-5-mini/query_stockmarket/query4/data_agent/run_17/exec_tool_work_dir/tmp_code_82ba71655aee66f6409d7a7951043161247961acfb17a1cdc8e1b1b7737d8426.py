code = """import json
# Load the previous tool results from the storage file paths
# var_call_Js61eKeKPd8pJkBCv55jt5nu contains path to JSON of stockinfo query result
# var_call_LbZzmGVobT3Mgm9lwFj5SNHc contains path to JSON of stocktrade list result
with open(var_call_Js61eKeKPd8pJkBCv55jt5nu, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_LbZzmGVobT3Mgm9lwFj5SNHc, 'r') as f:
    trade_tables = json.load(f)
# Build mapping symbol -> company description for NYSE non-ETF entries
sym_to_name = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    desc = rec.get('Company Description')
    # ensure symbol exists in trade tables
    if sym in trade_tables:
        sym_to_name[sym] = desc
# Prepare result list
result = {'symbols': list(sym_to_name.keys()), 'sym_to_name': sym_to_name}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bYQyMqrBbLBPnHo5oOIwzCIP': ['stockinfo'], 'var_call_Js61eKeKPd8pJkBCv55jt5nu': 'file_storage/call_Js61eKeKPd8pJkBCv55jt5nu.json', 'var_call_LbZzmGVobT3Mgm9lwFj5SNHc': 'file_storage/call_LbZzmGVobT3Mgm9lwFj5SNHc.json'}

exec(code, env_args)
