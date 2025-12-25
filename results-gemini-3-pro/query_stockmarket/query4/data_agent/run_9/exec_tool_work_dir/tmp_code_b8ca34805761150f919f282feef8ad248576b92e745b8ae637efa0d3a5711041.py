code = """import json

path = locals()['var_function-call-2477184406544893280']
with open(path, 'r') as f:
    data = json.load(f)

valid_symbols = data['valid_symbols']
chunk_size = 50
batches = []

part1 = "SELECT '"
part2 = "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down FROM \""
part3 = "\" WHERE Date LIKE '2017-%'"

for i in range(0, len(valid_symbols), chunk_size):
    batch = valid_symbols[i:i+chunk_size]
    queries = []
    for sym in batch:
        q = part1 + sym + part2 + sym + part3
        queries.append(q)
    
    full_query = " UNION ALL ".join(queries)
    batches.append(full_query)

print(f"Number of batches: {len(batches)}")
print("First query preview:")
print(batches[0][:200])

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-4623597435965185168': 'file_storage/function-call-4623597435965185168.json', 'var_function-call-4623597435965183535': 'file_storage/function-call-4623597435965183535.json', 'var_function-call-2477184406544893280': 'file_storage/function-call-2477184406544893280.json', 'var_function-call-956611621751547404': 'file_storage/function-call-956611621751547404.json'}

exec(code, env_args)
