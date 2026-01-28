code = """import json
import pandas as pd
import re

# Load the language data from file
lang_data_path = locals()['var_functions.query_db:2']
with open(lang_data_path, 'r') as f:
    all_languages = json.load(f)

# Get commit data
commit_data = locals()['var_functions.query_db:8']

# Extract primary language for each repository
def get_primary_language(lang_record):
    """Get the primary language from a language description record"""
    repo_name = lang_record['repo_name']
    lang_desc = lang_record['language_description']
    
    if not lang_desc:
        return {'repo_name': repo_name, 'primary_language': None, 'description': lang_desc}
    
    # Find all language-byte pairs
    import re
    pattern = r'(\w(?:[\w+#-]*\w)?)\s*\(([\d,]+)\s*bytes?\)'
    matches = re.findall(pattern, lang_desc)
    
    if not matches:
        return {'repo_name': repo_name, 'primary_language': None, 'description': lang_desc}
    
    # Find language with max bytes
    max_lang = None
    max_bytes = -1
    
    for lang, byte_str in matches:
        try:
            byte_count = int(byte_str.replace(',', ''))
            if byte_count > max_bytes:
                max_bytes = byte_count
                max_lang = lang.lower()  # Normalize to lowercase
        except:
            continue
    
    return {'repo_name': repo_name, 'primary_language': max_lang, 'description': lang_desc}

# Process only the repos we care about (from commit data)
commit_repos = {item['repo_name'] for item in commit_data}
print(f'Repositories from commit data: {commit_repos}')

# Filter and process languages for commit repos
target_langs = []
for record in all_languages:
    if record['repo_name'] in commit_repos:
        processed = get_primary_language(record)
        target_langs.append(processed)
        if len(target_langs) >= len(commit_repos):
            break

print(f'Found {len(target_langs)} language records for commit repos')
print(f'Sample: {target_langs[:3]}')

# Check which ones are NOT primarily Python
non_python_repos = [
    item['repo_name'] 
    for item in target_langs 
    if item['primary_language'] != 'python'
]

print(f'Non-Python repos from commit data: {non_python_repos}')

# Create final result to return
result = {
    'non_python_repos': non_python_repos,
    'all_commit_repos': list(commit_repos),
    'language_records_processed': len(target_langs),
    'sample_lang_record': target_langs[0] if target_langs else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:14': {'lang_type': "<class 'str'>", 'commit_type': "<class 'list'>", 'commit_count': 6, 'lang_count': 3325634}}

exec(code, env_args)
