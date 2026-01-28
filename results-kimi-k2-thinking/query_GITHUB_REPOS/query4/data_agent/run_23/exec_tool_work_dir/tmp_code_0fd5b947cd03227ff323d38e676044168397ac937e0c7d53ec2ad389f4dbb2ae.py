code = """import json
import re

# Access data from storage
languages_file = locals()['var_functions.query_db:18']
commit_data = locals()['var_functions.query_db:12']

# Read language data
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Debug: Check structure of language data
print('Total language records:', len(languages_data))
print('First few records:')
for i, item in enumerate(languages_data[:5]):
    print(f"  {i}: {item}")

# Build language mapping
repo_languages = {}
for item in languages_data:
    repo_name = item.get('repo_name')
    lang_desc = item.get('language_description', '')
    
    if not repo_name or not lang_desc:
        continue
        
    # Extract languages and bytes
    lang_bytes = {}
    pattern = r'(\w+)\s*\((\d+)\s*bytes\)'
    matches = re.findall(pattern, lang_desc)
    
    for lang, bytes_str in matches:
        lang_bytes[lang] = int(bytes_str)
    
    if lang_bytes:
        main_lang = max(lang_bytes, key=lang_bytes.get)
        repo_languages[repo_name] = main_lang

print()
print('Repos with parsed language info:', len(repo_languages))
print('Sample:', list(repo_languages.items())[:10])

# Check which top commit repos we have language data for
top_commit_repos = [r['repo_name'] for r in commit_data]
print()
print('Top commit repos:', top_commit_repos)
print()

repos_with_lang_info = []
for repo_info in commit_data:
    repo_name = repo_info['repo_name']
    commit_count = int(repo_info['commit_count'])
    
    if repo_name in repo_languages:
        main_lang = repo_languages[repo_name]
        repos_with_lang_info.append({
            'repo_name': repo_name,
            'commit_count': commit_count,
            'main_language': main_lang
        })

print('Repos with both commit and language data:', len(repos_with_lang_info))
for repo in repos_with_lang_info:
    print(f"  {repo['repo_name']}: {repo['main_language']} - {repo['commit_count']} commits")

# Sort and filter for non-Python
top_non_python = [r for r in repos_with_lang_info if r['main_language'] != 'Python']
top_non_python_sorted = sorted(top_non_python, key=lambda x: x['commit_count'], reverse=True)

print()
print('Top 5 non-Python repos:')
top_5 = top_non_python_sorted[:5]
for repo in top_5:
    print(f"  {repo['repo_name']}: {repo['main_language']} ({repo['commit_count']} commits)")

# Extract just names
result = [r['repo_name'] for r in top_5]
print()
print('Final result:', result)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}], 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:16': ['twbs/bootstrap', 'Microsoft/vscode', 'tensorflow/tensorflow'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
