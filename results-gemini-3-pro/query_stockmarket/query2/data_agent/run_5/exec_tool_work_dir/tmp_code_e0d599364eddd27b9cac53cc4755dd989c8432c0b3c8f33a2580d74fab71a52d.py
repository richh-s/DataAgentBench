code = """import json

path = locals()['var_function-call-11973061372010644575']
with open(path, 'r') as f:
    symbols = json.load(f)

queries = []
for s in symbols:
    # Python string enclosed in double quotes
    # SQL string uses single quotes for literals and double quotes for identifiers
    # We need to escape the double quotes inside the python string
    q = "SELECT '%s' as Symbol FROM \"%s\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1" % (s, s)
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-16341739704993987166': 'file_storage/function-call-16341739704993987166.json', 'var_function-call-17860090179265240781': 'file_storage/function-call-17860090179265240781.json', 'var_function-call-11973061372010644575': 'file_storage/function-call-11973061372010644575.json', 'var_function-call-16861433214838265826': 1435, 'var_function-call-2000411894810468263': 'test', 'var_function-call-12527035195204984051': 1435}

exec(code, env_args)
