code = """import json

# Load valid ETFs
path = locals()['var_function-call-6325032711824725866']
with open(path, 'r') as f:
    valid_etfs = json.load(f)

queries = []
for symbol in valid_etfs:
    # Construct the query part
    # Use "Adj Close" in double quotes
    # Date is a string in format YYYY-MM-DD usually.
    q = "SELECT '{0}' as Symbol FROM \"{0}\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1".format(symbol)
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-14532322368764427460': 'file_storage/function-call-14532322368764427460.json', 'var_function-call-8803107773511705717': 'file_storage/function-call-8803107773511705717.json', 'var_function-call-6325032711824725866': 'file_storage/function-call-6325032711824725866.json'}

exec(code, env_args)
