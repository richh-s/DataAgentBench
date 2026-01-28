code = """import json
import os

# Read the repo list from the file
file_path = locals()['var_functions.query_db:10']

with open(file_path, 'r') as f:
    repo_data = json.load(f)

# Extract repo names
repo_names = [repo['repo_name'] for repo in repo_data]

# Get a batch of 1000 repos for testing
batch = repo_names[:1000]

# Build the query for DuckDB
query = f"""
SELECT COUNT(*) as commit_count 
FROM commits 
WHERE repo_name IN ({', '.join([f"'{repo}'" for repo in batch])})
  AND message IS NOT NULL 
  AND LENGTH(message) < 1000 
  AND LOWER(message) NOT LIKE 'merge%'
  AND LOWER(message) NOT LIKE 'update%'
  AND LOWER(message) NOT LIKE 'test%'
"""

print('__RESULT__:')
print(json.dumps({
    'batch_size': len(batch),
    'query_preview': query[:200] + '...' if len(query) > 200 else query
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'repo_count': 114972, 'sample_repos': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_repos': 114972, 'sample_repos': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}, 'var_functions.execute_python:16': {'total_repos': 114972, 'sample_repos': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook'], 'query_ready': True}, 'var_functions.execute_python:18': {'query': "SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN ('juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook', 'rarenerd/trai...", 'query_length': 3021909, 'repos_count': 114972}}

exec(code, env_args)
