code = """import json
key = 'var_function-call-16716209027256917724'
path = locals()[key]
with open(path, 'r') as f: data = json.load(f)
parts = ["SELECT '" + i['Symbol'] + "' as S, COUNT(*) as C FROM \"" + i['Symbol'] + "\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' AND (\"High\" - \"Low\") > 0.20 * \"Low\"" for i in data]
q = " UNION ALL ".join(parts) + " ORDER BY C DESC LIMIT 5"
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_function-call-5873850458865278019': 'file_storage/function-call-5873850458865278019.json', 'var_function-call-10785221419564258441': 'file_storage/function-call-10785221419564258441.json', 'var_function-call-16716209027256917724': 'file_storage/function-call-16716209027256917724.json', 'var_function-call-139130541756909283': 86}

exec(code, env_args)
