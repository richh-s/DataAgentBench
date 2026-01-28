code = """import json
import re

# Read languages data from file
languages_file = locals()['var_functions.query_db:2']
if isinstance(languages_file, str) and languages_file.endswith('.json'):
    with open(languages_file, 'r') as f:
        languages_data = json.load(f)
else:
    languages_data = locals()['var_functions.query_db:2']

# Parse language descriptions to find main language per repo
non_python_repos = []
for entry in languages_data:
    repo_name = entry['repo_name']
    lang_desc = entry['language_description']
    
    # Extract languages and their byte sizes using regex
    # pattern to match language name and bytes
    pattern = r'(\w+)\s*\((\d+)\s+bytes\)'
    matches = re.findall(pattern, lang_desc)
    
    if matches:
        # Find language with max bytes (main language)
        max_bytes = 0
        main_lang = None
        for lang, bytes_str in matches:
            bytes_count = int(bytes_str)
            if bytes_count > max_bytes:
                max_bytes = bytes_count
                main_lang = lang
        
        # Check if main language is not Python
        if main_lang and main_lang.lower() != 'python':
            non_python_repos.append(repo_name)

# Get commit counts for these repos from artifacts_database commits table
print('__RESULT__:')
print(json.dumps(non_python_repos))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['commits', 'contents', 'files']}

exec(code, env_args)
