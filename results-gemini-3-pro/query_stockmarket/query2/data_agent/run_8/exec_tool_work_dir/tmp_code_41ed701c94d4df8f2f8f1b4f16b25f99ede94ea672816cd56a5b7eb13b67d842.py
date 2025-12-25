code = """import json

key = 'var_function-call-6325032711824725866'
path = locals()[key]
with open(path, 'r') as f:
    symbols = json.load(f)

# Take first 10
symbols = symbols[:10]

parts = []
for s in symbols:
    part = "SELECT '{0}' as Symbol FROM \"{0}\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1".format(s)
    parts.append(part)

full_query = " UNION ALL ".join(parts)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-14532322368764427460': 'file_storage/function-call-14532322368764427460.json', 'var_function-call-8803107773511705717': 'file_storage/function-call-8803107773511705717.json', 'var_function-call-6325032711824725866': 'file_storage/function-call-6325032711824725866.json', 'var_function-call-16713880611030902886': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}

exec(code, env_args)
