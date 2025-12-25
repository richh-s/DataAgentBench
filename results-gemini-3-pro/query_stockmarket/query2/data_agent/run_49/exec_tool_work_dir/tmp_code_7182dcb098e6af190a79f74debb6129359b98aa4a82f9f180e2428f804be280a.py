code = """import json

path = locals()['var_function-call-3732280635417606766']
with open(path, 'r') as f:
    symbols = json.load(f)

symbols.sort()

queries = []
batch_size = 200
current_batch = []

for s in symbols:
    q = "SELECT '{0}' as Symbol, MAX(\"Adj Close\") as MaxPrice FROM \"{0}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MaxPrice > 200".format(s)
    current_batch.append(q)
    if len(current_batch) >= batch_size:
        queries.append(" UNION ALL ".join(current_batch))
        current_batch = []

if current_batch:
    queries.append(" UNION ALL ".join(current_batch))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-5139739992729438025': 'file_storage/function-call-5139739992729438025.json', 'var_function-call-8590673828826687227': 'file_storage/function-call-8590673828826687227.json', 'var_function-call-5113928090904780528': 'file_storage/function-call-5113928090904780528.json', 'var_function-call-5191216881659803828': 'Done', 'var_function-call-3732280635417606766': 'file_storage/function-call-3732280635417606766.json'}

exec(code, env_args)
