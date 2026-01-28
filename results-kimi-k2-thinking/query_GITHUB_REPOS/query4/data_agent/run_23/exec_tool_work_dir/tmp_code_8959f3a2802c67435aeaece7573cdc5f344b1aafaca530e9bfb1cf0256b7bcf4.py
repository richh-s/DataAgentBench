code = """import json
import re

# Access data from storage
languages_file = locals()['var_functions.query_db:18']
commit_data = locals()['var_functions.query_db:12']

# Read language data
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Extract repo names from language data
repos_with_lang = set(item['repo_name'] for item in languages_data)

# Check which top commit repos have language data
print('Top commit repos:', [r['repo_name'] for r in commit_data])
print()
print('Repos with language data count:', len(repos_with_lang))
print('Sample repos with language data:', list(repos_with_lang)[:10])
print()

# Check overlap
overlap = []
for repo in commit_data:
    if repo['repo_name'] in repos_with_lang:
        overlap.append(repo['repo_name'])

print('Overlap between top commits and language data:', overlap)
print('Count:', len(overlap))

# Parse language for overlapping repos
repo_lang_info = {}
for item in languages_data:
    repo_name = item['repo_name']
    if repo_name in [r['repo_name'] for r in commit_data]:
        lang_desc = item['language_description']
        
        # Extract languages and bytes
        lang_bytes = {}
        pattern = r'(\w+)\s*\((\d+)\s*bytes\)'
        matches = re.findall(pattern, lang_desc)
        
        for lang, bytes_str in matches:
            lang_bytes[lang] = int(bytes_str)
        
        if lang_bytes:
            main_lang = max(lang_bytes, key=lang_bytes.get)
            total_bytes = sum(lang_bytes.values())
            repo_lang_info[repo_name] = {
                'main_lang': main_lang,
                'lang_bytes': lang_bytes,
                'total_bytes': total_bytes
            }

print()
print('Language info for repos with both data:')
for repo, info in repo_lang_info.items():
    if repo in [r['repo_name'] for r in commit_data]:
        commit_count = next(r['commit_count'] for r in commit_data if r['repo_name'] == repo)
        print(f"{repo}: {info['main_lang']} ({commit_count} commits)")"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}], 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:16': ['twbs/bootstrap', 'Microsoft/vscode', 'tensorflow/tensorflow'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
