code = """import json
import re
import os

# Read the languages data from file
lang_file_key = "var_functions.query_db:16"
file_path = locals()[lang_file_key]

with open(file_path, 'r') as f:
    languages_data = json.load(f)

print(f"Total repositories in languages table: {len(languages_data)}")
print(f"\nFirst 5 entries:")
for i, entry in enumerate(languages_data[:5]):
    print(f"  {i+1}. {entry['repo_name']}")
    print(f"     Description: {entry['language_description'][:100]}...")

# Parse language descriptions to find main language
repos_with_main_lang = []

for entry in languages_data:
    lang_desc = entry['language_description']
    repo_name = entry['repo_name']
    
    # Extract language and byte count pairs
    # Look for patterns like: Language (bytes) or Language (bytes)
    lang_patterns = re.findall(r'(\w+)\s*\(([\d,]+)\s*bytes\)', lang_desc)
    
    if lang_patterns:
        # Convert to list of (language, bytes) tuples
        languages = []
        for lang, bytes_str in lang_patterns:
            try:
                bytes_clean = int(bytes_str.replace(',', ''))
                languages.append((lang, bytes_clean))
            except:
                continue
        
        if languages:
            # Find main language (one with most bytes)
            main_lang, max_bytes = max(languages, key=lambda x: x[1])
            
            repos_with_main_lang.append({
                'repo_name': repo_name,
                'main_language': main_lang,
                'main_language_bytes': max_bytes,
                'all_languages': languages,
                'original_desc': lang_desc
            })

print(f"\nSuccessfully parsed {len(repos_with_main_lang)} repositories")

# Filter out Python repositories
non_python_repos = [repo for repo in repos_with_main_lang 
                    if 'python' not in repo['main_language'].lower()]

print(f"Repositories where main language is NOT Python: {len(non_python_repos)}")

# Show some examples
print(f"\nExamples of non-Python repositories:")
for i, repo in enumerate(non_python_repos[:10]):
    print(f"  {repo['repo_name']}: {repo['main_language']} ({repo['main_language_bytes']:,} bytes)")

# Save the non-Python repo names for later use
non_python_repo_names = [repo['repo_name'] for repo in non_python_repos]

print(f"\nTotal non-Python repositories to check for commits: {len(non_python_repo_names)}")
print(f"Sample: {non_python_repo_names[:5]}")

# Also check if any of the top commit repos are in our non-Python list
commit_repos_key = "var_functions.query_db:18"
top_commit_repos = locals()[commit_repos_key]

print(f"\nTop commit repositories:")
for repo in top_commit_repos:
    is_non_python = repo['repo_name'] in non_python_repo_names
    print(f"  {repo['repo_name']}: {repo['commit_count']} commits - Non-Python: {is_non_python}")"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
