code = """import json
# read storage variables
with open(var_call_DBNXkzqyXkU5tq9i7a1T72uH, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_W6eAo72LvMbwCYDhT1jQJ2YJ, 'r') as f:
    trade_tables = json.load(f)
# extract symbols from stockinfo records
symbols_info = [rec['Symbol'] for rec in stockinfo]
# intersect with available trade tables
trade_set = set(trade_tables)
intersection = sorted([s for s in symbols_info if s in trade_set])
output = {'count': len(intersection), 'symbols': intersection}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_DBNXkzqyXkU5tq9i7a1T72uH': 'file_storage/call_DBNXkzqyXkU5tq9i7a1T72uH.json', 'var_call_W6eAo72LvMbwCYDhT1jQJ2YJ': 'file_storage/call_W6eAo72LvMbwCYDhT1jQJ2YJ.json'}

exec(code, env_args)
