code = """# Access variables directly by reading from storage
import json

# Read packages data
packages_file_path = var_functions.query_db:0
with open(packages_file_path, 'r') as f:
    packages_data = json.load(f)

print('__RESULT__:')
print(json.dumps({"packages_count": len(packages_data)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:7': {'packages_count': 100, 'projects_count': 100}}

exec(code, env_args)
