code = """import json
import re

# Read the full language data from file
languages_file_path = locals()['var_functions.query_db:8']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

# Load commit data (should be small enough to be in memory)
commits_data = locals()['var_functions.query_db:2']

print(f"Total language records: {len(languages_data)}")
print(f"Total commit records: {len(commits_data)}")

# Parse language descriptions to find main language for each repo
repo_main_language = {}

for row in languages_data:
    repo_name = row['repo_name']
    lang_desc = row['language_description']
    
    # Extract language-byte pairs using regex
    # Looks for patterns like: "Language (bytes)"
    lang_bytes = re.findall(r'([A-Za-z\+#]+)\s*\(([\d,]+)\s*bytes\)', lang_desc)
    
    if not lang_bytes:
        continue
    
    # Convert bytes to integers and find the main language (highest bytes)
    max_bytes = 0
    main_lang = None
    
    for lang, bytes_str in lang_bytes:
        try:
            bytes_val = int(bytes_str.replace(',', ''))
            if bytes_val > max_bytes:
                max_bytes = bytes_val
                main_lang = lang
        except:
            continue
    
    if main_lang:
        repo_main_language[repo_name] = main_lang

# Filter repos where main language is NOT Python
non_python_repos = {repo: lang for repo, lang in repo_main_language.items() if lang.lower() != 'python'}

# Create a map of repo to commit count
repo_commit_count = {row['repo_name']: int(row['commit_count']) for row in commits_data}

# Find intersection of repos that have both language and commit data
common_repos = set(non_python_repos.keys()) & set(repo_commit_count.keys())

print(f"Repos with language data: {len(repo_main_language)}")
print(f"Non-Python repos: {len(non_python_repos)}")
print(f"Repos with commit data: {len(repo_commit_count)}")
print(f"Common repos (have both): {len(common_repos)}")

# Create list of repos with commit counts
repos_with_commits = []
for repo in common_repos:
    repos_with_commits.append({
        'repo_name': repo,
        'commit_count': repo_commit_count[repo],
        'main_language': non_python_repos[repo]
    })

# Sort by commit count descending
top_repos = sorted(repos_with_commits, key=lambda x: x['commit_count'], reverse=True)

# Take top 5
if len(top_repos) >= 5:
    top_5_repos = top_repos[:5]
    print("Top 5 repositories by commits (non-Python):")
    for repo in top_5_repos:
        print(f"  {repo['repo_name']}: {repo['commit_count']} commits (main lang: {repo['main_language']})")
else:
    print(f"Only found {len(top_repos)} repos:")
    for repo in top_repos:
        print(f"  {repo['repo_name']}: {repo['commit_count']} commits (main lang: {repo['main_language']})")

# Extract just the repository names
result = [repo['repo_name'] for repo in top_repos[:5]]

# Print result in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
