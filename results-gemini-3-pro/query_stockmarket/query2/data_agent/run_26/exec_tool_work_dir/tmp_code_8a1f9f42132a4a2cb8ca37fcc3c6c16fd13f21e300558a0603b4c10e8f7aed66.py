code = """import json
path = locals()['var_function-call-10673993515668568278']
with open(path, 'r') as f:
    target_symbols = json.load(f)

queries = []
batch_size = 500
for i in range(0, len(target_symbols), batch_size):
    batch = target_symbols[i:i+batch_size]
    subqueries = []
    for sym in batch:
        sq = "SELECT '{0}' AS Symbol, MAX(\"Adj Close\") AS MaxPrice FROM \"{0}\" WHERE Date LIKE '2015%'".format(sym)
        subqueries.append(sq)
    
    full_q = "SELECT Symbol FROM (" + " UNION ALL ".join(subqueries) + ") WHERE MaxPrice > 200"
    queries.append(full_q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-10776686363882636286': 'file_storage/function-call-10776686363882636286.json', 'var_function-call-17564146579276978654': 'file_storage/function-call-17564146579276978654.json', 'var_function-call-10673993515668568278': 'file_storage/function-call-10673993515668568278.json', 'var_function-call-14270725523313256816': 1435}

exec(code, env_args)
