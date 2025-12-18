code = """import json

with open(locals()['var_function-call-605780459573890234'], 'r') as f:
    non_python_repos_data = json.load(f)

non_python_repo_names = [repo['repo_name'] for repo in non_python_repos_data]

# Escape single quotes in repo names for SQL IN clause
escaped_repo_names = [name.replace("'", "''") for name in non_python_repo_names]

# Join them into a single string for the IN clause
repo_names_in_clause = ', '.join([f"'{name}'" for name in escaped_repo_names])

# Construct the final SQL query
sql_query = f"SELECT repo_name, COUNT(commit) AS commit_count FROM commits WHERE repo_name IN ({repo_names_in_clause}) GROUP BY repo_name ORDER BY commit_count DESC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({"db_name": "artifacts_database", "query": sql_query}))"""

env_args = {'var_function-call-605780459573890234': 'file_storage/function-call-605780459573890234.json', 'var_function-call-8996245140497775337': 'file_storage/function-call-8996245140497775337.json'}

exec(code, env_args)
