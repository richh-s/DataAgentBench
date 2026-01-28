code = """import json
import re

# Read languages data from file
languages_file = locals()['var_functions.query_db:9']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Get commit counts directly
commit_counts = locals()['var_functions.query_db:12']

# Parse language descriptions to find main language for each repo
repo_main_language = {}

for row in languages_data:
    repo_name = row['repo_name']
    lang_desc = row['language_description']
    
    # Extract language names and byte counts
    lang_pattern = r'(\w+)\s*\(\s*([\d,]+)\s*bytes\s*\)'
    matches = re.findall(lang_pattern, lang_desc)
    
    if matches:
        # Find language with max bytes
        max_bytes = 0
        main_lang = None
        
        for lang, bytes_str in matches:
            bytes_val = int(bytes_str.replace(',', ''))
            if bytes_val > max_bytes:
                max_bytes = bytes_val
                main_lang = lang
        
        if main_lang:
            repo_main_language[repo_name] = main_lang

# Filter out repos where main language is Python
non_python_repos = {}
for repo, lang in repo_main_language.items():
    if lang.lower() != 'python':
        non_python_repos[repo] = lang

# Create a dictionary of commit counts for easy lookup
commit_count_dict = {}
for row in commit_counts:
    commit_count_dict[row['repo_name']] = int(row['commit_count'])

# Find common repos between language data and commit data
common_repos = set(non_python_repos.keys()).intersection(set(commit_count_dict.keys()))

# Create list of repos with commit counts and main languages
filtered_repos = []
for repo in common_repos:
    filtered_repos.append({
        'repo_name': repo,
        'main_language': non_python_repos[repo],
        'commit_count': commit_count_dict[repo]
    })

# For debugging, let's check the top repos by commit count first
top_by_commits = sorted(filtered_repos, key=lambda x: x['commit_count'], reverse=True)[:10]

result = {
    'top_10_by_commits': top_by_commits
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:24': {'languages_type': "<class 'str'>", 'commit_type': "<class 'list'>", 'commit_is_list': True}}

exec(code, env_args)
