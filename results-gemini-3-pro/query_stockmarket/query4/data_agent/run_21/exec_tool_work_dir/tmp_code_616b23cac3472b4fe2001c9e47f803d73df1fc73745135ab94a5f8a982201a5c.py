code = """import json

# Load symbols
path = locals()['var_function-call-14501516431972951322']
with open(path, 'r') as f:
    stocks = json.load(f)

symbols = [s['Symbol'] for s in stocks]

# Generate query
queries = []
for sym in symbols:
    # Ensure sym is safe? Assuming alphanumeric.
    q = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-14501516431972951322': 'file_storage/function-call-14501516431972951322.json', 'var_function-call-15409720678341312675': 234}

exec(code, env_args)
