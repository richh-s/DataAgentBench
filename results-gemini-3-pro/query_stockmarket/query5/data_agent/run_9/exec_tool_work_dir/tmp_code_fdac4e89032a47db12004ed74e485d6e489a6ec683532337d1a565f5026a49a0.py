code = """import json

key = 'var_function-call-9687647277801400069'
path = locals()[key]
with open(path, 'r') as f:
    data = json.load(f)
symbols = data['target_symbols']

parts = []
for s in symbols:
    p = 'SELECT \'' + s + '\' as Symbol, COUNT(*) as Days FROM "' + s + '" WHERE "Date" LIKE \'2019%\' AND ("High" - "Low") > 0.2 * "Low"'
    parts.append(p)

full_query = ' UNION ALL '.join(parts) + ' ORDER BY Days DESC LIMIT 5'

print('__RESULT__:')
print(json.dumps(full_query))"""

env_args = {'var_function-call-5715290877284323167': 'file_storage/function-call-5715290877284323167.json', 'var_function-call-18378532918632794193': 'file_storage/function-call-18378532918632794193.json', 'var_function-call-9687647277801400069': 'file_storage/function-call-9687647277801400069.json', 'var_function-call-7849848251971865444': 'test', 'var_function-call-15107257653857092335': "SELECT 'AGMH' as S, COUNT(*) FROM  + s +  UNION SELECT 'ALACU' as S, COUNT(*) FROM  + s + "}

exec(code, env_args)
