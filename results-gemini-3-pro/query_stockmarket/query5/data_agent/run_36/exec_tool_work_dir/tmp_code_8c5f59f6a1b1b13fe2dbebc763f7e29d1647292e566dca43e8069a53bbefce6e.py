code = """import json

key = 'var_function-call-7323746392053808009'
with open(locals()[key], 'r') as f:
    data = json.load(f)
    valid_symbols = data['valid_symbols']

queries = []
for sym in valid_symbols:
    # Use .format()
    q = "SELECT '{0}' AS Symbol, COUNT(*) AS DayCount FROM \"{0}\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.20 * Low)".format(sym)
    queries.append(q)

chunk_size = 25
chunked_queries = []
for i in range(0, len(queries), chunk_size):
    chunk = queries[i:i+chunk_size]
    full_q = " UNION ALL ".join(chunk)
    chunked_queries.append(full_q)

print("DEBUG FIRST QUERY:")
print(queries[0])
print("__RESULT__:")
print(json.dumps(chunked_queries))"""

env_args = {'var_function-call-12648435365939612161': 'file_storage/function-call-12648435365939612161.json', 'var_function-call-16816668521200579530': 'file_storage/function-call-16816668521200579530.json', 'var_function-call-7323746392053808009': 'file_storage/function-call-7323746392053808009.json', 'var_function-call-1581519369653255099': 'file_storage/function-call-1581519369653255099.json', 'var_function-call-15284564913974246743': 'file_storage/function-call-15284564913974246743.json', 'var_function-call-8419711716962408880': 'file_storage/function-call-8419711716962408880.json'}

exec(code, env_args)
