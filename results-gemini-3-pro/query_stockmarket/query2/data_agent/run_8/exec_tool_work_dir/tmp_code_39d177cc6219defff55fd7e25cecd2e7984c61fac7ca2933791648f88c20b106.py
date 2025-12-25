code = """import json

path = locals().get('var_function-call-6325032711824725866')
with open(path, 'r') as f:
    symbols = json.load(f)

# Batch 1: 0-80
batch = symbols[0:80]
dq = chr(34)
parts = []
for s in batch:
    # "Adj Close" needs double quotes
    q = "SELECT '{0}' as Symbol FROM {1}{0}{1} WHERE {1}Adj Close{1} > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1".format(s, dq)
    parts.append(q)

full_query = " UNION ALL ".join(parts)
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-14532322368764427460': 'file_storage/function-call-14532322368764427460.json', 'var_function-call-8803107773511705717': 'file_storage/function-call-8803107773511705717.json', 'var_function-call-6325032711824725866': 'file_storage/function-call-6325032711824725866.json', 'var_function-call-16713880611030902886': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_function-call-16160768990026222278': 'file_storage/function-call-16160768990026222278.json', 'var_function-call-1491270065845566597': 1435}

exec(code, env_args)
