code = """import json
import re

# Get the data
non_python_file = locals()['var_functions.query_db:4']
readme_file = locals()['var_functions.query_db:14']

# Read the files
with open(non_python_file, 'r') as f:
    non_python_repos = [item['repo_name'] for item in json.load(f)]

with open(readme_file, 'r') as f:
    readme_data = json.load(f)

# Convert to set for faster lookup
non_python_set = set(non_python_repos)

# Filter READMEs that belong to non-Python repos
non_python_readmes = []
for item in readme_data:
    if item['sample_repo_name'] in non_python_set:
        non_python_readmes.append(item)

# Function to check for copyright
def has_copyright(content):
    if not content:
        return False
    return bool(re.search(r'copyright', content, re.IGNORECASE))

# Analyze
total_non_python_readmes = len(non_python_readmes)
copyright_count = sum(1 for item in non_python_readmes if has_copyright(item['content']))

print('__RESULT__:')
print(json.dumps({
    'total_non_python_readmes': total_non_python_readmes,
    'copyright_count': copyright_count,
    'sample_repos_with_copyright': [item['sample_repo_name'] for item in non_python_readmes if has_copyright(item['content'])][:5],
    'sample_repos_without_copyright': [item['sample_repo_name'] for item in non_python_readmes if not has_copyright(item['content'])][:5]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:6': {'count': 2774729, 'sample': [{'repo_name': 'juliandunn/rackspacecloud'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer'}, {'repo_name': 'michaellihs/gitlab'}, {'repo_name': 'vyorkin/xftp'}, {'repo_name': 'airatshigapov/drophunter'}]}, 'var_functions.list_db:8': ['commits', 'contents', 'files'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'non_python_repos_count': 2774729, 'readme_file_count': 128, 'sample_repos': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab'], 'sample_readmes': ['ninja-ide/ninja-ide', 'cwilso/midi-synth', 'ha/doozerd']}}

exec(code, env_args)
