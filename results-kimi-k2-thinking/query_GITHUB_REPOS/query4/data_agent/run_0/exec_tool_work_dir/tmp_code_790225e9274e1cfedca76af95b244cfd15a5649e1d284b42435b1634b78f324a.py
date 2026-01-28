code = """import json
import re

# Load data
languages_file = locals()['var_functions.query_db:20']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

commit_data = locals()['var_functions.query_db:12']

# Extract primary language from description
def get_primary_lang(desc):
    pattern = r'(\w+)\s*\(([\d,]+)\s+bytes\)'
    matches = re.findall(pattern, desc)
    if not matches:
        return None
    # Find language with maximum bytes
    max_bytes = 0
    primary = None
    for lang, byte_str in matches:
        bytes_count = int(byte_str.replace(',', ''))
        if bytes_count > max_bytes:
            max_bytes = bytes_count
            primary = lang
    return primary

# Build language map
repo_lang = {}
for item in languages_data:
    repo = item['repo_name']
    lang = get_primary_lang(item['language_description'])
    if lang:
        repo_lang[repo] = lang

# Process all commit data - we need at least top 10 to ensure we get 5 that aren't Python
print('__RESULT__:')
print('Number of commit entries to process: ' + str(len(commit_data)))

not_python_repos = []
for commit in commit_data:
    repo = commit['repo_name']
    if repo in repo_lang:
        lang = repo_lang[repo]
        if lang.lower() != 'python':
            not_python_repos.append({
                'repo': repo,
                'commits': int(commit['commit_count']),
                'lang': lang
            })

print('Repos with language info and not Python: ' + str(len(not_python_repos)))
if not_python_repos:
    sorted_repos = sorted(not_python_repos, key=lambda x: x['commits'], reverse=True)[:5]
    output = [r['repo'] for r in sorted_repos]
    print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:9': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:8': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:48': ['apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react']}

exec(code, env_args)
