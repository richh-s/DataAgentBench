code = """import json

# Load previous results
with open(locals()['var_function-call-16619216267788933502'], 'r') as f:
    candidates = json.load(f)
with open(locals()['var_function-call-7766385081012407064'], 'r') as f:
    tables = json.load(f)

table_set = set(tables)
valid_symbols = [c['Symbol'] for c in candidates if c['Symbol'] in table_set]

chunk_size = 50
chunks = [valid_symbols[i:i + chunk_size] for i in range(0, len(valid_symbols), chunk_size)]

queries = []
for chunk in chunks:
    subqueries = []
    for sym in chunk:
        q = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date LIKE '2017-%'"
        subqueries.append(q)
    queries.append(" UNION ALL ".join(subqueries))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-16619216267788933502': 'file_storage/function-call-16619216267788933502.json', 'var_function-call-7766385081012407064': 'file_storage/function-call-7766385081012407064.json', 'var_function-call-9364681288924485365': 234, 'var_function-call-13310879459313706391': 'file_storage/function-call-13310879459313706391.json'}

exec(code, env_args)
