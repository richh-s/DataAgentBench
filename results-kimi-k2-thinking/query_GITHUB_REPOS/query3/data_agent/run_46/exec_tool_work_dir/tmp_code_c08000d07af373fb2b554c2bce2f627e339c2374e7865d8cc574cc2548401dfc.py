code = """import json

# Load commit results
commit_file_path = locals()['var_functions.query_db:32']
if isinstance(commit_file_path, str) and commit_file_path.endswith('.json'):
    with open(commit_file_path, 'r') as f:
        commits_result = json.load(f)
else:
    commits_result = locals()['var_functions.query_db:32']

# Get the qualified repos list
qualified_file_path = locals()['var_functions.query_db:18']
if isinstance(qualified_file_path, str) and qualified_file_path.endswith('.json'):
    with open(qualified_file_path, 'r') as f:
        qualified_repos_list = json.load(f)
else:
    qualified_repos_list = locals()['var_functions.query_db:18']

qualified_repo_names = {repo['repo_name'] for repo in qualified_repos_list}

# Check which qualified repos actually have commits in the commits table
repos_found = []
for commit in commits_result:
    if commit['repo_name'] in qualified_repo_names:
        repos_found.append(commit['repo_name'])

unique_repos_found = set(repos_found)

print('__RESULT__:')
print(json.dumps({
    'qualified_repos_total': len(qualified_repo_names),
    'repos_found_in_commits': len(unique_repos_found),
    'example_repos_found': list(unique_repos_found)[:10],
    'example_qualified_not_found': list(qualified_repo_names - unique_repos_found)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['languages', 'repos', 'licenses'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'qualified_repos_count': 39, 'example_repos': 'file_stora'}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [], 'var_functions.query_db:26': [], 'var_functions.query_db:28': [{'repo_name': 'facebook/react'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'tensorflow/tensorflow'}], 'var_functions.query_db:30': [{'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'twbs/bootstrap'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'repo_counts': {'torvalds/linux': 7}, 'total_count': 7}}

exec(code, env_args)
