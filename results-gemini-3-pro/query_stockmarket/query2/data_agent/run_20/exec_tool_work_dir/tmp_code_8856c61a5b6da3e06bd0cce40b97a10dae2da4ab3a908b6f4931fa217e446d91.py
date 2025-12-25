code = """import json

# Load valid symbols
with open(locals()['var_function-call-1508129544288372996']) as f:
    data = json.load(f)
    symbols = data['symbols']

queries = []
batch_size = 200
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    subqueries = []
    for sym in batch:
        # Construct query carefully
        # SELECT 'SYM' as Symbol FROM "SYM" WHERE "Adj Close" > 200 AND Date LIKE '2015%' LIMIT 1
        q = "SELECT '" + sym + "' as Symbol FROM \"" + sym + "\" WHERE \"Adj Close\" > 200 AND Date LIKE '2015%' LIMIT 1"
        subqueries.append(q)
    
    full_query = " UNION ALL ".join(subqueries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-8581251308861529440': 'file_storage/function-call-8581251308861529440.json', 'var_function-call-1676637049727952223': 'file_storage/function-call-1676637049727952223.json', 'var_function-call-1508129544288372996': 'file_storage/function-call-1508129544288372996.json'}

exec(code, env_args)
