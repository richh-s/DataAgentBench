code = """import json

# Get the list of valid symbols
prev_res = locals()['var_function-call-13496402127410082925']
if isinstance(prev_res, str):
    data = json.loads(prev_res) # It was printed as json string, but stored as string in prev result? 
    # Wait, execute_python prints. The system stores the print output.
    # If the output was a json string, I need to parse it.
    # The previous output was: {"count": 234, "sample": ...}
    pass
else:
    # If it's already a dict (unlikely based on description)
    data = prev_res

# Re-derive the list because the previous output only had a sample
# I need to read the full lists again to be sure I have all 234.
# Re-reading:
stockinfo_path = locals()['var_function-call-2420597473229265013']
with open(stockinfo_path, 'r') as f:
    stock_data = json.load(f)

table_list_path = locals()['var_function-call-310547401484517096']
with open(table_list_path, 'r') as f:
    table_data = json.load(f)

stock_symbols = set(d['Symbol'] for d in stock_data)
# Filter tables that are in stock_symbols
valid_symbols = [t for t in table_data if t in stock_symbols]

# Construct query
queries = []
for sym in valid_symbols:
    # Escape double quotes in symbol if any (unlikely for tickers but good practice)
    # DuckDB quoting: double quotes for identifiers.
    # Only need to worry if symbol has " inside, which is invalid for tickers usually.
    # Tickers can have special chars like ^ or .
    # I'll just wrap in ".
    q = f"""SELECT '{sym}' as Symbol, 
            SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, 
            SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down 
            FROM "{sym}" WHERE Date LIKE '2017-%'"""
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-2420597473229265013': 'file_storage/function-call-2420597473229265013.json', 'var_function-call-310547401484517096': 'file_storage/function-call-310547401484517096.json', 'var_function-call-13496402127410082925': {'count': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_function-call-8579205056495132833': [{'Date': '2019-10-24'}]}

exec(code, env_args)
