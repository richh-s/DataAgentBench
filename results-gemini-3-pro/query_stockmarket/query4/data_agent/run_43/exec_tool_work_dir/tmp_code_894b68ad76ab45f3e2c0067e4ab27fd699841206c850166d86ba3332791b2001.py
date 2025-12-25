code = """import json

# Load stockinfo results
with open(locals()['var_function-call-9713228108888965980'], 'r') as f:
    stock_info_list = json.load(f)

# Load stocktrade table list
with open(locals()['var_function-call-4176542361702259114'], 'r') as f:
    table_list = json.load(f)

available_tables = set(table_list)

candidates = []
candidate_map = {}
for entry in stock_info_list:
    sym = entry['Symbol']
    if sym in available_tables:
        candidates.append(sym)
        candidate_map[sym] = entry['Company Description']

# Generate SQL query
# We want to count Up days (Close > Open) and Down days (Close < Open) for 2017
# Date format is assumed YYYY-MM-DD, so LIKE '2017%' works.

subqueries = []
for sym in candidates:
    # Escape double quotes in symbol if any (unlikely for tickers but good practice)
    # Wrap table name in double quotes
    table_name = f'"{sym}"'
    q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM {table_name} WHERE Date LIKE '2017%'"
    subqueries.append(q)

final_query = " UNION ALL ".join(subqueries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-9713228108888965980': 'file_storage/function-call-9713228108888965980.json', 'var_function-call-4176542361702259114': 'file_storage/function-call-4176542361702259114.json', 'var_function-call-13928048968551544209': 234}

exec(code, env_args)
