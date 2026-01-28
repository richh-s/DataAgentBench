code = """import json
import re

# Load the language data from the file
with open('/tmp/tmp_hwwwwl7.json', 'r') as f:
    language_data = json.load(f)

# Load the commit count data from storage
commit_data = locals()['var_functions.query_db:10']

# Parse language descriptions to find the main language for each repository
repo_main_language = {}

for entry in language_data:
    repo_name = entry['repo_name']
    language_description = entry['language_description']
    
    # Extract language names and byte counts using regex
    # Pattern looks for language names followed by byte counts in parentheses
    pattern = r'(\w+) \((\d+,?\d*) bytes\)'
    matches = re.findall(pattern, language_description)
    
    if matches:
        # Find the language with the highest byte count
        max_bytes = 0
        main_lang = None
        for lang, bytes_str in matches:
            bytes_val = int(bytes_str.replace(',', ''))
            if bytes_val > max_bytes:
                max_bytes = bytes_val
                main_lang = lang
        
        repo_main_language[repo_name] = main_lang

# Create a list of repositories with their commit counts and main languages
repo_commit_info = []

for commit_entry in commit_data:
    repo_name = commit_entry['repo_name']
    commit_count = int(commit_entry['commit_count'])
    main_lang = repo_main_language.get(repo_name, 'Unknown')
    
    repo_commit_info.append({
        'repo_name': repo_name,
        'commit_count': commit_count,
        'main_language': main_lang
    })

# Filter out repositories whose main language is Python
non_python_repos = [repo for repo in repo_commit_info if repo['main_language'] != 'Python']

# Sort by commit count descending and take top 5
top_5_non_python = sorted(non_python_repos, key=lambda x: x['commit_count'], reverse=True)[:5]

# Extract just the repository names
result = [repo['repo_name'] for repo in top_5_non_python]

# Print in the required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:6': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
