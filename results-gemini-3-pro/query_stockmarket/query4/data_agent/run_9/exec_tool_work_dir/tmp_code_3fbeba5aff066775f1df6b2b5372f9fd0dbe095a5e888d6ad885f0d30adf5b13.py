code = """import json

path = locals()['var_function-call-2477184406544893280']
with open(path, 'r') as f:
    data = json.load(f)

valid_symbols = data['valid_symbols']
chunk_size = 50
batches = []

# Use chr(34) for double quote and chr(39) for single quote to avoid literal issues
q_double = chr(34)
q_single = chr(39)

for i in range(0, len(valid_symbols), chunk_size):
    batch = valid_symbols[i:i+chunk_size]
    queries = []
    for sym in batch:
        # SELECT 'SYM' ... FROM "SYM" ...
        q = "SELECT " + q_single + sym + q_single + " as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down FROM " + q_double + sym + q_double + " WHERE Date LIKE " + q_single + "2017-%" + q_single
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
