code = """import json

# Try to access the variable - it might be a raw list or a file path
lang_data = locals()['var_functions.query_db:11']

# Load the languages data
if isinstance(lang_data, str):
    # It's a file path
    import os
    with open(lang_data, 'r') as f:
        languages_data = json.load(f)
else:
    # It's the actual data
    languages_data = lang_data

# Count total and categorize
python_count = 0
non_python_count = 0
non_python_repos = []

for item in languages_data:
    lang_desc = item['language_description'].lower()
    if 'python' in lang_desc:
        python_count += 1
    else:
        non_python_count += 1
        non_python_repos.append(item['repo_name'])

print('__RESULT__:')
print(json.dumps({
    'total': len(languages_data),
    'python_count': python_count,
    'non_python_count': non_python_count,
    'non_python_repos_sample': non_python_repos[:10]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['commits', 'contents', 'files'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
