code = """import json
import os
import re

# Access the stored result using the correct variable name
result_key = "var_functions.query_db:6"
file_path = locals()[result_key]

print(f"File path: {file_path}")
print(f"File exists: {os.path.exists(file_path)}")

# Read and parse the JSON file
with open(file_path, 'r') as f:
    languages_data = json.load(f)

print(f"Total repositories loaded: {len(languages_data)}")
print("First 3 entries:")
for entry in languages_data[:3]:
    print(f"  - {entry}")

# Parse language descriptions to find main language and check if it's Python
repos_not_python = []
total_checked = 0

for entry in languages_data:
    total_checked += 1
    repo_name = entry['repo_name']
    lang_desc = entry['language_description']
    
    # Try to extract languages and their byte counts
    # Look for patterns like "Language (bytes), Language (bytes)"
    lang_patterns = re.findall(r'(\w+)\s*\(([\d,]+)\s*bytes\)', lang_desc)
    
    if lang_patterns:
        # Find the language with max bytes (main language)
        languages = [(lang, int(bytes_str.replace(',', ''))) for lang, bytes_str in lang_patterns]
        main_lang, max_bytes = max(languages, key=lambda x: x[1])
        
        # Check if it's not Python
        if 'python' not in main_lang.lower():
            repos_not_python.append({
                'repo_name': repo_name,
                'main_language': main_lang,
                'main_language_bytes': max_bytes,
                'all_languages': languages
            })

print(f"\nTotal checked: {total_checked}")
print(f"Repositories where main language is NOT Python: {len(repos_not_python)}")
print(f"Example non-Python repo: {repos_not_python[0] if repos_not_python else 'None'}")"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
