code = """import json

# Load the readme data from the file
with open(locals()['var_functions.query_db:22'], 'r') as f:
    readme_data = json.load(f)

# Load the list of readme repos from the other query
with open(locals()['var_functions.query_db:18'], 'r') as f:
    readme_repos_list = json.load(f)

# Create a set of all repositories that have README files
readme_repos = set([r['sample_repo_name'] for r in readme_repos_list])

# Load a sample of non-Python repositories
with open(locals()['var_functions.query_db:20'], 'r') as f:
    non_python_repos_data = json.load(f)

# Create a set of non-Python repositories
non_python_repos = set([r['repo_name'] for r in non_python_repos_data])

# Debug: Find some common repositories
common_repos = readme_repos.intersection(non_python_repos)
readme_examples = [r['sample_repo_name'] for r in readme_data[:10]]
non_python_examples = list(non_python_repos)[:10]

result = {
    'total_readme_repos': len(readme_repos),
    'total_non_python_repos': len(non_python_repos),
    'common_repos_count': len(common_repos),
    'sample_common_repos': list(common_repos)[:10],
    'sample_readme_repos': readme_examples,
    'sample_non_python_repos': non_python_examples
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_repos': 3325634, 'non_python_repos': 2774729, 'sample_non_python': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.execute_python:14': {'total_readmes_checked': 0, 'readmes_with_copyright': 0, 'sample_copyright_repos': []}, 'var_functions.execute_python:16': {'total_readmes_sampled': 100, 'readmes_with_content': 97, 'readmes_with_copyright': 7, 'copyright_percent': 7.216494845360824, 'sample_copyright_repos': ['selenith/plasmide', 'apache/stratos', 'id-Software/Quake-III-Arena', 'espadrine/opera', 'svn2github/chromium-depot-tools', 'mluisbrown/Memories', 'F1ReKing/wheelview']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_non_python_readmes': 0, 'readmes_with_copyright': 0, 'readmes_without_copyright': 0, 'proportion': 0, 'percentage': 0, 'sample_repos_with_copyright': []}}

exec(code, env_args)
