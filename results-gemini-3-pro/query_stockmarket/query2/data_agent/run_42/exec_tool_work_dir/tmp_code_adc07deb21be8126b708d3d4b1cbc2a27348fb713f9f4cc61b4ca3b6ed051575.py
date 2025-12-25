code = """import json

file_path = locals()['var_function-call-5384306223597069049']
with open(file_path, 'r') as f:
    syms = json.load(f)

batch = syms[0:120]
queries = []
q_quote = chr(39) # '
d_quote = chr(34) # "

for s in batch:
    # SELECT 'SYM' as Symbol FROM "SYM" WHERE "Adj Close" > 200 AND Date LIKE '2015%' LIMIT 1
    q = "SELECT " + q_quote + s + q_quote + " as Symbol FROM " + d_quote + s + d_quote + " WHERE " + d_quote + "Adj Close" + d_quote + " > 200 AND Date LIKE " + q_quote + "2015%" + q_quote + " LIMIT 1"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-15044746787595229407': 'file_storage/function-call-15044746787595229407.json', 'var_function-call-2315172505104339094': 'file_storage/function-call-2315172505104339094.json', 'var_function-call-5384306223597069049': 'file_storage/function-call-5384306223597069049.json', 'var_function-call-331467625531987005': 1435, 'var_function-call-15656793673732984981': 'test', 'var_function-call-11220487807880313085': ['var_function-call-15044746787595229407', 'var_function-call-2315172505104339094', 'var_function-call-5384306223597069049', 'var_function-call-331467625531987005', 'var_function-call-15656793673732984981', '__builtins__', 'json']}

exec(code, env_args)
