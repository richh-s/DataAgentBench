code = """import json

path = locals()['var_function-call-10141947115754413206']
with open(path, 'r') as f:
    etfs = json.load(f)['etfs']

queries = []
chunk_size = 400
d_start = "2015-01-01"
d_end = "2015-12-31"
q = chr(34) # double quote

i = 0
n = len(etfs)
while i < n:
    chunk = etfs[i : i + chunk_size]
    parts = []
    for s in chunk:
        # (SELECT 's' as Symbol FROM "s" WHERE ... LIMIT 1)
        query_str = "(SELECT '" + s + "' as Symbol FROM " + q + s + q + " WHERE Date >= '" + d_start + "' AND Date <= '" + d_end + "' AND " + q + "Adj Close" + q + " > 200 LIMIT 1)"
        parts.append(query_str)
    queries.append(" UNION ALL ".join(parts))
    i += chunk_size

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-3498236825446053099': 'file_storage/function-call-3498236825446053099.json', 'var_function-call-17765899317089105745': 'file_storage/function-call-17765899317089105745.json', 'var_function-call-10141947115754413206': 'file_storage/function-call-10141947115754413206.json', 'var_function-call-741459784411179294': 'test', 'var_function-call-7809123985342749198': 'file_storage/function-call-7809123985342749198.json', 'var_function-call-10055699509827202705': 'file_storage/function-call-10055699509827202705.json'}

exec(code, env_args)
