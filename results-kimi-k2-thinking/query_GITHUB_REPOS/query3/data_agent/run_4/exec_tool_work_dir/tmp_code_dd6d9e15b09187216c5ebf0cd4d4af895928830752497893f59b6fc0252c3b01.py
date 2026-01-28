code = """import json
import os

# Read the repo list from the file
file_path = locals()['var_functions.query_db:10']

with open(file_path, 'r') as f:
    repo_data = json.load(f)

# Extract repo names
repo_names = [repo['repo_name'] for repo in repo_data]

# Build the query for DuckDB
# We need to query the commits table with these repos
# Since the list is large, we'll construct the query
query = "SELECT COUNT(*) as commit_count FROM commits WHERE "
query += "repo_name IN ("
query += ", ".join([f"'{repo}'" for repo in repo_names])
query += ") AND "
query += "message IS NOT NULL AND "
query += "LENGTH(message) < 1000 AND "
query += "LOWER(message) NOT LIKE 'merge%' AND "
query += "LOWER(message) NOT LIKE 'update%' AND "
query += "LOWER(message) NOT LIKE 'test%'"

print('__RESULT__:')
print(json.dumps({
    'query': query[:200] + '...' if len(query) > 200 else query,
    'query_length': len(query),
    'repos_count': len(repo_names)
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'repo_count': 114972, 'sample_repos': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_repos': 114972, 'sample_repos': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}, 'var_functions.execute_python:16': {'total_repos': 114972, 'sample_repos': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook'], 'query_ready': True}}

exec(code, env_args)
