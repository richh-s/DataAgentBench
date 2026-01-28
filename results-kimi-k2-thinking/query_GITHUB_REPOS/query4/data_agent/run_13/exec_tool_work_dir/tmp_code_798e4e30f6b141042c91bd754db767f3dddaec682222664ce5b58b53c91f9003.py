code = """import json
import re

# Load language data from file
lang_file_path = locals()['var_functions.query_db:6']
with open(lang_file_path, 'r') as f:
    languages_data = json.load(f)

# Load commit data
commits_data = locals()['var_functions.query_db:10']

# Parse languages to find main language and filter out Python repos
non_python_repos = []

for repo in languages_data:
    repo_name = repo['repo_name']
    lang_desc = repo['language_description']
    
    # Extract language names and their byte counts
    # Pattern matches: Language (bytes)
    lang_pattern = r'(\w+)\s*\((\d+)\s*bytes?\)'
    matches = re.findall(lang_pattern, lang_desc)
    
    if matches:
        # Find the language with max bytes (main language)
        main_lang = max(matches, key=lambda x: int(x[1]))[0]
        
        # Check if main language is NOT Python (case-insensitive)
        if main_lang.lower() != 'python':
            non_python_repos.append(repo_name)

# Now get commit counts for these non-Python repos
# Create a dict for faster lookup
commit_dict = {item['repo_name']: int(item['commit_count']) for item in commits_data}

# Filter and sort non-Python repos by commit count
filtered_commits = []
for repo in non_python_repos:
    if repo in commit_dict:
        filtered_commits.append({
            'repo_name': repo,
            'commit_count': commit_dict[repo]
        })

# Sort by commit count descending and get top 5
top_5_repos = sorted(filtered_commits, key=lambda x: x['commit_count'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5_repos, indent=2))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:10': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
