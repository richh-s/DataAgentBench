code = """import json

with open(locals()['var_function-call-17729935126212957061'], 'r') as f:
    nyse_non_etf_stocks = json.load(f)

symbols = list(nyse_non_etf_stocks.keys())

all_queries = []
for symbol in symbols:
    # Use an f-string directly with proper escaping for the table name
    all_queries.append(f"SELECT '{symbol}' AS Symbol, Date, Open, Close FROM \"{symbol}\" WHERE Date BETWEEN '2017-01-01' AND '2017-12-31'")

union_query = " UNION ALL ".join(all_queries)

print("__RESULT__:")
print(json.dumps(union_query))"""

env_args = {'var_function-call-16320646233867090762': 'file_storage/function-call-16320646233867090762.json', 'var_function-call-17729935126212957061': 'file_storage/function-call-17729935126212957061.json'}

exec(code, env_args)
