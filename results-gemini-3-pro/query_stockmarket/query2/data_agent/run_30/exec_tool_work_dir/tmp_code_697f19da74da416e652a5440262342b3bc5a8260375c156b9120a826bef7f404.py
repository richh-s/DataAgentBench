code = """import json

with open('var_function-call-2542358163233930626.json', 'r') as f:
    cand_list = json.load(f)
    candidates = set(c['Symbol'] for c in cand_list)

with open('var_function-call-17634865684080335630.json', 'r') as f:
    tables = set(json.load(f))

symbols = sorted(list(candidates.intersection(tables)))

parts = []
for s in symbols:
    q = 'SELECT \'{0}\' AS Symbol FROM "{0}" WHERE "Adj Close" > 200 AND "Date" LIKE \'2015%\' LIMIT 1'.format(s)
    parts.append(q)

final_query = ' UNION ALL '.join(parts)

print('__RESULT__:')
print(json.dumps(final_query))"""

env_args = {'var_function-call-2542358163233930626': 'file_storage/function-call-2542358163233930626.json', 'var_function-call-17634865684080335630': 'file_storage/function-call-17634865684080335630.json', 'var_function-call-753327868909953960': 'test'}

exec(code, env_args)
