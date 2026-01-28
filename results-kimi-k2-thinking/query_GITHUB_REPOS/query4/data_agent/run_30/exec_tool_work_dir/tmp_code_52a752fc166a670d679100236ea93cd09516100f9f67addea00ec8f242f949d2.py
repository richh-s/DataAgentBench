code = """import json
import re

# Get commit data - it's already a list
commit_storage_key = 'var_functions.query_db:14'
commit_data = locals()[commit_storage_key]

# Get language data from file
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

# Filter repos to only those whose main language is NOT Python
non_python_repos = {repo: lang for repo, lang in repo_main_lang.items() if lang != 'Python'}

# Filter commit data to only include non-Python repos and sort by commit count
filtered_commits = []
for commit_item in commit_data:
    repo_name = commit_item['repo_name']
    if repo_name in non_python_repos:
        filtered_commits.append({
            'repo_name': repo_name,
            'commit_count': int(commit_item['commit_count']),
            'main_language': non_python_repos[repo_name]
        })

# Sort by commit count descending and get top 5
top_5 = sorted(filtered_commits, key=lambda x: x['commit_count'], reverse=True)[:5]

# Extract just the repository names
result = [repo['repo_name'] for repo in top_5]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'type': "<class 'str'>", 'preview': 'file_storage/functions.query_db:0.json'}, 'var_functions.execute_python:12': {'total_repos': 914225, 'non_python_repos': 893211, 'language_counts': {'Shell': 185349, 'CSS': 113124, 'HTML': 94995, 'Makefile': 80811, 'JavaScript': 80595, 'Ruby': 63902, 'C': 34293, 'ApacheConf': 33937, 'Batchfile': 31309, 'Python': 21014}, 'sample_non_python': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'tibastral/web_motion', 'Haegin/stately', 'Scripted/pandago-ruby']}, 'var_functions.query_db:14': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:20': {'type': "<class 'list'>", 'value': "[{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode"}}

exec(code, env_args)
