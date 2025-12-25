code = """import json

key = 'var_function-call-13205512608983909052'
path = locals()[key]
with open(path, 'r') as f:
    symbols = json.load(f)

batches = []
current_batch = []
for s in symbols:
    current_batch.append(s)
    if len(current_batch) >= 200:
        batches.append(current_batch)
        current_batch = []
if current_batch:
    batches.append(current_batch)

queries = []
d1 = "2015-01-01"
d2 = "2015-12-31"
dq = chr(34) # double quote

for batch in batches:
    parts = []
    for s in batch:
        part = "SELECT '" + s + "' as Sym FROM " + dq + s + dq + " WHERE " + dq + "Adj Close" + dq + " > 200 AND Date >= '" + d1 + "' AND Date <= '" + d2 + "' LIMIT 1"
        parts.append(part)
    q = " UNION ALL ".join(parts)
    queries.append(q)

print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_function-call-4965379198154257053': ['stockinfo'], 'var_function-call-7361389423706829961': 'file_storage/function-call-7361389423706829961.json', 'var_function-call-2696260633542718629': 'file_storage/function-call-2696260633542718629.json', 'var_function-call-12571622607259600225': 'file_storage/function-call-12571622607259600225.json', 'var_function-call-13205512608983909052': 'file_storage/function-call-13205512608983909052.json', 'var_function-call-4912288642378271924': 'test', 'var_function-call-13122600800845119992': 'OK'}

exec(code, env_args)
