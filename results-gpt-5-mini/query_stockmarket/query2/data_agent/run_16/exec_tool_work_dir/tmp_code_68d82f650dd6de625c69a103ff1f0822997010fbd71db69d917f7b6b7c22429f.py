code = """import json
with open(var_call_WaEvCHYDu8q5PYvnJxAh1X2s, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_C9yV3KAORv9nL5ONxiYWO0Ud, 'r') as f:
    trade_tables = json.load(f)
symbols = [r['Symbol'] for r in stockinfo]
available_symbols = [s for s in symbols if s in trade_tables]
result = {'available_symbols': available_symbols, 'count_available': len(available_symbols)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7unxnarEaWwSx7trThvVwizq': ['stockinfo'], 'var_call_WaEvCHYDu8q5PYvnJxAh1X2s': 'file_storage/call_WaEvCHYDu8q5PYvnJxAh1X2s.json', 'var_call_C9yV3KAORv9nL5ONxiYWO0Ud': 'file_storage/call_C9yV3KAORv9nL5ONxiYWO0Ud.json'}

exec(code, env_args)
