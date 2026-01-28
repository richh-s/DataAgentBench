code = """import json

# Read the repos list from the file
with open('file_storage/functions.query_db:10.json', 'r') as f:
    repos_data = json.load(f)

# Extract repo names
apache_shell_repos = [repo['repo_name'] for repo in repos_data]

# Read the commits from the file
with open('file_storage/functions.query_db:26.json', 'r') as f:
    commits_data = json.load(f)

# Filter commits that are in our repos list and meet criteria
def is_valid_message(msg):
    if not msg:
        return False
    if len(msg) >= 1000:
        return False
    lower_msg = msg.lower()
    if lower_msg.startswith('merge') or lower_msg.startswith('update') or lower_msg.startswith('test'):
        return False
    return True

target_commits = []
for commit in commits_data:
    if commit['repo_name'] in apache_shell_repos and is_valid_message(commit.get('message', '')):
        target_commits.append(commit)

print('__RESULT__:')
print(json.dumps({
    'matching_commits': len(target_commits),
    'unique_repos': len(set(c['repo_name'] for c in target_commits)),
    'sample_commits': [
        {'repo': c['repo_name'], 'message_preview': c['message'][:100]} 
        for c in target_commits[:5]
    ] if target_commits else []
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['commits', 'contents', 'files'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'repo_count': 114972, 'first_5_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.query_db:20': [{'total_commits': '17976'}], 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.query_db:24': [{'count': '0'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
