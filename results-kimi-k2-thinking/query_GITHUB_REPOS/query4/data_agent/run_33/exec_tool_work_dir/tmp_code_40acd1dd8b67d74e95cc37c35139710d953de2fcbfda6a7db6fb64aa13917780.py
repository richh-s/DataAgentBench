code = """import json
import re

# Load non-Python repos
non_python_file = locals()['var_functions.execute_python:18']
with open(non_python_file, 'r') as f:
    non_python_repos = json.load(f)

# Load commit data
commit_data = locals()['var_functions.query_db:22']
commit_repos = {item['repo_name']: int(item['commit_count']) for item in commit_data}

print(f"Total non-Python repos: {len(non_python_repos)}")
print(f"Repos with commit data: {len(commit_repos)}")

# Find intersection
common_repos = []
for repo in non_python_repos:
    if repo in commit_repos:
        common_repos.append((repo, commit_repos[repo]))

# Sort by commit count
common_repos.sort(key=lambda x: x[1], reverse=True)

print(f"Common repos (non-Python with commit data): {len(common_repos)}")
print(f"Top 10: {common_repos[:10]}")

# Check if any of the top repos are in our non-Python list
top_repos_in_our_data = []
for repo, count in commit_repos.items():
    if len(top_repos_in_our_data) >= 20:  # Check top 20
        break
    top_repos_in_our_data.append((repo, count))

print(f"Top repos from commits table: {top_repos_in_our_data}")

# Since there's very little overlap, let me check the actual scope of both datasets
print("__RESULT__:")
print(json.dumps({
    'non_python_count': len(non_python_repos),
    'commit_repos_count': len(commit_repos),
    'common_count': len(common_repos),
    'top_common': common_repos[:10]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.query_db:20': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:22': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
