code = """import json
import pandas as pd

file_path = locals()['var_function-call-1004509868039729014']
with open(file_path, 'r') as f:
    repo_names_data = json.load(f)

repo_names = [repo['repo_name'] for repo in repo_names_data]

# Construct the WHERE IN clause by joining parts
# Use single quotes for repo names
repo_name_filter_parts = []
for name in repo_names:
    repo_name_filter_parts.append("'" + name + "'")
repo_name_filter = ', '.join(repo_name_filter_parts)

# Construct the full SQL query using string concatenation
# Avoid triple double quotes in the Python code itself
query = "SELECT COUNT(DISTINCT commit) FROM commits WHERE repo_name IN (" + repo_name_filter + ") AND message IS NOT NULL AND LENGTH(message) < 1000 AND NOT (message LIKE 'merge%' OR message LIKE 'update%' OR message LIKE 'test%');"

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-1004509868039729014': 'file_storage/function-call-1004509868039729014.json', 'var_function-call-3430277530278713437': 'file_storage/function-call-3430277530278713437.json'}

exec(code, env_args)
