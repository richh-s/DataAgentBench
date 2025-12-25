code = """import json

# Load stockinfo results
with open(locals()['var_function-call-9713228108888965980'], 'r') as f:
    stock_info_list = json.load(f)

# Load stocktrade table list
with open(locals()['var_function-call-4176542361702259114'], 'r') as f:
    table_list = json.load(f)

available_tables = set(table_list)

candidates = []
for entry in stock_info_list:
    sym = entry['Symbol']
    if sym in available_tables:
        candidates.append(sym)

# Chunking
chunk_size = 50
chunks = [candidates[i:i + chunk_size] for i in range(0, len(candidates), chunk_size)]

queries = []
for chunk in chunks:
    subqueries = []
    for sym in chunk:
        table_name = f'"{sym}"'
        q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM {table_name} WHERE Date LIKE '2017%'"
        subqueries.append(q)
    queries.append(" UNION ALL ".join(subqueries))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-9713228108888965980': 'file_storage/function-call-9713228108888965980.json', 'var_function-call-4176542361702259114': 'file_storage/function-call-4176542361702259114.json', 'var_function-call-13928048968551544209': 234, 'var_function-call-18070296961767226041': 'file_storage/function-call-18070296961767226041.json'}

exec(code, env_args)
