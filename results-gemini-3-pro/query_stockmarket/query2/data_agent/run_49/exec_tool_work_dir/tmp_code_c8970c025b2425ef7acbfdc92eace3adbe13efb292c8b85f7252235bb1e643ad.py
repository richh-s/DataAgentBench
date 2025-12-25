code = """import json

path = locals().get('var_function-call-5113928090904780528')
with open(path, 'r') as f:
    valid_symbols = json.load(f)

batches = []
batch_size = 50
current_batch = []

for sym in valid_symbols:
    # Use simple string concatenation
    q = "SELECT '" + sym + "' as Symbol, MAX(\"Adj Close\") as MaxPrice FROM \"" + sym + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MaxPrice > 200"
    current_batch.append(q)
    if len(current_batch) >= batch_size:
        batches.append(" UNION ALL ".join(current_batch))
        current_batch = []

if len(current_batch) > 0:
    batches.append(" UNION ALL ".join(current_batch))

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-5139739992729438025': 'file_storage/function-call-5139739992729438025.json', 'var_function-call-8590673828826687227': 'file_storage/function-call-8590673828826687227.json', 'var_function-call-5113928090904780528': 'file_storage/function-call-5113928090904780528.json', 'var_function-call-5191216881659803828': 'Done'}

exec(code, env_args)
