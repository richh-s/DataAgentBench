code = """import json
import pandas as pd

with open(locals()['var_function-call-605780459573890234'], 'r') as f:
    non_python_repos_data = json.load(f)

non_python_repo_names = [repo['repo_name'] for repo in non_python_repos_data]

batch_size = 500  # Define a reasonable batch size
batch_queries = []

for i in range(0, len(non_python_repo_names), batch_size):
    batch_repos = non_python_repo_names[i:i + batch_size]
    # Escape single quotes in repo names for SQL
    formatted_batch_repos = ', '.join([f"'{name.replace("'", "''')}'" for name in batch_repos])
    query = f"SELECT repo_name, COUNT(commit) AS commit_count FROM commits WHERE repo_name IN ({formatted_batch_repos}) GROUP BY repo_name;"
    batch_queries.append({"db_name": "artifacts_database", "query": query})

print('__RESULT__:')
print(json.dumps(batch_queries))"""

env_args = {'var_function-call-605780459573890234': 'file_storage/function-call-605780459573890234.json', 'var_function-call-8996245140497775337': 'file_storage/function-call-8996245140497775337.json'}

exec(code, env_args)
