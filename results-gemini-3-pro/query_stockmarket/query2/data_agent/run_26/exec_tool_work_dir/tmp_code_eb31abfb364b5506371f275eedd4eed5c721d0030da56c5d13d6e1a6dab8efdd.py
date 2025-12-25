code = """import json

keys = list(locals().keys())
target_key = [k for k in keys if '10673993515668568278' in k][0]
with open(locals()[target_key], 'r') as f:
    target_symbols = json.load(f)

queries = []
batch_size = 500
q_quote = chr(34)

for i in range(0, len(target_symbols), batch_size):
    batch = target_symbols[i:i+batch_size]
    subqueries = []
    for sym in batch:
        sq = "SELECT '{0}' AS Symbol, MAX({1}Adj Close{1}) AS MaxPrice FROM {1}{0}{1} WHERE Date LIKE '2015%'".format(sym, q_quote)
        subqueries.append(sq)
    
    full_q = "SELECT Symbol FROM (" + " UNION ALL ".join(subqueries) + ") WHERE MaxPrice > 200"
    queries.append(full_q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-10776686363882636286': 'file_storage/function-call-10776686363882636286.json', 'var_function-call-17564146579276978654': 'file_storage/function-call-17564146579276978654.json', 'var_function-call-10673993515668568278': 'file_storage/function-call-10673993515668568278.json', 'var_function-call-14270725523313256816': 1435}

exec(code, env_args)
