code = """import json
import re

# Load language data from file
languages_file = locals()['var_functions.query_db:18']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Load commit data
commit_data = locals()['var_functions.query_db:12']

# Parse language descriptions to find main language for each repo
repo_main_language = {}
for item in languages_data:
    repo_name = item.get('repo_name')
    lang_desc = item.get('language_description', '')
    
    if not repo_name or not lang_desc:
        continue
    
    # Extract language names and byte counts
    lang_bytes = {}
    # Pattern matches: Language (bytes) - handles optional commas and spaces
    pattern = r'(\w+)\s*\((\d+,?\d*)\s*bytes\)'
    matches = re.findall(pattern, lang_desc)
    
    for lang, bytes_str in matches:
        # Remove commas from numbers
        clean_bytes = int(bytes_str.replace(',', ''))
        lang_bytes[lang] = clean_bytes
    
    # Determine main language (highest byte count)
    if lang_bytes:
        main_lang = max(lang_bytes, key=lang_bytes.get)
        repo_main_language[repo_name] = main_lang

# Create list of repos with both commit and language data, filtered for non-Python
repos_with_info = []
for repo_info in commit_data:
    repo_name = repo_info['repo_name']
    commit_count = int(repo_info['commit_count'])
    
    if repo_name in repo_main_language:
        main_lang = repo_main_language[repo_name]
        if main_lang != 'Python':
            repos_with_info.append({
                'repo_name': repo_name,
                'commit_count': commit_count,
                'main_language': main_lang
            })

# Sort by commit count descending and get top 5
top_repos = sorted(repos_with_info, key=lambda x: x['commit_count'], reverse=True)[:5]

# Extract just repository names
result = [repo['repo_name'] for repo in top_repos]

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}], 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:16': ['twbs/bootstrap', 'Microsoft/vscode', 'tensorflow/tensorflow'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
