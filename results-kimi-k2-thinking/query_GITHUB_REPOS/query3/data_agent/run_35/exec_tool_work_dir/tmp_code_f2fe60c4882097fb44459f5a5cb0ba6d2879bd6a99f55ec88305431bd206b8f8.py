code = """import json

# Read the repository list file
repo_list_file = var_functions.query_db:10

# If it's a file path, read it
if isinstance(repo_list_file, str) and '.json' in repo_list_file:
    with open(repo_list_file, 'r') as f:
        repos_data = json.load(f)
else:
    repos_data = repo_list_file

# Create batches of 1000 repositories each
batch_size = 1000
repo_names = [item['repo_name'] for item in repos_data]
batches = [repo_names[i:i+batch_size] for i in range(0, len(repo_names), batch_size)]

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(repo_names),
    'num_batches': len(batches),
    'first_batch': batches[0][:5],  # Show first 5 repos of first batch
    'batch_size': batch_size
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': [{'count_star()': '0'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'commit_count': '0'}], 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'repo_count': '111756'}]}

exec(code, env_args)
