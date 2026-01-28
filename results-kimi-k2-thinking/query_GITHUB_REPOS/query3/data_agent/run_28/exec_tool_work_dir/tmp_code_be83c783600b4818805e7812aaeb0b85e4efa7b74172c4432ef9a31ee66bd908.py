code = """import json
import os

# Read the result file
result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    repo_data = json.load(f)

# Extract repo names
repo_names = [item['repo_name'] for item in repo_data]
print(f"Total repos with Shell and Apache-2.0: {len(repo_names)}")
print(f"Sample repos: {repo_names[:5]}")

# Generate the IN clause for SQL
# Since there are many repos, we need to process in batches to avoid SQL query length limits
batch_size = 100
batches = [repo_names[i:i + batch_size] for i in range(0, len(repo_names), batch_size)]
print(f"Number of batches: {len(batches)}")

# Print first batch for verification
print(f"First batch: {batches[0]}")

print('__RESULT__:')
print(json.dumps({'repo_list': repo_names, 'batch_info': {'batch_size': batch_size, 'num_batches': len(batches)}}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
