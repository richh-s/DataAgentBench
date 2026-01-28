code = """import json
with open(var_call_aCAbdB3jQgRTH8mqdp5wsMj6, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_tJA9EW3OouFCqMIGZNLFpvYc, 'r') as f:
    trade_tables = json.load(f)

symbols_info = [r['Symbol'] for r in stockinfo]
available_symbols = [s for s in symbols_info if s in trade_tables]

out = {'num_stockinfo_symbols': len(symbols_info), 'num_available': len(available_symbols), 'available_sample': available_symbols[:20]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_aCAbdB3jQgRTH8mqdp5wsMj6': 'file_storage/call_aCAbdB3jQgRTH8mqdp5wsMj6.json', 'var_call_tJA9EW3OouFCqMIGZNLFpvYc': 'file_storage/call_tJA9EW3OouFCqMIGZNLFpvYc.json'}

exec(code, env_args)
