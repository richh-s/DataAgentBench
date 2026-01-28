code = """import json

# Read the repository list from the stored result
repo_list_path = var_functions.query_db:0
with open(repo_list_path, 'r') as f:
    repo_data = json.load(f)

# Extract repo names
repo_names = [item['repo_name'] for item in repo_data]

# Create a SQL-safe list of repo names for the IN clause
# Since there are many repos, we'll create a comma-separated string
repo_names_str = ', '.join([f"'{name}'" for name in repo_names[:100]])  # Limit to first 100 to avoid query size limits

print('__RESULT__:')
print(repo_names_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
