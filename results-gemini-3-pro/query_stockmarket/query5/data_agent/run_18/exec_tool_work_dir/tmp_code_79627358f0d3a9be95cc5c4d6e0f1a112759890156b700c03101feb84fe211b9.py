code = """import json

key = 'var_function-call-6577585085519005006'
fname = locals()[key]

with open(fname, 'r') as f:
    valid_stocks = json.load(f)

queries = []
for stock in valid_stocks:
    sym = stock['Symbol']
    # Use simple string concatenation
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as Count FROM \"" + sym + "\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

full_query = " UNION ALL ".join(queries) + " ORDER BY Count DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-12823899382906122625': 'file_storage/function-call-12823899382906122625.json', 'var_function-call-15795794129974371923': 'file_storage/function-call-15795794129974371923.json', 'var_function-call-6577585085519005006': 'file_storage/function-call-6577585085519005006.json', 'var_function-call-10505731309346460483': 'file_storage/function-call-10505731309346460483.json'}

exec(code, env_args)
