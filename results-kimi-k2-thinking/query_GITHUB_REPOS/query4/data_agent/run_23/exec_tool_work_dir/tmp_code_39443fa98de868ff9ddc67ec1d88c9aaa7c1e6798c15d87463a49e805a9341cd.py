code = """import json
import re

# Access the language data from storage
languages_var = locals()['var_functions.query_db:10']
with open(languages_var, 'r') as f:
    languages_data = json.load(f)

# Access the commit data from storage
commit_data = locals()['var_functions.query_db:12']

# Parse language descriptions to find main language
repo_languages = {}
for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    # Extract language and byte information using regex
    # Pattern matches: Language (bytes)
    lang_bytes = {}
    pattern = r'(\w+)\s*\((\d+)\s*bytes\)'
    matches = re.findall(pattern, lang_desc)
    
    for lang, bytes_str in matches:
        lang_bytes[lang] = int(bytes_str)
    
    if lang_bytes:
        # Find language with max bytes (main language)
        main_lang = max(lang_bytes, key=lang_bytes.get)
        repo_languages[repo_name] = main_lang

# Filter to get top repos where main language is NOT Python
top_repos = []
for repo in commit_data:
    repo_name = repo['repo_name']
    commit_count = int(repo['commit_count'])
    
    # Check if we have language info for this repo
    if repo_name in repo_languages:
        main_lang = repo_languages[repo_name]
        if main_lang != 'Python':
            top_repos.append({
                'repo_name': repo_name,
                'commit_count': commit_count,
                'main_language': main_lang
            })

# Sort by commit count descending and get top 5
top_repos_sorted = sorted(top_repos, key=lambda x: x['commit_count'], reverse=True)
top_5_repos = top_repos_sorted[:5]

# Extract just the repository names
result = [repo['repo_name'] for repo in top_5_repos]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}], 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
