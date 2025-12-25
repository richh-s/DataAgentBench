code = """import json

# Load stockinfo
path_info = locals()['var_function-call-2745503811113855905']
with open(path_info, 'r') as f:
    stock_info = json.load(f)

# Load table list
path_tables = locals()['var_function-call-15628124183444077375']
with open(path_tables, 'r') as f:
    table_list = json.load(f)

table_set = set(table_list)
target_stocks = []
stock_name_map = {}

for s in stock_info:
    sym = s.get('Symbol')
    exchange = s.get('Listing Exchange')
    etf = s.get('ETF')
    
    if exchange == 'N' and etf == 'N':
        if sym in table_set:
            target_stocks.append(sym)
            stock_name_map[sym] = s.get('Company Description')

queries = []
for sym in target_stocks:
    # Escape double quotes in symbol if any (though unlikely for tickers)
    safe_sym = sym.replace('"', '""')
    # Using '2017%' for date matching
    q = f"SELECT '{safe_sym}' as symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as down_days FROM \"{safe_sym}\" WHERE Date LIKE '2017%'"
    queries.append(q)

final_query = " UNION ALL ".join(queries)

result_obj = {
    "query": final_query,
    "stock_name_map": stock_name_map,
    "count": len(target_stocks)
}

print("__RESULT__:")
print(json.dumps(result_obj))"""

env_args = {'var_function-call-2745503811113855905': 'file_storage/function-call-2745503811113855905.json', 'var_function-call-15628124183444077375': 'file_storage/function-call-15628124183444077375.json'}

exec(code, env_args)
