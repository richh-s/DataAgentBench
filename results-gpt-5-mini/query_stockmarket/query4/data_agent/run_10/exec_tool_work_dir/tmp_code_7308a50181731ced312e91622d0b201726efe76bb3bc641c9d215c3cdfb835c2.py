code = """import json
with open(var_call_f1r85XmWDTSl5Ddo53iy59CI) as f:
    data = json.load(f)
syms = [rec['Symbol'] for rec in data if rec.get('Listing Exchange') == 'N' and (rec.get('ETF') is None or rec.get('ETF') != 'Y')]
print('__RESULT__:')
print(json.dumps(syms))"""

env_args = {'var_call_f1r85XmWDTSl5Ddo53iy59CI': 'file_storage/call_f1r85XmWDTSl5Ddo53iy59CI.json', 'var_call_6Z6sS3PLvRX8NaXWX42bHpQu': 'file_storage/call_6Z6sS3PLvRX8NaXWX42bHpQu.json'}

exec(code, env_args)
