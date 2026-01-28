code = """import json

# Get the full commit data
with open(locals()['var_functions.query_db:32'], 'r') as f:
    commit_result = json.load(f)

# Check repos with their messages
repos_with_messages = {}
for commit in commit_result:
    repo_name = commit['repo_name']
    message = commit['message']
    if repo_name not in repos_with_messages:
        repos_with_messages[repo_name] = []
    # Filter messages based on criteria
    if (message and len(message) < 1000 and 
        not message.lower().startswith(('merge', 'update', 'test'))):
        repos_with_messages[repo_name].append(message)

print('__RESULT__:')
print(json.dumps({
    'repo_counts': {repo: len(msgs) for repo, msgs in repos_with_messages.items()},
    'total_count': sum(len(msgs) for msgs in repos_with_messages.values())
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['languages', 'repos', 'licenses'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'qualified_repos_count': 39, 'example_repos': 'file_stora'}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [], 'var_functions.query_db:26': [], 'var_functions.query_db:28': [{'repo_name': 'facebook/react'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'tensorflow/tensorflow'}], 'var_functions.query_db:30': [{'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'twbs/bootstrap'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
