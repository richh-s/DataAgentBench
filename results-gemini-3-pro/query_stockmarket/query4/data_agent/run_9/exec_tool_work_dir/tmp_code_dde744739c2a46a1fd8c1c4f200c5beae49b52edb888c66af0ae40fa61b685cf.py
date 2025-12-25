code = """import json

path = locals()['var_function-call-2477184406544893280']
with open(path, 'r') as f:
    data = json.load(f)

valid_symbols = data['valid_symbols']
print(f"Count: {len(valid_symbols)}")

# chunk size
chunk_size = 100
batches = []
for i in range(0, len(valid_symbols), chunk_size):
    batch = valid_symbols[i:i+chunk_size]
    queries = []
    for sym in batch:
        # Wrap symbol in double quotes just in case, though they are usually uppercase letters
        # Date filtering for 2017
        q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down FROM \"{sym}\" WHERE Date LIKE '2017-%'"
        queries.append(q)
    
    full_query = " UNION ALL ".join(queries)
    batches.append(full_query)

print(f"Number of batches: {len(batches)}")
# Print the first batch query to verify
print("First batch query preview:")
print(batches[0][:500] + "...")

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-4623597435965185168': 'file_storage/function-call-4623597435965185168.json', 'var_function-call-4623597435965183535': 'file_storage/function-call-4623597435965183535.json', 'var_function-call-2477184406544893280': 'file_storage/function-call-2477184406544893280.json'}

exec(code, env_args)
