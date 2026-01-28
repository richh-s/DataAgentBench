code = """import json
import re
from collections import defaultdict

# Load languages data
lang_var = locals()['var_functions.query_db:6']
if isinstance(lang_var, str):
    with open(lang_var, 'r') as f:
        languages_data = json.load(f)
else:
    languages_data = lang_var

# Load commits data
commits_var = locals()['var_functions.query_db:9']
if isinstance(commits_var, str):
    with open(commits_var, 'r') as f:
        commits_data = json.load(f)
else:
    commits_data = commits_var

print(f"Total language records: {len(languages_data)}")
print(f"Total commit records: {len(commits_data)}")

# Parse main language from language_description
def extract_main_language(lang_desc):
    """Extract the main language and its bytes from language_description"""
    if not lang_desc:
        return None, 0
    
    # Pattern to match language names and byte counts
    # Look for patterns like: Language (X bytes) or Language (X,XXX bytes)
    pattern = r'([A-Za-z\+#]+)\s*\((\d+(?:,\d+)*)\s*bytes\)'
    matches = re.findall(pattern, lang_desc)
    
    if not matches:
        return None, 0
    
    # Convert bytes to integers and find the language with max bytes
    max_bytes = 0
    main_lang = None
    
    for lang, bytes_str in matches:
        try:
            # Remove commas and convert to integer
            bytes_val = int(bytes_str.replace(',', ''))
            if bytes_val > max_bytes:
                max_bytes = bytes_val
                main_lang = lang
        except:
            continue
    
    return main_lang, max_bytes

# Create a mapping of repo to main language
repo_main_language = {}
for record in languages_data:
    repo_name = record['repo_name']
    lang_desc = record['language_description']
    main_lang, _ = extract_main_language(lang_desc)
    if main_lang:
        repo_main_language[repo_name] = main_lang

print(f"Successfully parsed main languages for {len(repo_main_language)} repositories")
print(f"Sample mapping: {list(repo_main_language.items())[:5]}")

# Count commits per repository
commit_counts = defaultdict(int)
for record in commits_data:
    repo_name = record['repo_name']
    commit_counts[repo_name] += 1

print(f"Total unique repositories with commits: {len(commit_counts)}")
print(f"Sample commit counts: {list(commit_counts.items())[:5]}")

# Filter repositories whose main language is NOT Python
non_python_repos = {}
for repo, language in repo_main_language.items():
    if language.lower() != 'python':
        # Get commit count if available
        if repo in commit_counts:
            non_python_repos[repo] = commit_counts[repo]

print(f"Non-Python repositories with commits: {len(non_python_repos)}")
print(f"Sample non-Python repos: {list(non_python_repos.items())[:5]}")

# Get top 5 repositories by commit count
top_5 = sorted(non_python_repos.items(), key=lambda x: x[1], reverse=True)[:5]
print(f"Top 5 non-Python repositories by commits: {top_5}")

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:4': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
