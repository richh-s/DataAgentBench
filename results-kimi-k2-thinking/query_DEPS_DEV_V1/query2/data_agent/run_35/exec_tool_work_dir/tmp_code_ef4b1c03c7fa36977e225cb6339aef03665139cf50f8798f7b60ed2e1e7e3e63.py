code = """import json

# Access the variables from storage using locals()
packages_file = locals().get('var_functions.query_db:0')
projects_file = locals().get('var_functions.query_db:2')

with open(packages_file, 'r') as f:
    packages = json.load(f)

with open(projects_file, 'r') as f:
    projects = json.load(f)

# Count total records
print('__RESULT__:')
print(json.dumps({"packages_count": len(packages), "projects_count": len(projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
