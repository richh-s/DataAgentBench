code = """import json
import pandas as pd
import re

# Load language data
lang_data_path = locals()['var_functions.query_db:2']
with open(lang_data_path, 'r') as f:
    all_languages = json.load(f)

# Get commit data
commit_data = locals()['var_functions.query_db:8']

# Process languages to find primary language
print('Loading languages...')
print(f'Total language records: {len(all_languages)}')
print(f'Commit records: {len(commit_data)}')

# Get repo names from commit data
commit_repo_names = set([item['repo_name'] for item in commit_data])
print(f'Repos from commits: {commit_repo_names}')

# Find language info for these repos
non_python_repos = []
target_repos = []

for lang_record in all_languages:
    if lang_record['repo_name'] in commit_repo_names:
        lang_desc = lang_record['language_description']
        repo_name = lang_record['repo_name']
        
        # Parse language description
        pattern = r'([\w#+-]+)\s*\(([\d,]+)\s*bytes?\)'
        matches = re.findall(pattern, lang_desc)
        
        if matches:
            # Find language with max bytes
            max_lang = None
            max_bytes = 0
            for lang, byte_str in matches:
                try:
                    byte_count = int(byte_str.replace(',', ''))
                    if byte_count > max_bytes:
                        max_bytes = byte_count
                        max_lang = lang.lower()
                except:
                    continue
            
            if max_lang != 'python':
                target_repos.append((repo_name, max_lang, byte_count))
                non_python_repos.append(repo_name)

print(f'Non-Python repos found: {non_python_repos}')
print(f'Target repos: {target_repos}')

result = {
    'non_python_repos': non_python_repos,
    'all_commit_repos': list(commit_repo_names)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:14': {'lang_type': "<class 'str'>", 'commit_type': "<class 'list'>", 'commit_count': 6, 'lang_count': 3325634}}

exec(code, env_args)
