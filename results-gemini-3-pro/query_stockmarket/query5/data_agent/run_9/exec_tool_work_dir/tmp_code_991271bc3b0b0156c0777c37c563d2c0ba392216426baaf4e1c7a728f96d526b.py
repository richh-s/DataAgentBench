code = """import json
import os

# Find the variable holding the path
target_key = 'var_function-call-9687647277801400069'
path = locals()[target_key]

with open(path, 'r') as f:
    data = json.load(f)

symbols = data['target_symbols']

# Construct query
parts = []
for sym in symbols:
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as Days FROM \"" + sym + "\" WHERE \"Date\" LIKE '2019%' AND (\"High\" - \"Low\") > 0.2 * \"Low\""
    parts.append(q)

full_query = " UNION ALL ".join(parts) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-5715290877284323167': 'file_storage/function-call-5715290877284323167.json', 'var_function-call-18378532918632794193': 'file_storage/function-call-18378532918632794193.json', 'var_function-call-9687647277801400069': 'file_storage/function-call-9687647277801400069.json'}

exec(code, env_args)
