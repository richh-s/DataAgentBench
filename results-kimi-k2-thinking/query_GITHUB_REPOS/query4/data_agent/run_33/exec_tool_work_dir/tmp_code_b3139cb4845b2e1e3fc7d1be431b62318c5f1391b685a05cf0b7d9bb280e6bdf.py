code = """import re
import json

print("LOADING languages data...")
# Load full languages data from the file
file_path = locals()['var_functions.query_db:6']
print(f"File path: {file_path}")

with open(file_path, 'r') as f:
    languages_data = json.load(f)

print(f"Total repos in languages data: {len(languages_data)}")

# Parse language descriptions to find main language
def extract_language_bytes(lang_desc):
    pattern = r'(\w+)\s*\((\d+(?:,\d+)*)\s+bytes?\)'
    matches = re.findall(pattern, lang_desc)
    
    lang_bytes = {}
    for lang, bytes_str in matches:
        bytes_count = int(bytes_str.replace(',', ''))
        lang_bytes[lang] = bytes_count
    
    return lang_bytes

def get_main_language(lang_desc):
    lang_bytes = extract_language_bytes(lang_desc)
    if not lang_bytes:
        return None
    
    main_lang = max(lang_bytes, key=lang_bytes.get)
    return main_lang

# Find non-Python repos
non_python_repos = []
for repo in languages_data:
    repo_name = repo['repo_name']
    lang_desc = repo['language_description']
    
    main_lang = get_main_language(lang_desc)
    if main_lang and main_lang.lower() != 'python':
        non_python_repos.append(repo_name)

print(f"Non-Python repos: {len(non_python_repos)}")

# Return the list
print("__RESULT__:")
print(json.dumps(non_python_repos))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
