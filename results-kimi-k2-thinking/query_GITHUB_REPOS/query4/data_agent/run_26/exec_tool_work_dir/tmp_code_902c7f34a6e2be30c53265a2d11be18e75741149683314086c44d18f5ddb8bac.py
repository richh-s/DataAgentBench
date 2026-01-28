code = """import json
import re

# Load languages data
languages_file_path = locals()['var_functions.query_db:6']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

# Get commit data
commits_data = locals()['var_functions.query_db:5']

# Parse languages
repo_languages = {}
for row in languages_data:
    repo_name = row['repo_name']
    lang_desc = row['language_description']
    
    lang_pattern = r'(\w+)\s*\((\d+(?:,\d+)*)\s*bytes?\)'
    matches = re.findall(lang_pattern, lang_desc)
    
    if matches:
        lang_bytes = {}
        for lang, byte_str in matches:
            byte_count = int(byte_str.replace(',', ''))
            lang_bytes[lang] = byte_count
        
        if lang_bytes:
            main_lang = max(lang_bytes, key=lang_bytes.get)
            repo_languages[repo_name] = main_lang

# Check all commit repos and their main languages
all_repos_info = []
for commit_row in commits_data:
    repo_name = commit_row['repo_name']
    commit_count = int(commit_row['commit_count'])
    main_lang = repo_languages.get(repo_name, 'Unknown')
    all_repos_info.append((repo_name, commit_count, main_lang))

# Sort by commit count descending
all_repos_info.sort(key=lambda x: x[1], reverse=True)

# Filter non-Python repositories
non_python_repos = [repo for repo in all_repos_info if repo[2] != 'Python']

# Get top 5 - names only
top_5_names = [repo[0] for repo in non_python_repos[:5]]

result = {
    'all_repos_with_main_lang': all_repos_info,
    'non_python_top_5_names': top_5_names
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': {'top_5_repos': [['apple/swift', 1051, 'Swift'], ['twbs/bootstrap', 340, 'JavaScript'], ['Microsoft/vscode', 190, 'TypeScript'], ['facebook/react', 178, 'JavaScript']]}}

exec(code, env_args)
