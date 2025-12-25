code = """import json

# Access file paths from storage
path_cand = locals()['var_function-call-2542358163233930626']
path_tables = locals()['var_function-call-17634865684080335630']

# Load data
with open(path_cand, 'r') as f:
    cand_list = json.load(f)
    candidates = set(c['Symbol'] for c in cand_list)

with open(path_tables, 'r') as f:
    tables = set(json.load(f))

# Intersect
symbols = sorted(list(candidates.intersection(tables)))

# Construct query
parts = []
for s in symbols:
    q = 'SELECT \'' + s + '\' AS Symbol FROM "' + s + '" WHERE "Adj Close" > 200 AND "Date" LIKE \'2015%\' LIMIT 1'
    parts.append(q)

final_query = ' UNION ALL '.join(parts)

print('__RESULT__:')
print(json.dumps(final_query))"""

env_args = {'var_function-call-2542358163233930626': 'file_storage/function-call-2542358163233930626.json', 'var_function-call-17634865684080335630': 'file_storage/function-call-17634865684080335630.json', 'var_function-call-753327868909953960': 'test'}

exec(code, env_args)
