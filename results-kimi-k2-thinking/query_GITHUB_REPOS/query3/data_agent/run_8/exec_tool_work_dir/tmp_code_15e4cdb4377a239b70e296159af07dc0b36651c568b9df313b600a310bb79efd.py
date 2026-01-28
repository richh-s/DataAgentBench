code = """import json

# Access the stored repository list
repo_names_data = locals()['var_functions.execute_python:10']

# Parse the JSON string to get the list
repo_names = json.loads(repo_names_data)

print(f'Total repositories to check: {len(repo_names)}')

# Create a comma-separated string of repo names for SQL IN clause
# We'll batch them to avoid hitting query size limits
batch_size = 100
batches = []
for i in range(0, len(repo_names), batch_size):
    batch = repo_names[i:i+batch_size]
    quoted_batch = ', '.join([f"'{name}'" for name in batch])
    batches.append(quoted_batch)

print(f'Created {len(batches)} batches of {batch_size} repos each')
print('__RESULT__:')
print(json.dumps(batches[:2]))  # Show first 2 batches"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json'}

exec(code, env_args)
