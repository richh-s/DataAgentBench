code = """import json
import os

# Read the repository list from file
file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    repo_data = json.load(f)

repo_names = [repo['repo_name'] for repo in repo_data]

# Process in batches to avoid overwhelming the database
batch_size = 500
total_commits = 0
batch_count = 0

for i in range(0, len(repo_names), batch_size):
    batch = repo_names[i:i+batch_size]
    
    # Build the query
    repo_list = ', '.join(["'{}'".format(repo) for repo in batch])
    query = """SELECT COUNT(*) as commit_count FROM commits 
    WHERE repo_name IN ({}) 
    AND message IS NOT NULL 
    AND LENGTH(message) < 1000 
    AND LOWER(message) NOT LIKE 'merge%' 
    AND LOWER(message) NOT LIKE 'update%' 
    AND LOWER(message) NOT LIKE 'test%'" """.format(repo_list)
    
    print(f"Processing batch {batch_count + 1}/{(len(repo_names) + batch_size - 1) // batch_size}")
    
    # Execute the query (simulated for now since we can't execute inside execute_python)
    # In reality, this would call the query_db tool
    
    batch_count += 1

print('__RESULT__:')
print(json.dumps({
    'total_batches': (len(repo_names) + batch_size - 1) // batch_size,
    'repos_to_process': len(repo_names),
    'batch_size': batch_size,
    'ready_to_execute': True
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'repo_count': 114972, 'sample_repos': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_repos': 114972, 'sample_repos': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}, 'var_functions.execute_python:16': {'total_repos': 114972, 'sample_repos': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook'], 'query_ready': True}, 'var_functions.execute_python:18': {'query': "SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN ('juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook', 'rarenerd/trai...", 'query_length': 3021909, 'repos_count': 114972}, 'var_functions.execute_python:22': {'batch_size': 500, 'query_preview': "SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN ('juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook', 'rarenerd/train', 'wallyqs/ruby-nats', 'dthtvwls/bento', 'darrenleeweber/aws-ops', 'yepengxj/binary-buildpack', 'E..."}}

exec(code, env_args)
