code = """import json

# Load qualified repositories
qualified_file_path = locals()['var_functions.query_db:18']
if isinstance(qualified_file_path, str) and qualified_file_path.endswith('.json'):
    with open(qualified_file_path, 'r') as f:
        qualified_repos_list = json.load(f)
else:
    qualified_repos_list = locals()['var_functions.query_db:18']

qualified_names = {repo['repo_name'] for repo in qualified_repos_list}

# Load all distinct repositories from commits
all_commits_file = locals()['var_functions.query_db:40']
if isinstance(all_commits_file, str) and all_commits_file.endswith('.json'):
    with open(all_commits_file, 'r') as f:
        commits_repos_list = json.load(f)
else:
    commits_repos_list = locals()['var_functions.query_db:40']

commits_names = {repo['repo_name'] for repo in commits_repos_list}

# Find intersection
intersection = qualified_names & commits_names

print('__RESULT__:')
print(json.dumps({
    'qualified_repos_count': len(qualified_names),
    'commits_repos_count': len(commits_names),
    'intersection_count': len(intersection),
    'intersection_repos': list(intersection),
    'sample_qualified': list(qualified_names)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['languages', 'repos', 'licenses'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'qualified_repos_count': 39, 'example_repos': 'file_stora'}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [], 'var_functions.query_db:26': [], 'var_functions.query_db:28': [{'repo_name': 'facebook/react'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'tensorflow/tensorflow'}], 'var_functions.query_db:30': [{'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'twbs/bootstrap'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'repo_counts': {'torvalds/linux': 7}, 'total_count': 7}, 'var_functions.execute_python:36': {'qualified_repos_total': 114972, 'repos_found_in_commits': 0, 'example_repos_found': [], 'example_qualified_not_found': ['baslr/ArangoDB', 'flyhard/awsHashicorpStack', 'amollenkopf/dcos-iot-demo', 'stevengill/cordova-lib', 'menghan/shadowsocks-go', 'pralexa/awsebcli', 'objectiser/rtgov', 'JasonHZXie/Mycat-Web', 'cuiqunhao/jstorm', 'uhm-coe/assist']}, 'var_functions.query_db:38': [{'total': '16135'}], 'var_functions.query_db:40': [{'repo_name': 'torvalds/linux', 'commit_count': '14315'}, {'repo_name': 'apple/swift', 'commit_count': '1021'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '322'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '176'}, {'repo_name': 'facebook/react', 'commit_count': '160'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '141'}]}

exec(code, env_args)
