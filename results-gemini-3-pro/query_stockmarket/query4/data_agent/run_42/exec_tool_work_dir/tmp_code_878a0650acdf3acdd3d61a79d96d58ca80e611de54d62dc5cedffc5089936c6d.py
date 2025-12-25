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
    
    if etf == 'N':
        if sym in table_set:
            target_stocks.append(sym)
            stock_name_map[sym] = s.get('Company Description', '')

queries = []
sq = chr(39) # single quote
dq = chr(34) # double quote

for sym in target_stocks:
    # SQL: SELECT 'SYM' as symbol, ... FROM "SYM" WHERE Date LIKE '2017%'
    q = "SELECT " + sq + sym + sq + " as symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as down_days FROM " + dq + sym + dq + " WHERE Date LIKE " + sq + "2017%" + sq
    queries.append(q)

final_query = " UNION ALL ".join(queries)

res = {
    "query": final_query,
    "stock_name_map": stock_name_map,
    "count": len(target_stocks)
}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-2745503811113855905': 'file_storage/function-call-2745503811113855905.json', 'var_function-call-15628124183444077375': 'file_storage/function-call-15628124183444077375.json', 'var_function-call-5011260897291684611': {'query': '', 'stock_name_map': {}, 'count': 0}, 'var_function-call-16235586898272906057': 'file_storage/function-call-16235586898272906057.json', 'var_function-call-11764409698490584313': {'preview': "SELECT 'AEFC' as symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as down_days FROM  + sym +  WHERE Date LIKE '2017%' UNION ALL SELECT 'AIN' as symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as down_days FROM  + sym +  WHERE Date LIKE '2017%' UNION ALL SELECT 'AIV' as symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN Close < Open THEN 1 ELS"}, 'var_function-call-16781553813162880461': 'file_storage/function-call-16781553813162880461.json'}

exec(code, env_args)
