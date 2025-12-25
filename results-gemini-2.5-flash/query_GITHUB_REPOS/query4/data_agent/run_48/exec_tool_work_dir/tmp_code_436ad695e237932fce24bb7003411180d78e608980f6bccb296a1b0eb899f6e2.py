code = """import json
import pandas as pd

with open(locals()['var_function-call-605780459573890234'], 'r') as f:
    non_python_repos_data = json.load(f)

non_python_repo_names = [repo['repo_name'] for repo in non_python_repos_data]

# Construct the IN clause for the SQL query
# Handle potential single quote in repo names by escaping them
formatted_repo_names = ', '.join([f"'{name.replace("'", "''')}'" for name in non_python_repo_names])

# Print the constructed query for the next step
print('__RESULT__:')
print(json.dumps({"query": f"SELECT repo_name, COUNT(commit) AS commit_count FROM commits WHERE repo_name IN ({formatted_repo_names}) GROUP BY repo_name ORDER BY commit_count DESC LIMIT 5;"}))"""

env_args = {'var_function-call-605780459573890234': 'file_storage/function-call-605780459573890234.json', 'var_function-call-8996245140497775337': 'file_storage/function-call-8996245140497775337.json'}

exec(code, env_args)
