code = """import json

candidates_key = 'var_function-call-13463588165360546647'
candidates_path = locals()[candidates_key]
with open(candidates_path, 'r') as f:
    candidates = json.load(f)

batch_size = 200
queries = []

for i in range(0, len(candidates), batch_size):
    batch = candidates[i:i+batch_size]
    parts = []
    for sym in batch:
        s = "SELECT '" + sym + "' as Symbol FROM \"" + sym + "\" WHERE \"Adj Close\" > 200 AND Date LIKE '2015%' LIMIT 1"
        parts.append(s)
    queries.append(" UNION ALL ".join(parts))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-1439893960657579719': 'file_storage/function-call-1439893960657579719.json', 'var_function-call-8649986010323061245': 'file_storage/function-call-8649986010323061245.json', 'var_function-call-13463588165360546647': 'file_storage/function-call-13463588165360546647.json', 'var_function-call-17317458862947975022': 1435}

exec(code, env_args)
