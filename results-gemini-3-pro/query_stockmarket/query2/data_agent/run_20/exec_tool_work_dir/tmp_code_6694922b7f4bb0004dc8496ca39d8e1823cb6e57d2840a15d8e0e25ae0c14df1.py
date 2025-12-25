code = """import json

with open(locals()['var_function-call-1508129544288372996']) as f:
    data = json.load(f)
    symbols = data['symbols']

queries = []
batch_size = 50
dq = chr(34)
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    subqueries = []
    for sym in batch:
        q = "SELECT '" + sym + "' as Symbol FROM " + dq + sym + dq + " WHERE " + dq + "Adj Close" + dq + " > 200 AND Date LIKE '2015%' LIMIT 1"
        subqueries.append(q)
    
    full_query = " UNION ALL ".join(subqueries)
    queries.append(full_query)

# Save all queries
with open('queries_50.json', 'w') as f:
    json.dump(queries, f)

# Print first 5
print("__RESULT__:")
print(json.dumps(queries[:5]))"""

env_args = {'var_function-call-8581251308861529440': 'file_storage/function-call-8581251308861529440.json', 'var_function-call-1676637049727952223': 'file_storage/function-call-1676637049727952223.json', 'var_function-call-1508129544288372996': 'file_storage/function-call-1508129544288372996.json', 'var_function-call-3424350687941908327': 'file_storage/function-call-3424350687941908327.json', 'var_function-call-9687718414884459442': 'file_storage/function-call-9687718414884459442.json', 'var_function-call-6699271192767326831': {'num_batches': 15, 'len_batch_0': 9933}}

exec(code, env_args)
