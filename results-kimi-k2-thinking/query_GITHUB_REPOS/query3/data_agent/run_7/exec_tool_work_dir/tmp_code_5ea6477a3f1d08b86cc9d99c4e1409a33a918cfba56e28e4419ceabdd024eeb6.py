code = """import json
import csv
import os

# Load the repository list
repo_list_file = locals()['var_functions.query_db:0']
with open(repo_list_file, 'r') as f:
    repositories = json.load(f)

repo_names = [repo['repo_name'] for repo in repositories]
total_repos = len(repo_names)
batch_size = 500
num_batches = (total_repos + batch_size - 1) // batch_size

# Create a batch query file for DuckDB
batch_queries = []
for i in range(0, total_repos, batch_size):
    batch = repo_names[i:i+batch_size]
    repo_list = ', '.join(f"'{repo}'" for repo in batch)
    query = f"""
        SELECT count(*) as commit_count
        FROM commits 
        WHERE repo_name IN ({repo_list})
        AND message IS NOT NULL 
        AND message <> '' 
        AND length(message) < 1000 
        AND lower(message) NOT LIKE 'merge%'
        AND lower(message) NOT LIKE 'update%'
        AND lower(message) NOT LIKE 'test%'
    """
    batch_queries.append(query.strip())

print('__RESULT__:')
print(json.dumps({
    "total_repos": total_repos,
    "batch_size": batch_size,
    "num_batches": num_batches,
    "first_query_preview": batch_queries[0][:200] + "..."
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 114972, 'var_functions.execute_python:6': {'total_repos': 114972, 'num_batches': 115, 'first_batch_size': 1000}, 'var_functions.list_db:8': ['commits', 'contents', 'files'], 'var_functions.execute_python:10': {'total_repos': 114972, 'batch_size': 50, 'num_batches': 2300}}

exec(code, env_args)
