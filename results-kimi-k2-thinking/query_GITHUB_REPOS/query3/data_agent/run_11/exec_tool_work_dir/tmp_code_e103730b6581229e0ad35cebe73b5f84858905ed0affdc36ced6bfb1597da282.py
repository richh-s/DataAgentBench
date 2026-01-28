code = """import json

result_file = locals()['var_functions.query_db:10']
with open(result_file, 'r') as f:
    shell_repos = json.load(f)

# Create list of repo names
repo_list = [repo['repo_name'] for repo in shell_repos]

# Build SQL query for DuckDB
# We need to use the commits table in artifacts_database
conditions = []
conditions.append("repo_name IN (" + ", ".join([f"'{repo}'" for repo in repo_list[:50]]) + ")")  # Limit for testing
conditions.append("message IS NOT NULL")
conditions.append("LENGTH(message) < 1000")
conditions.append("LOWER(message) NOT LIKE 'merge%'")
conditions.append("LOWER(message) NOT LIKE 'update%'")
conditions.append("LOWER(message) NOT LIKE 'test%'")

query = "SELECT COUNT(*) as commit_count FROM commits WHERE " + " AND ".join(conditions)

print("__RESULT__:")
print(json.dumps(f"Query: {query}"))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'Total repos found: 114972', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': 'Total Shell repos: 6936'}

exec(code, env_args)
