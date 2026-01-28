code = """import json
# read the two stored files from previous queries
with open(var_call_Nnffy5WqwlKBUYMC5Opf1NhG, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_CS7wPfP4rUVF9gBDQtifhV7n, 'r') as f:
    trade_tables = json.load(f)
# get symbols from stockinfo where Market Category S
symbols = [rec['Symbol'] for rec in stockinfo]
# intersect with trade_tables
trade_set = set(trade_tables)
symbols_in_trade = [s for s in symbols if s in trade_set]
# print result as JSON string
import json
print('__RESULT__:')
print(json.dumps(symbols_in_trade))"""

env_args = {'var_call_Nnffy5WqwlKBUYMC5Opf1NhG': 'file_storage/call_Nnffy5WqwlKBUYMC5Opf1NhG.json', 'var_call_CS7wPfP4rUVF9gBDQtifhV7n': 'file_storage/call_CS7wPfP4rUVF9gBDQtifhV7n.json'}

exec(code, env_args)
