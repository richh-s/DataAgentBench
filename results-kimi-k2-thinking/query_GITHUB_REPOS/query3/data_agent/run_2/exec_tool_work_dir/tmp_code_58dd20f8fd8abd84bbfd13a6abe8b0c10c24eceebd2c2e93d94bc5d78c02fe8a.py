code = """import json

# Get repo names from the previous query
repo_key = 'var_functions.execute_python:38'
if repo_key in locals():
    file_path = locals()[repo_key]
    if isinstance(file_path, str):
        with open(file_path, 'r') as f:
            repo_names = json.load(f)
    else:
        repo_names = file_path
else:
    repo_names = []

# Count the repositories
print(f"Found {len(repo_names)} repositories")
print(f"Sample repos: {repo_names[:5]}")

# Build a SQL query for the artifacts database
# We'll use a smaller batch to avoid query size limits
batch_size = 100
small_batch = repo_names[:batch_size]

# Create the IN clause
in_clause = (", ").join(f"'{name}'" for name in small_batch)

# Build the full query
query = """
SELECT COUNT(*) as commit_count 
FROM commits 
WHERE repo_name IN (""" + in_clause + """) 
  AND length(message) < 1000 
  AND lower(message) NOT LIKE 'merge%' 
  AND lower(message) NOT LIKE 'update%' 
  AND lower(message) NOT LIKE 'test%'
  AND message IS NOT NULL 
  AND trim(message) != ''
"""

print("Query preview (first 500 chars):")
print(query[:500])
print("...")

# Store the query for the next step
result = {
    "repo_count": len(repo_names),
    "batch_size": batch_size,
    "query": query
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['commits', 'contents', 'files'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json'}

exec(code, env_args)
