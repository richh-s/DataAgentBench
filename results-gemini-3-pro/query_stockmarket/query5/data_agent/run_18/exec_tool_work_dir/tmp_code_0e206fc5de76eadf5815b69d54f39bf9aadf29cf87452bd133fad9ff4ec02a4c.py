code = """import json

key = 'var_function-call-6577585085519005006'
fname = locals()[key]

with open(fname, 'r') as f:
    valid_stocks = json.load(f)

queries = []
for stock in valid_stocks[:1]:
    sym = stock['Symbol']
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as Count FROM \"" + sym + "\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

print("__RESULT__:")
print(json.dumps(queries[0]))"""

env_args = {'var_function-call-12823899382906122625': 'file_storage/function-call-12823899382906122625.json', 'var_function-call-15795794129974371923': 'file_storage/function-call-15795794129974371923.json', 'var_function-call-6577585085519005006': 'file_storage/function-call-6577585085519005006.json', 'var_function-call-10505731309346460483': 'file_storage/function-call-10505731309346460483.json', 'var_function-call-7006835438988277563': 'file_storage/function-call-7006835438988277563.json'}

exec(code, env_args)
