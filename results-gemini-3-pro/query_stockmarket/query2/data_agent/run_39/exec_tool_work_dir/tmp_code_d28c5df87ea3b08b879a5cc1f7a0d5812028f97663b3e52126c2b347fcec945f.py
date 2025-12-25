code = """import json

path = locals()['var_function-call-10141947115754413206']
with open(path, 'r') as f:
    etfs = json.load(f)['etfs']

queries = []
chunk_size = 400
for i in range(0, len(etfs), chunk_size):
    chunk = etfs[i:i+chunk_size]
    parts = []
    for s in chunk:
        part = 'SELECT \'' + s + '\' as Symbol FROM "' + s + '" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1'
        parts.append(part)
    queries.append(" UNION ALL ".join(parts))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-3498236825446053099': 'file_storage/function-call-3498236825446053099.json', 'var_function-call-17765899317089105745': 'file_storage/function-call-17765899317089105745.json', 'var_function-call-10141947115754413206': 'file_storage/function-call-10141947115754413206.json', 'var_function-call-741459784411179294': 'test'}

exec(code, env_args)
