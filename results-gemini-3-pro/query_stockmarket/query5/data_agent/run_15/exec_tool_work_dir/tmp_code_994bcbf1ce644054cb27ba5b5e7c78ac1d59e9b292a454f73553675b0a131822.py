code = """import json

# Get paths
path1 = locals()['var_function-call-14483470659460654413']
path2 = locals()['var_function-call-14483470659460654526']

with open(path1, 'r') as f:
    stock_info = json.load(f)

with open(path2, 'r') as f:
    tables = json.load(f)

target_symbols = [item['Symbol'] for item in stock_info]
valid_symbols = sorted(list(set(target_symbols).intersection(set(tables))))

queries = []
# helpers for quotes
sq = chr(39) # single quote
dq = chr(34) # double quote

for sym in valid_symbols:
    # SELECT 'sym' as Symbol, COUNT(*) as Days FROM "sym" WHERE Date LIKE '2019%' AND (High - Low) > 0.2 * Low
    q = "SELECT " + sq + sym + sq + " as Symbol, COUNT(*) as Days FROM " + dq + sym + dq + " WHERE Date LIKE " + sq + "2019%" + sq + " AND (High - Low) > 0.2 * Low"
    queries.append(q)

final_query = " UNION ALL ".join(queries) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-14483470659460654413': 'file_storage/function-call-14483470659460654413.json', 'var_function-call-14483470659460654526': 'file_storage/function-call-14483470659460654526.json', 'var_function-call-17026473911973201946': {'count': 86, 'first_10': ['DZSI', 'PLIN', 'PEIX', 'CPAH', 'CBAT', 'EXPC', 'CUBA', 'BKYI', 'PBFS', 'SSNT']}, 'var_function-call-12112332931073037359': [{'Date': '2003-11-14', 'Open': '169.25', 'High': '172.5', 'Low': '166.25'}], 'var_function-call-9515048861433129617': 'file_storage/function-call-9515048861433129617.json'}

exec(code, env_args)
