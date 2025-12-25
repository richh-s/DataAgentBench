code = """import json

etf_file_path = locals()['var_function-call-3295962867968348472']

with open(etf_file_path, 'r') as f:
    valid_etfs = json.load(f)

parts = []
for symbol in valid_etfs:
    # careful with quotes
    # Query part: (SELECT 'SYM' as Symbol FROM "SYM" WHERE "Date" BETWEEN '2015-01-01' AND '2015-12-31' AND "Adj Close" > 200 LIMIT 1)
    q = "(SELECT '" + symbol + "' as Symbol FROM \"" + symbol + "\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1)"
    parts.append(q)

full_query = " UNION ALL ".join(parts)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-3501888639631551339': 'file_storage/function-call-3501888639631551339.json', 'var_function-call-1897156142471319365': 'file_storage/function-call-1897156142471319365.json', 'var_function-call-3295962867968348472': 'file_storage/function-call-3295962867968348472.json', 'var_function-call-11530623601656083675': 1435, 'var_function-call-3709276694871422927': [{'Date': '2018-08-15'}], 'var_function-call-4537489530168145434': []}

exec(code, env_args)
