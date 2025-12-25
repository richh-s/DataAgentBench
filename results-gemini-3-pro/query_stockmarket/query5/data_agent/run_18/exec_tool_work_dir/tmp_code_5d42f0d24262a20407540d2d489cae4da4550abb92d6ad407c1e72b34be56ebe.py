code = """import json

key = 'var_function-call-6577585085519005006'
fname = locals()[key]

with open(fname, 'r') as f:
    valid_stocks = json.load(f)

# Batch 1: 0 to 50
batch = valid_stocks[:50]

queries = []
dq = chr(34)
for stock in batch:
    sym = stock['Symbol']
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as Count FROM " + dq + sym + dq + " WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-12823899382906122625': 'file_storage/function-call-12823899382906122625.json', 'var_function-call-15795794129974371923': 'file_storage/function-call-15795794129974371923.json', 'var_function-call-6577585085519005006': 'file_storage/function-call-6577585085519005006.json', 'var_function-call-10505731309346460483': 'file_storage/function-call-10505731309346460483.json', 'var_function-call-7006835438988277563': 'file_storage/function-call-7006835438988277563.json', 'var_function-call-12347760722963562781': "SELECT 'AGMH' as Symbol, COUNT(*) as Count FROM  + sym +  WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)", 'var_function-call-5980987491185989219': 'file_storage/function-call-5980987491185989219.json', 'var_function-call-17003443271316880937': 'file_storage/function-call-17003443271316880937.json'}

exec(code, env_args)
