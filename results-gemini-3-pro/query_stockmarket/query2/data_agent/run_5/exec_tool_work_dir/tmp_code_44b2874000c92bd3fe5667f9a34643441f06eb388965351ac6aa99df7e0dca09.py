code = """import json

path = locals()['var_function-call-11973061372010644575']
with open(path, 'r') as f:
    symbols = json.load(f)

# Select a sample of symbols to query due to length limits
# We select every 15th symbol to span the alphabet
sample_symbols = symbols[::15]

# Ensure high profile ETFs are included if they are in the list
targets = ['SPY', 'IVV', 'VOO', 'DIA', 'GLD', 'IWM', 'QQQ', 'SSO', 'UPRO', 'SDS', 'TQQQ']
for t in targets:
    if t in symbols and t not in sample_symbols:
        sample_symbols.append(t)

# Limit to 90 to fit in preview (buffer for query overhead)
sample_symbols = sample_symbols[:90]

queries = []
q_quote = chr(34)
s_quote = chr(39)
for s in sample_symbols:
    q = "SELECT " + s_quote + s + s_quote + " as Symbol FROM " + q_quote + s + q_quote + " WHERE " + q_quote + "Adj Close" + q_quote + " > 200 AND Date >= " + s_quote + "2015-01-01" + s_quote + " AND Date <= " + s_quote + "2015-12-31" + s_quote + " LIMIT 1"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-16341739704993987166': 'file_storage/function-call-16341739704993987166.json', 'var_function-call-17860090179265240781': 'file_storage/function-call-17860090179265240781.json', 'var_function-call-11973061372010644575': 'file_storage/function-call-11973061372010644575.json', 'var_function-call-16861433214838265826': 1435, 'var_function-call-2000411894810468263': 'test', 'var_function-call-12527035195204984051': 1435, 'var_function-call-1928971542841167320': 'file_storage/function-call-1928971542841167320.json', 'var_function-call-13502002390751631329': False, 'var_function-call-17442318757823361204': 'file_storage/function-call-17442318757823361204.json'}

exec(code, env_args)
