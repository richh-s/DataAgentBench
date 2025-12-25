code = """import json

key_info = 'var_function-call-2745503811113855905'
key_tables = 'var_function-call-15628124183444077375'

path_info = locals()[key_info]
path_tables = locals()[key_tables]

with open(path_info, 'r') as f:
    stock_info = json.load(f)

with open(path_tables, 'r') as f:
    table_list = json.load(f)

table_set = set(table_list)
target_stocks = []
stock_name_map = {}

for s in stock_info:
    sym = s.get('Symbol', '')
    etf = s.get('ETF', '')
    
    # Stock info is already filtered by Listing Exchange = 'N' in the SQL query.
    # We just need to filter non-ETFs and check existence in stocktrade_database.
    if etf == 'N':
        if sym in table_set:
            target_stocks.append(sym)
            stock_name_map[sym] = s.get('Company Description', '')

queries = []
for sym in target_stocks:
    part1 = "SELECT '" + sym + "' as symbol, "
    part2 = "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as up_days, "
    part3 = "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as down_days "
    part4 = "FROM \"" + sym + "\" WHERE Date LIKE '2017%'"
    queries.append(part1 + part2 + part3 + part4)

final_query = " UNION ALL ".join(queries)

res = {
    "query": final_query,
    "stock_name_map": stock_name_map,
    "count": len(target_stocks)
}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-2745503811113855905': 'file_storage/function-call-2745503811113855905.json', 'var_function-call-15628124183444077375': 'file_storage/function-call-15628124183444077375.json', 'var_function-call-5011260897291684611': {'query': '', 'stock_name_map': {}, 'count': 0}}

exec(code, env_args)
