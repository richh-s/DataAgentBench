code = """import json, pandas as pd
symbols_info = json.load(open(var_call_NtV0ylhLgiw0Jdmpd0RZCe9O))
nyse_symbols = [row['Symbol'] for row in symbols_info]
trade_tables = json.load(open(var_call_LZrArnqQ3hWDEAwcrfaZCoM5))
common_syms = sorted(set(nyse_symbols).intersection(trade_tables))
selected = common_syms[:200]
json.dump(selected, open('selected_syms.json','w'))
print('__RESULT__:')
print(json.dumps({'count': len(common_syms), 'sample': selected[:10]}))"""

env_args = {'var_call_LZrArnqQ3hWDEAwcrfaZCoM5': 'file_storage/call_LZrArnqQ3hWDEAwcrfaZCoM5.json', 'var_call_NtV0ylhLgiw0Jdmpd0RZCe9O': 'file_storage/call_NtV0ylhLgiw0Jdmpd0RZCe9O.json'}

exec(code, env_args)
