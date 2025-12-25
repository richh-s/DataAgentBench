code = """import json

# Use get to be safe
path1 = locals().get('var_function-call-2664401347096856404')
path2 = locals().get('var_function-call-14718190706972975468')

with open(path1, 'r') as f:
    stock_info = json.load(f)

with open(path2, 'r') as f:
    trade_tables = json.load(f)

trade_table_set = set(trade_tables)
valid_symbols = []
symbol_map = {}

for item in stock_info:
    sym = item['Symbol']
    if sym in trade_table_set:
        valid_symbols.append(sym)
        symbol_map[sym] = item['Company Description']

sqls = []
for sym in valid_symbols:
    # Construct query parts safely
    part = 'SELECT \'' + sym + '\' as symbol, SUM(CASE WHEN "Close" > "Open" THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN "Close" < "Open" THEN 1 ELSE 0 END) as down_days FROM "' + sym + '" WHERE "Date" >= \'2017-01-01\' AND "Date" <= \'2017-12-31\''
    sqls.append(part)

full_query = ' UNION ALL '.join(sqls)
# Check length
if len(full_query) > 1000000: # Arbitrary limit
    # If too long, maybe take first 500? No, we need top 5.
    # We rely on DuckDB handling it.
    pass

final_query = 'SELECT symbol, up_days, down_days, (up_days - down_days) as diff FROM (' + full_query + ') WHERE up_days > down_days ORDER BY diff DESC LIMIT 5'

print('__RESULT__:')
print(json.dumps({'query': final_query, 'symbol_map': symbol_map}))"""

env_args = {'var_function-call-2664401347096856404': 'file_storage/function-call-2664401347096856404.json', 'var_function-call-14718190706972975468': 'file_storage/function-call-14718190706972975468.json'}

exec(code, env_args)
