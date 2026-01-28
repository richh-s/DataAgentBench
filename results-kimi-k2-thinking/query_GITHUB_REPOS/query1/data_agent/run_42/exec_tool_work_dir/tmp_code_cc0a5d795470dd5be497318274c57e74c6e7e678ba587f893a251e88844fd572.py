code = """import json
import re

# Load the language data from the file
with open('/tmp/tmp5g9h8u4d/results.json', 'r') as f:
    language_data = json.load(f)

# Function to check if a repo uses Python based on language_description
def uses_python(lang_desc):
    if not lang_desc:
        return False
    # Look for Python in the description (case-insensitive)
    return 'python' in lang_desc.lower()

# Filter repos that do NOT use Python
non_python_repos = []
python_repos = []

for item in language_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    if uses_python(lang_desc):
        python_repos.append(repo_name)
    else:
        non_python_repos.append(repo_name)

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(language_data),
    'python_repos': len(python_repos),
    'non_python_repos': len(non_python_repos),
    'non_python_repos_list': non_python_repos[:10]  # Just a sample
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
