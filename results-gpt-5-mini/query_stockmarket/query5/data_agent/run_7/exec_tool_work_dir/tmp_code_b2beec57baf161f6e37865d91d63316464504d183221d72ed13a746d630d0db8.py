code = """import json
val1 = var_call_g29DMfGZ1F5iPmMFwe0rGJmZ
if isinstance(val1, str) and val1.endswith('.json'):
    with open(val1, 'r') as f:
        stockinfo = json.load(f)
else:
    stockinfo = val1
val2 = var_call_NxAzjzgAprbtYGql6TUtUGiP
if isinstance(val2, str) and val2.endswith('.json'):
    with open(val2, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = val2

symbols_s = [rec['Symbol'] for rec in stockinfo if rec.get('Symbol')]
trade_set = set(trade_tables)
common = [s for s in symbols_s if s in trade_set]

# build mapping symbol -> company description
mapping = {rec['Symbol']: rec.get('Company Description','') for rec in stockinfo if rec.get('Symbol') in common}

out = {'symbols': common, 'mapping': mapping}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_g29DMfGZ1F5iPmMFwe0rGJmZ': 'file_storage/call_g29DMfGZ1F5iPmMFwe0rGJmZ.json', 'var_call_NxAzjzgAprbtYGql6TUtUGiP': 'file_storage/call_NxAzjzgAprbtYGql6TUtUGiP.json'}

exec(code, env_args)
