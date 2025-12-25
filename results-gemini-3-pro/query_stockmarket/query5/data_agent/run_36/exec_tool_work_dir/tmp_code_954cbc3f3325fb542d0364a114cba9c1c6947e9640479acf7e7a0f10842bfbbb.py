code = """import json

key = 'var_function-call-7323746392053808009'
with open(locals()[key], 'r') as f:
    data = json.load(f)
    valid_symbols = data['valid_symbols']

chunk_size = 25
queries = []
for i in range(0, len(valid_symbols), chunk_size):
    chunk = valid_symbols[i:i+chunk_size]
    sub_queries = []
    for sym in chunk:
        q = "SELECT '" + sym + "' AS Symbol, COUNT(*) AS DayCount FROM \"" + sym + "\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.20 * Low)"
        sub_queries.append(q)
    full_q = " UNION ALL ".join(sub_queries)
    queries.append(full_q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-12648435365939612161': 'file_storage/function-call-12648435365939612161.json', 'var_function-call-16816668521200579530': 'file_storage/function-call-16816668521200579530.json', 'var_function-call-7323746392053808009': 'file_storage/function-call-7323746392053808009.json', 'var_function-call-1581519369653255099': 'file_storage/function-call-1581519369653255099.json', 'var_function-call-15284564913974246743': 'file_storage/function-call-15284564913974246743.json'}

exec(code, env_args)
