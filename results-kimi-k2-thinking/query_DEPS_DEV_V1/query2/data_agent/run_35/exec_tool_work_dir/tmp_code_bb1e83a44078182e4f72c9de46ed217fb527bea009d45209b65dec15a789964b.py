code = """import json

# Read the full results from the files
pkg_file = var_functions.query_db:0
proj_file = var_functions.query_db:2

with open(pkg_file, 'r') as f:
    packages = json.load(f)

with open(proj_file, 'r') as f:
    projects = json.load(f)

print('__RESULT__:')
print(f"Packages count: {len(packages)}, Projects count: {len(projects)}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
