code = """import json

file_path = locals()['var_function-call-11004709737379666324']
with open(file_path, 'r') as f:
    data = json.load(f)

symbols = data['symbols']
chunk_size = 20
chunks = [symbols[i:i + chunk_size] for i in range(0, len(symbols), chunk_size)]

queries = []
dq = chr(34)
sq = chr(39)

for chunk in chunks:
    parts = []
    for s in chunk:
        q = "SELECT " + sq + s + sq + " as Symbol, COUNT(*) as Days FROM " + dq + s + dq + " WHERE Date LIKE " + sq + "2019%" + sq + " AND (High - Low) > 0.20 * Low"
        parts.append(q)
    full_query = " UNION ALL ".join(parts)
    # No ORDER BY or LIMIT yet, just raw counts
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-7798081154467211843': 'file_storage/function-call-7798081154467211843.json', 'var_function-call-7798081154467211922': 'file_storage/function-call-7798081154467211922.json', 'var_function-call-11004709737379666324': 'file_storage/function-call-11004709737379666324.json', 'var_function-call-14210081583729227631': 'Hello', 'var_function-call-9607862806926100376': 86, 'var_function-call-2380045601877292304': 'file_storage/function-call-2380045601877292304.json'}

exec(code, env_args)
