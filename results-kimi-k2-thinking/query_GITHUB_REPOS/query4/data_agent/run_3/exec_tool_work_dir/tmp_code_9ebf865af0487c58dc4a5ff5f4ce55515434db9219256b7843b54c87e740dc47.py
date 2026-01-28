code = """import json
import re

# Read languages data (full result stored in file)
languages_file = var_functions.query_db:10
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Read commits data (full result stored in file)
commits_file = var_functions.query_db:11
with open(commits_file, 'r') as f:
    commits_data = json.load(f)

# Parse main language from description
# Extract language with highest bytes
def get_main_language(lang_desc):
    if not lang_desc:
        return None
    
    # Pattern to match language and bytes
    # Looks for patterns like "Ruby (22,438 bytes)" or "Shell (21,286 bytes)"
    pattern = r'([A-Za-z\+\#]+)\s*\(([,\d]+)\s+bytes\)'
    matches = re.findall(pattern, lang_desc)
    
    if not matches:
        return None
    
    # Find language with max bytes
    max_bytes = 0
    main_lang = None
    
    for lang, bytes_str in matches:
        # Remove commas and convert to int
        try:
            bytes_val = int(bytes_str.replace(',', ''))
            if bytes_val > max_bytes:
                max_bytes = bytes_val
                main_lang = lang.strip()
        except:
            continue
    
    return main_lang

# Process languages to get main language per repo
repo_languages = {}
for row in languages_data:
    repo_name = row['repo_name']
    lang_desc = row['language_description']
    main_lang = get_main_language(lang_desc)
    if main_lang:
        repo_languages[repo_name] = main_lang

# Process commit counts
repo_commit_counts = {}
for row in commits_data:
    repo_name = row['repo_name']
    commit_count = int(row['commit_count'])
    repo_commit_counts[repo_name] = commit_count

# Join and filter out Python repos
top_repos = []
for repo_name, commit_count in repo_commit_counts.items():
    main_lang = repo_languages.get(repo_name)
    if main_lang and main_lang.lower() != 'python':
        top_repos.append({
            'repo_name': repo_name,
            'commit_count': commit_count,
            'main_language': main_lang
        })

# Sort by commit count descending
top_repos_sorted = sorted(top_repos, key=lambda x: x['commit_count'], reverse=True)

# Get top 5
top_5 = top_repos_sorted[:5]

# Extract just the repo names
result = [repo['repo_name'] for repo in top_5]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'facebook/react', 'commit_count': '178'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
