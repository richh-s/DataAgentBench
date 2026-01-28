code = """import json
import re
from collections import defaultdict

# Load the data with proper variable handling
lang_data_key = 'var_functions.query_db:6'
commits_data_key = 'var_functions.query_db:9'

# Get language data
lang_result = locals()[lang_data_key]
if isinstance(lang_result, str):
    with open(lang_result, 'r') as f:
        languages_data = json.load(f)
else:
    languages_data = lang_result

# Get commits data
commits_result = locals()[commits_data_key]
if isinstance(commits_result, str):
    with open(commits_result, 'r') as f:
        commits_data = json.load(f)
else:
    commits_data = commits_result

print("Data loaded successfully")
print(f"Language records: {len(languages_data)}")
print(f"Commit records: {len(commits_data)}")

# Function to extract main language from description
def get_main_language(description):
    if not description:
        return None
    
    pattern = r'([A-Za-z\+#]+)\s*\((\d+(?:,\d+)*)\s*bytes\)'
    matches = re.findall(pattern, description)
    
    if not matches:
        return None
    
    max_bytes = 0
    main_lang = None
    
    for lang, bytes_str in matches:
        try:
            bytes_val = int(bytes_str.replace(',', ''))
            if bytes_val > max_bytes:
                max_bytes = bytes_val
                main_lang = lang
        except:
            pass
    
    return main_lang

# Map repositories to their main languages
repo_languages = {}
for item in languages_data:
    repo = item['repo_name']
    desc = item['language_description']
    main_lang = get_main_language(desc)
    if main_lang:
        repo_languages[repo] = main_lang

print(f"Parsed languages for {len(repo_languages)} repositories")

# Count commits per repository
repo_commit_counts = defaultdict(int)
for item in commits_data:
    repo = item['repo_name']
    repo_commit_counts[repo] += 1

print(f"Commit counts for {len(repo_commit_counts)} repositories")

# Filter for non-Python repos and get their commit counts
non_python_results = []
for repo, lang in repo_languages.items():
    if lang.lower() != 'python' and repo in repo_commit_counts:
        commit_count = repo_commit_counts[repo]
        non_python_results.append((repo, commit_count))

# Sort by commit count descending and get top 5
top_5_repos = sorted(non_python_results, key=lambda x: x[1], reverse=True)[:5]

print(f"Top 5 non-Python repositories:")
for repo, count in top_5_repos:
    lang = repo_languages[repo]
    print(f"  {repo}: {count} commits (main language: {lang})")

# Return just the repository names
result = [repo for repo, count in top_5_repos]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:4': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
