code = """import json

# Get file path
file_path = locals()['var_function-call-2951448566390777149']

# Load data
with open(file_path, 'r') as f:
    data = json.load(f)

symbols = data['symbols']
chunks = []
chunk_size = 300
for i in range(0, len(symbols), chunk_size):
    chunks.append(symbols[i:i+chunk_size])

queries = []
for chunk in chunks:
    sub_queries = []
    for sym in chunk:
        # Quote symbol just in case, though they seem to be standard
        q = f"SELECT '{sym}' as Symbol FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
        sub_queries.append(q)
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-14301945511223140359': 'file_storage/function-call-14301945511223140359.json', 'var_function-call-6882633768806362112': 'file_storage/function-call-6882633768806362112.json', 'var_function-call-2951448566390777149': 'file_storage/function-call-2951448566390777149.json', 'var_function-call-4592447069327499722': [{'Date': '2018-08-15'}]}

exec(code, env_args)
