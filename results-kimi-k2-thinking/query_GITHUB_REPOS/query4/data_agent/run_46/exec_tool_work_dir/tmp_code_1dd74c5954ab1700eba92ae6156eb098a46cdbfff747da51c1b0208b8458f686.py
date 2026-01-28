code = """import json
import re
import os

# Read the languages data from file
lang_file_key = "var_functions.query_db:16"
file_path = locals()[lang_file_key]

with open(file_path, 'r') as f:
    languages_data = json.load(f)

print("Total repositories in languages table: %d" % len(languages_data))

# Parse language descriptions to find main language
repos_with_main_lang = []

for entry in languages_data:
    lang_desc = entry['language_description']
    repo_name = entry['repo_name']
    
    # Extract language and byte count pairs
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
                'all_languages': languages
            })

print("Successfully parsed %d repositories" % len(repos_with_main_lang))

# Filter out Python repositories
non_python_repos = []
for repo in repos_with_main_lang:
    if 'python' not in repo['main_language'].lower():
        non_python_repos.append(repo)

print("Repositories where main language is NOT Python: %d" % len(non_python_repos))

# Save results to a variable for use
print("__RESULT__:")
print(json.dumps({
    'non_python_repos': non_python_repos,
    'total_parsed': len(repos_with_main_lang),
    'total_non_python': len(non_python_repos)
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
