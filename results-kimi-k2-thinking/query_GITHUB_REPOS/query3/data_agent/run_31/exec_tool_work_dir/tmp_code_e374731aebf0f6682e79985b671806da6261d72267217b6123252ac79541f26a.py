code = """import json

# Read the repository list from the file
repo_file_path = 'var_functions.query_db:0'
with open(repo_file_path, 'r') as f:
    repo_data = json.load(f)

# Extract repo names and format them for SQL IN clause
repo_names = [repo['repo_name'] for repo in repo_data]
print('Total repos found:', len(repo_names))
print('First 5 repos:', repo_names[:5])

# Create a comma-separated string of quoted repo names for SQL
# Handle the case where there might be many repos
if len(repo_names) > 0:
    # For DuckDB, we need to use proper string escaping
    escaped_repos = []
    for name in repo_names[:100]:  # Limit to first 100 to avoid query size issues
        # Escape single quotes by doubling them
        escaped = name.replace("'", "''")
        escaped_repos.append(f"'{escaped}'")
    
    repo_list_str = ','.join(escaped_repos)
    print('Formatted repo list (first 5):', ','.join(escaped_repos[:5]))
else:
    repo_list_str = "''"
    
print('Ready to query commits table')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': [{'repo_name': 'facebook/react'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'tensorflow/tensorflow'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
