code = """import json

# Load valid stocks
with open(locals()['var_function-call-6577585085519005006'], 'r') as f:
    valid_stocks = json.load(f)

# Construct SQL query
queries = []
for stock in valid_stocks:
    sym = stock['Symbol']
    # Use double quotes for table identifiers
    query = f"SELECT '{sym}' as Symbol, COUNT(*) as Count FROM \"{sym}\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"
    queries.append(query)

full_query = " UNION ALL ".join(queries) + " ORDER BY Count DESC LIMIT 5"

print("__RESULT__:")
print(full_query)"""

env_args = {'var_function-call-12823899382906122625': 'file_storage/function-call-12823899382906122625.json', 'var_function-call-15795794129974371923': 'file_storage/function-call-15795794129974371923.json', 'var_function-call-6577585085519005006': 'file_storage/function-call-6577585085519005006.json'}

exec(code, env_args)
