code = """import json
import re

# Load the language data from file
lang_file = locals()['var_functions.query_db:10']
with open(lang_file, 'r') as f:
    lang_data = json.load(f)

# Get the commit count data (which is already in the result from query_db:8)
commit_data = locals()['var_functions.query_db:8']

# Create a dictionary for language lookup
lang_dict = {item['repo_name']: item['language_description'] for item in lang_data}

# Function to extract main language from description
def get_main_language(lang_desc):
    if not lang_desc:
        return None
    
    # Pattern to match "Language (bytes)" format
    pattern = r'(\w+)\s*\((\d+)\s*bytes?\)'
    matches = re.findall(pattern, lang_desc)
    
    if not matches:
        return None
    
    # Find the language with max bytes
    max_bytes = 0
    main_lang = None
    for lang, bytes_str in matches:
        bytes_val = int(bytes_str)
        if bytes_val > max_bytes:
            max_bytes = bytes_val
            main_lang = lang
    
    return main_lang

# Process each repository with commits
results = []
for commit_item in commit_data:
    repo_name = commit_item['repo_name']
    commit_count = int(commit_item['commit_count'])
    
    # Get language description
    lang_desc = lang_dict.get(repo_name)
    if not lang_desc:
        continue
    
    # Get main language
    main_lang = get_main_language(lang_desc)
    if not main_lang:
        continue
    
    # Check if main language is NOT Python
    if main_lang.lower() != 'python':
        results.append({
            'repo_name': repo_name,
            'commit_count': commit_count,
            'main_language': main_lang
        })

# Sort by commit count descending
results_sorted = sorted(results, key=lambda x: x['commit_count'], reverse=True)

# Take top 5
top_5 = results_sorted[:5]

# Extract just the repository names
repo_names = [item['repo_name'] for item in top_5]

# Format output
json_result = json.dumps(repo_names)
print('__RESULT__:')
print(json_result)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:5': [{'commit': '78e3f1f01d23c1a0d5828669d35afa2e7951987d', 'repo_name': 'torvalds/linux'}, {'commit': '4a4e07c1bdbbc24d905e4c266b92cada9371db5d', 'repo_name': 'torvalds/linux'}, {'commit': 'afe1bb73f8ed588ab6268c27c5a447fe0484e48f', 'repo_name': 'torvalds/linux'}, {'commit': 'b7ac233515c6263d6cb471d9e0f57bdd7ea36894', 'repo_name': 'torvalds/linux'}, {'commit': '71c11c378f46e42ca67c1e227646ce23bf43a8c6', 'repo_name': 'torvalds/linux'}, {'commit': '76cdd58e558669366adfaded436fda01b30cce3e', 'repo_name': 'torvalds/linux'}, {'commit': '2565409fc0303f3ab8d66b8326702a687962a29b', 'repo_name': 'torvalds/linux'}, {'commit': '7779d7bed950a7fb1af4f540c2f82a6b81b65901', 'repo_name': 'torvalds/linux'}, {'commit': '3443ad095fc330ace0ef23bf965354a56298bf58', 'repo_name': 'torvalds/linux'}, {'commit': '42e41c54d61e32e8a349943607daa53205324d7f', 'repo_name': 'torvalds/linux'}], 'var_functions.query_db:6': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'facebook/react', 'commit_count': '178'}], 'var_functions.query_db:8': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
