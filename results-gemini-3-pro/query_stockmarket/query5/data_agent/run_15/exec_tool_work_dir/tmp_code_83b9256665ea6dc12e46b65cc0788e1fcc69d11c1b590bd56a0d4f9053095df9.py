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

# Split into 2 batches
mid = len(valid_symbols) // 2
batch1 = valid_symbols[:mid]
batch2 = valid_symbols[mid:]

sq = chr(39)
dq = chr(34)

queries = []
for batch in [batch1, batch2]:
    sub_queries = []
    for sym in batch:
        q = "SELECT " + sq + sym + sq + " as Symbol, COUNT(*) as Days FROM " + dq + sym + dq + " WHERE Date LIKE " + sq + "2019%" + sq + " AND (High - Low) > 0.2 * Low"
        sub_queries.append(q)
    full_q = " UNION ALL ".join(sub_queries)
    queries.append(full_q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-14483470659460654413': 'file_storage/function-call-14483470659460654413.json', 'var_function-call-14483470659460654526': 'file_storage/function-call-14483470659460654526.json', 'var_function-call-17026473911973201946': {'count': 86, 'first_10': ['DZSI', 'PLIN', 'PEIX', 'CPAH', 'CBAT', 'EXPC', 'CUBA', 'BKYI', 'PBFS', 'SSNT']}, 'var_function-call-12112332931073037359': [{'Date': '2003-11-14', 'Open': '169.25', 'High': '172.5', 'Low': '166.25'}], 'var_function-call-9515048861433129617': 'file_storage/function-call-9515048861433129617.json', 'var_function-call-3190209440704312918': 'file_storage/function-call-3190209440704312918.json', 'var_function-call-1689569685408152486': 'file_storage/function-call-1689569685408152486.json'}

exec(code, env_args)
