code = """import json

etf_file_path = locals()['var_function-call-3295962867968348472']

with open(etf_file_path, 'r') as f:
    valid_etfs = json.load(f)

batch = valid_etfs[:100]

parts = []
for symbol in batch:
    # Use format to avoid f-string quote issues
    part = "SELECT '{}' as Symbol FROM \"{}\" WHERE \"Date\" LIKE '2015%' AND \"Adj Close\" > 200 LIMIT 1".format(symbol, symbol)
    parts.append(part)

query = " UNION ALL ".join(parts)

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-3501888639631551339': 'file_storage/function-call-3501888639631551339.json', 'var_function-call-1897156142471319365': 'file_storage/function-call-1897156142471319365.json', 'var_function-call-3295962867968348472': 'file_storage/function-call-3295962867968348472.json', 'var_function-call-11530623601656083675': 1435, 'var_function-call-3709276694871422927': [{'Date': '2018-08-15'}]}

exec(code, env_args)
