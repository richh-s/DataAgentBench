code = """import json

file_path = locals()['var_function-call-5384306223597069049']
with open(file_path, 'r') as f:
    valid_symbols = json.load(f)

batch = valid_symbols[0:150]
queries = []
for sym in batch:
    q = "SELECT '" + sym + "' as Symbol FROM \"" + sym + "\" WHERE \"Adj Close\" > 200 AND Date LIKE '2015%' LIMIT 1"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-15044746787595229407': 'file_storage/function-call-15044746787595229407.json', 'var_function-call-2315172505104339094': 'file_storage/function-call-2315172505104339094.json', 'var_function-call-5384306223597069049': 'file_storage/function-call-5384306223597069049.json', 'var_function-call-331467625531987005': 1435}

exec(code, env_args)
