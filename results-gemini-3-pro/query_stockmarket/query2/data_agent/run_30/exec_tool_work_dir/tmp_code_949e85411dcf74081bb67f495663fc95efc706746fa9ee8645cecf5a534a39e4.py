code = """import json
cand_list = json.load(open('var_function-call-2542358163233930626.json', 'r'))
candidates = set(c['Symbol'] for c in cand_list)
tables = set(json.load(open('var_function-call-17634865684080335630.json', 'r')))
symbols = sorted(list(candidates.intersection(tables)))
parts = ['SELECT \'' + s + '\' AS Symbol FROM "' + s + '" WHERE "Adj Close" > 200 AND "Date" LIKE \'2015%\' LIMIT 1' for s in symbols]
final_query = ' UNION ALL '.join(parts)
print('__RESULT__:')
print(json.dumps(final_query))"""

env_args = {'var_function-call-2542358163233930626': 'file_storage/function-call-2542358163233930626.json', 'var_function-call-17634865684080335630': 'file_storage/function-call-17634865684080335630.json', 'var_function-call-753327868909953960': 'test'}

exec(code, env_args)
