code = """import json
with open(var_call_B94K0khwE25FYcdJAC9uOdh6, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_NQ5Ham37xJsRiDqZHYYtyUqb, 'r') as f:
    trade_tables = json.load(f)

symbols_info = [rec['Symbol'] for rec in stockinfo]
trade_set = set(trade_tables)
common_symbols = [s for s in symbols_info if s in trade_set]
common_symbols.sort()

print('__RESULT__:')
print(json.dumps(common_symbols))"""

env_args = {'var_call_B94K0khwE25FYcdJAC9uOdh6': 'file_storage/call_B94K0khwE25FYcdJAC9uOdh6.json', 'var_call_NQ5Ham37xJsRiDqZHYYtyUqb': 'file_storage/call_NQ5Ham37xJsRiDqZHYYtyUqb.json'}

exec(code, env_args)
