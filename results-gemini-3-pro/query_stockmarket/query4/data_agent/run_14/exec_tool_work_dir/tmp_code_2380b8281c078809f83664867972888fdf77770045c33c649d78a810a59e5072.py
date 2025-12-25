code = """import json

k1 = 'var_function-call-2664401347096856404'
k2 = 'var_function-call-14718190706972975468'
p1 = locals().get(k1)
p2 = locals().get(k2)

with open(p1, 'r') as f:
    stock_info = json.load(f)

with open(p2, 'r') as f:
    trade_tables = json.load(f)

trade_set = set(trade_tables)
valid_symbols = []
symbol_map = {}

for item in stock_info:
    sym = item['Symbol']
    if sym in trade_set:
        valid_symbols.append(sym)
        symbol_map[sym] = item['Company Description']

sqls = []
for sym in valid_symbols:
    # Construct SQL
    # Note: Use double quotes for column names in SQL (DuckDB) just in case, though standard columns usually don't need them.
    # The columns are Date, Open, Close.
    # The table name is the symbol.
    q = "SELECT '" + sym + "' as symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) as down_days FROM \"" + sym + "\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'"
    sqls.append(q)

full_query = " UNION ALL ".join(sqls)
final_query = "SELECT symbol, up_days, down_days, (up_days - down_days) as diff FROM (" + full_query + ") WHERE up_days > down_days ORDER BY diff DESC LIMIT 5"

print('__RESULT__:')
print(json.dumps({'query': final_query, 'symbol_map': symbol_map}))"""

env_args = {'var_function-call-2664401347096856404': 'file_storage/function-call-2664401347096856404.json', 'var_function-call-14718190706972975468': 'file_storage/function-call-14718190706972975468.json', 'var_function-call-5783268603279882755': {'count1': 234, 'count2': 2753}}

exec(code, env_args)
