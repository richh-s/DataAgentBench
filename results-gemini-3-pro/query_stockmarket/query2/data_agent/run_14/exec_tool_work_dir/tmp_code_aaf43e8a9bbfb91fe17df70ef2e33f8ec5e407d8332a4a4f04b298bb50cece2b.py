code = """import json

path = locals()['var_function-call-795890950430017818']
with open(path, 'r') as f:
    symbols = json.load(f)

batch_size = 500
batches = [symbols[i:i + batch_size] for i in range(0, len(symbols), batch_size)]

q = chr(39)
qq = chr(34)

queries = []
for batch in batches:
    parts = []
    for sym in batch:
        part = "SELECT " + q + sym + q + " as Symbol FROM " + qq + sym + qq + " WHERE " + qq + "Adj Close" + qq + " > 200 AND Date LIKE " + q + "2015%" + q + " LIMIT 1"
        parts.append(part)
    query = " UNION ALL ".join(parts)
    queries.append(query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-3949593977033921261': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12916805806640155023': 'file_storage/function-call-12916805806640155023.json', 'var_function-call-118847342532788354': 'file_storage/function-call-118847342532788354.json', 'var_function-call-795890950430017818': 'file_storage/function-call-795890950430017818.json', 'var_function-call-14536564358681273316': 1435, 'var_function-call-8889034498850713553': 'test', 'var_function-call-12910800544588247316': 1435, 'var_function-call-17086037818106034107': 'file_storage/function-call-17086037818106034107.json', 'var_function-call-12029157764372185238': 'file_storage/function-call-12029157764372185238.json', 'var_function-call-3474506765428153084': 'file_storage/function-call-3474506765428153084.json', 'var_function-call-15935806625743756606': 'file_storage/function-call-15935806625743756606.json'}

exec(code, env_args)
