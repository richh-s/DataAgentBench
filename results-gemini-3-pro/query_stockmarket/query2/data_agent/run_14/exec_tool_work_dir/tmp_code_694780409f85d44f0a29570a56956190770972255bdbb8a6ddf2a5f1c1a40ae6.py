code = """import json

path = locals()['var_function-call-795890950430017818']
with open(path, 'r') as f:
    symbols = json.load(f)

batch_size = 200
batches = [symbols[i:i + batch_size] for i in range(0, len(symbols), batch_size)]

queries = []
for batch in batches:
    parts = []
    for sym in batch:
        safe_sym = sym.replace('"', '""')
        # using format to avoid f-string quote issues
        part = "SELECT '{0}' as Symbol FROM \"{0}\" WHERE \"Adj Close\" > 200 AND Date LIKE '2015%' LIMIT 1".format(safe_sym)
        parts.append(part)
    query = " UNION ALL ".join(parts)
    queries.append(query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-3949593977033921261': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12916805806640155023': 'file_storage/function-call-12916805806640155023.json', 'var_function-call-118847342532788354': 'file_storage/function-call-118847342532788354.json', 'var_function-call-795890950430017818': 'file_storage/function-call-795890950430017818.json', 'var_function-call-14536564358681273316': 1435}

exec(code, env_args)
