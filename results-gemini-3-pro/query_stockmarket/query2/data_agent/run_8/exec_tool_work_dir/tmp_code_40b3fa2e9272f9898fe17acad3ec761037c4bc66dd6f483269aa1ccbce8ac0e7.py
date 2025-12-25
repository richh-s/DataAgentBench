code = """import json

path = locals().get('var_function-call-6325032711824725866')
with open(path, 'r') as f:
    symbols = json.load(f)

# Use chr(34) for double quote to avoid backslash issues
dq = chr(34)

queries = []
for s in symbols:
    # "Adj Close" needs double quotes
    # Date values need single quotes
    # Query: SELECT 'SYM' as Symbol FROM "SYM" WHERE "Adj Close" > 200 AND Date >= '2015-01-01' ...
    q = "SELECT '{0}' as Symbol FROM {1}{0}{1} WHERE {1}Adj Close{1} > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1".format(s, dq)
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-14532322368764427460': 'file_storage/function-call-14532322368764427460.json', 'var_function-call-8803107773511705717': 'file_storage/function-call-8803107773511705717.json', 'var_function-call-6325032711824725866': 'file_storage/function-call-6325032711824725866.json', 'var_function-call-16713880611030902886': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}

exec(code, env_args)
