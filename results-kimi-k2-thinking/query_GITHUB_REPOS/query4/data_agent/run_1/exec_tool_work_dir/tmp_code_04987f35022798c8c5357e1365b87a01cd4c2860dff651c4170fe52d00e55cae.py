code = """import json
import re

# Access the variables from storage using locals()
languages_data = locals()['var_functions.query_db:6']
commit_data = locals()['var_functions.query_db:7']

# Parse language descriptions to find the main language
def extract_main_language(lang_desc):
    # Pattern to match language and bytes: Language (bytes)
    pattern = r'(\w+)\s*\((\d+)\s*bytes?\)'
    matches = re.findall(pattern, lang_desc)
    
    if not matches:
        return None
    
    # Find the language with the highest byte count
    main_lang = None
    max_bytes = 0
    for lang, bytes_str in matches:
        bytes_count = int(bytes_str)
        if bytes_count > max_bytes:
            max_bytes = bytes_count
            main_lang = lang
    
    return main_lang

# Create a dictionary mapping repo_name to main language
repo_languages = {}
for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    main_lang = extract_main_language(lang_desc)
    if main_lang:
        repo_languages[repo_name] = main_lang

# Filter out repositories whose main language is Python
non_python_repos = {repo: lang for repo, lang in repo_languages.items() if lang.lower() != 'python'}

# Create a dictionary from commit data
commit_dict = {item['repo_name']: int(item['commit_count']) for item in commit_data}

# Find repositories that are in both datasets and not Python
results = []
for repo, lang in non_python_repos.items():
    if repo in commit_dict:
        results.append({
            'repo_name': repo,
            'main_language': lang,
            'commit_count': commit_dict[repo]
        })

# Sort by commit count descending
results.sort(key=lambda x: x['commit_count'], reverse=True)

# Get top 5 repositories (only returning the names as requested)
top_5_names = [repo['repo_name'] for repo in results[:5]]

# Print in the required format
result_str = json.dumps(top_5_names, indent=2)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:10': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
