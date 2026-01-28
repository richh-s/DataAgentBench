code = """import json
import re

# Get commit data
commit_storage_key = 'var_functions.query_db:24'
commit_data = locals()[commit_storage_key]

# Get language data
lang_storage_key = 'var_functions.query_db:0'
lang_file = locals()[lang_storage_key]
with open(lang_file, 'r') as f:
    lang_data = json.load(f)

# Parse language data to find main language for each repo
repo_main_lang = {}
for item in lang_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    # Extract language-byte pairs
    lang_bytes = re.findall(r'(\w+)\s*\((\d+)\s*bytes?\)', lang_desc)
    
    if lang_bytes:
        lang_dict = {}
        for lang, bytes_count in lang_bytes:
            lang_dict[lang] = int(bytes_count)
        main_lang = max(lang_dict, key=lang_dict.get)
        repo_main_lang[repo_name] = main_lang

# Check which of our top commit repos have language data
top_commit_repos = [item['repo_name'] for item in commit_data]
available_repos = [repo for repo in top_commit_repos if repo in repo_main_lang]

# Get language info for available repos
repo_info = []
for repo in available_repos:
    repo_info.append({
        'repo_name': repo,
        'main_language': repo_main_lang[repo],
        'commit_count': next(item['commit_count'] for item in commit_data if item['repo_name'] == repo)
    })

print('__RESULT__:')
print(json.dumps({
    'available_repos': len(available_repos),
    'repo_info': repo_info,
    'missing_repos': [repo for repo in top_commit_repos if repo not in repo_main_lang]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'type': "<class 'str'>", 'preview': 'file_storage/functions.query_db:0.json'}, 'var_functions.execute_python:12': {'total_repos': 914225, 'non_python_repos': 893211, 'language_counts': {'Shell': 185349, 'CSS': 113124, 'HTML': 94995, 'Makefile': 80811, 'JavaScript': 80595, 'Ruby': 63902, 'C': 34293, 'ApacheConf': 33937, 'Batchfile': 31309, 'Python': 21014}, 'sample_non_python': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'tibastral/web_motion', 'Haegin/stately', 'Scripted/pandago-ruby']}, 'var_functions.query_db:14': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:20': {'type': "<class 'list'>", 'value': "[{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode"}, 'var_functions.execute_python:22': ['twbs/bootstrap', 'Microsoft/vscode', 'tensorflow/tensorflow'], 'var_functions.query_db:24': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
