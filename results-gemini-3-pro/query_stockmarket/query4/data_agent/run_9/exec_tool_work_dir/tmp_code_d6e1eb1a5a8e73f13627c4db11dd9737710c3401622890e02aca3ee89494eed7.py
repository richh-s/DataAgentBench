code = """import json

path = locals()['var_function-call-14063153681807922901']
with open(path, 'r') as f:
    batches = json.load(f)

# Join all batches
full_query = " UNION ALL ".join(batches)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-4623597435965185168': 'file_storage/function-call-4623597435965185168.json', 'var_function-call-4623597435965183535': 'file_storage/function-call-4623597435965183535.json', 'var_function-call-2477184406544893280': 'file_storage/function-call-2477184406544893280.json', 'var_function-call-956611621751547404': 'file_storage/function-call-956611621751547404.json', 'var_function-call-14063153681807922901': 'file_storage/function-call-14063153681807922901.json', 'var_function-call-6204034109739629368': {'count': 5}}

exec(code, env_args)
