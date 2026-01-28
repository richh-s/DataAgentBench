code = """import json
import re
from collections import defaultdict

# Load languages data from file
languages_file = locals()['var_functions.query_db:20']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Load commit data
commit_data = locals()['var_functions.query_db:12']

# Parse language descriptions to extract the primary language
# by finding the language with the most bytes mentioned

def extract_primary_language(description):
    # Find all language-byte pairs like "Ruby (22,438 bytes)"
    pattern = r'(\w+)\s*\(([\d,]+)\s+bytes\)'
    matches = re.findall(pattern, description)
    
    if not matches:
        return None
    
    # Convert bytes to int and find the language with max bytes
    max_bytes = 0
    primary_lang = None
    for lang, byte_str in matches:
        byte_count = int(byte_str.replace(',', ''))
        if byte_count > max_bytes:
            max_bytes = byte_count
            primary_lang = lang
    
    return primary_lang

# Create mapping of repo -> primary language
repo_to_primary_lang = {}
for entry in languages_data:
    repo = entry['repo_name']
    lang = extract_primary_language(entry['language_description'])
    if lang:
        repo_to_primary_lang[repo] = lang

print('Total repositories with primary language:', len(repo_to_primary_lang))
print('Total repositories with commit data:', len(commit_data))

# Check which of the top commit repos have Python as primary language
top_repos_by_commits = commit_data[:10]
print('\nTop 10 repos by commits, checking primary language:')
for i, entry in enumerate(top_repos_by_commits, 1):
    repo = entry['repo_name']
    commits = entry['commit_count']
    primary_lang = repo_to_primary_lang.get(repo, 'Unknown')
    is_python = primary_lang.lower() == 'python' if primary_lang != 'Unknown' else False
    print(f'  {i}. {repo}: {commits} commits, primary lang: {primary_lang}, is_python: {is_python}')"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:9': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:8': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
