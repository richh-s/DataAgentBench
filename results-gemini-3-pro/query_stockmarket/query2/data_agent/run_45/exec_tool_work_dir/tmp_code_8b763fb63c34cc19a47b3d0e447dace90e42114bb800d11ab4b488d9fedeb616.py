code = """import json
path = locals()['var_function-call-3295962867968348472']
with open(path) as f: s = json.load(f)
q_list = ["(SELECT '{}' as Symbol FROM \"{}\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1)".format(x, x) for x in s]
full = " UNION ALL ".join(q_list)
print("__RESULT__:")
print(json.dumps(full))"""

env_args = {'var_function-call-3501888639631551339': 'file_storage/function-call-3501888639631551339.json', 'var_function-call-1897156142471319365': 'file_storage/function-call-1897156142471319365.json', 'var_function-call-3295962867968348472': 'file_storage/function-call-3295962867968348472.json', 'var_function-call-11530623601656083675': 1435, 'var_function-call-3709276694871422927': [{'Date': '2018-08-15'}], 'var_function-call-4537489530168145434': []}

exec(code, env_args)
