code = """import json

# Read the query result
result_path = var_functions.query_db:0
print(result_path)

# Let's just try to read the file
with open(result_path, 'r') as f:
    content = json.load(f)

print(len(content))
print(content[0].keys())"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
