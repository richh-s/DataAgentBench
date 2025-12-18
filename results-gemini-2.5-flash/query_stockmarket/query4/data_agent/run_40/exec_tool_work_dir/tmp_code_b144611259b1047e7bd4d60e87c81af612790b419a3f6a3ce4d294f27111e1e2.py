code = """import json

with open(locals()['var_function-call-17729935126212957061'], 'r') as f:
    nyse_non_etf_stocks = json.load(f)

symbols = list(nyse_non_etf_stocks.keys())

queries = []
for symbol in symbols:
    # Using str.format() to construct the query string to avoid f-string parsing issues
    # Double quotes for table name, single quotes for dates
    query = "SELECT Date, Open, Close FROM \"{}\" WHERE Date BETWEEN '2017-01-01' AND '2017-12-31';".format(symbol)
    queries.append(query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-16320646233867090762': 'file_storage/function-call-16320646233867090762.json', 'var_function-call-17729935126212957061': 'file_storage/function-call-17729935126212957061.json'}

exec(code, env_args)
