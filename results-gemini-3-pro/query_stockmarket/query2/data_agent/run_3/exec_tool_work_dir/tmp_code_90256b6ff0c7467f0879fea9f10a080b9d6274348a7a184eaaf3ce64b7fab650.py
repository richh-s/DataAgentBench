code = """import json

file_path = locals()['var_function-call-2951448566390777149']

with open(file_path, 'r') as f:
    data = json.load(f)

symbols = data['symbols']
queries = []
chunk_size = 200
dq = chr(34) # double quote

current_chunk = []
for sym in symbols:
    current_chunk.append(sym)
    if len(current_chunk) >= chunk_size:
        parts = []
        for s in current_chunk:
            # query: SELECT 'SYM' as Symbol FROM "SYM" WHERE ...
            q = "SELECT '" + s + "' as Symbol FROM " + dq + s + dq + " WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND " + dq + "Adj Close" + dq + " > 200 LIMIT 1"
            parts.append(q)
        queries.append(" UNION ALL ".join(parts))
        current_chunk = []

if current_chunk:
    parts = []
    for s in current_chunk:
        q = "SELECT '" + s + "' as Symbol FROM " + dq + s + dq + " WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND " + dq + "Adj Close" + dq + " > 200 LIMIT 1"
        parts.append(q)
    queries.append(" UNION ALL ".join(parts))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-14301945511223140359': 'file_storage/function-call-14301945511223140359.json', 'var_function-call-6882633768806362112': 'file_storage/function-call-6882633768806362112.json', 'var_function-call-2951448566390777149': 'file_storage/function-call-2951448566390777149.json', 'var_function-call-4592447069327499722': [{'Date': '2018-08-15'}]}

exec(code, env_args)
