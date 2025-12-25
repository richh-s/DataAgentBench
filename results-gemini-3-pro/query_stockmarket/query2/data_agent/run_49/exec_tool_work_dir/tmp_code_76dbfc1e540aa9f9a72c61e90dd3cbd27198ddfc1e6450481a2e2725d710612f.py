code = """import json

file_path = locals()['var_function-call-5113928090904780528']
with open(file_path, 'r') as f:
    valid_symbols = json.load(f)

print("Count:", len(valid_symbols))

batches = []
batch_size = 100
current_batch = []

for sym in valid_symbols:
    # Construct query string safely
    # Query: SELECT 'SYM' as Symbol, MAX("Adj Close") as MaxPrice FROM "SYM" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MaxPrice > 200
    q = "SELECT '" + sym + "' as Symbol, MAX(\"Adj Close\") as MaxPrice FROM \"" + sym + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MaxPrice > 200"
    current_batch.append(q)
    if len(current_batch) >= batch_size:
        batches.append(" UNION ALL ".join(current_batch))
        current_batch = []

if current_batch:
    batches.append(" UNION ALL ".join(current_batch))

print("Number of batches:", len(batches))

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-5139739992729438025': 'file_storage/function-call-5139739992729438025.json', 'var_function-call-8590673828826687227': 'file_storage/function-call-8590673828826687227.json', 'var_function-call-5113928090904780528': 'file_storage/function-call-5113928090904780528.json'}

exec(code, env_args)
