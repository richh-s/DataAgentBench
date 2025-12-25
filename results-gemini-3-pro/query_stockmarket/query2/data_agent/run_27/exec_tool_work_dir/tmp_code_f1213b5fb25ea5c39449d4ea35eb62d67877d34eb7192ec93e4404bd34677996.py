code = """import json

file_path = locals()['var_function-call-3637682741273971379']
with open(file_path, 'r') as f:
    batches = json.load(f)

valid_tickers = [ticker for batch in batches for ticker in batch]

queries = []
for ticker in valid_tickers:
    # Use single quotes for the python string, and include double quotes for SQL identifiers
    # SQL: SELECT 'TICKER' as Symbol FROM "TICKER" WHERE "Date" ...
    q = "SELECT '" + ticker + "' as Symbol FROM \"" + ticker + "\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("Query length:", len(full_query))
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-6291273035979822157': 'file_storage/function-call-6291273035979822157.json', 'var_function-call-17273355007471526409': 'file_storage/function-call-17273355007471526409.json', 'var_function-call-6700212571527904625': 1435, 'var_function-call-3183618801010455834': 'file_storage/function-call-3183618801010455834.json', 'var_function-call-3637682741273971379': 'file_storage/function-call-3637682741273971379.json'}

exec(code, env_args)
