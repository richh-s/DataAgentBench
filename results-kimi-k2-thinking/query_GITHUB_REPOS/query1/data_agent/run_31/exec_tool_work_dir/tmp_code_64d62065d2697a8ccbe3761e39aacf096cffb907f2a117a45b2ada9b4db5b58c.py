code = """import json, os, re
from collections import defaultdict

# Paths to result files
non_python_file = 'var_functions.query_db:6'
readme_files_file = 'var_functions.query_db:12'

# Load non-Python repos
if isinstance(locals()[non_python_file], str):
    with open(locals()[non_python_file], 'r') as f:
        non_python_repos = json.load(f)
else:
    non_python_repos = locals()[non_python_file]

non_python_set = set([r['repo_name'] for r in non_python_repos])
print(f"Total non-Python repos: {len(non_python_set)}")

# Load README files
if isinstance(locals()[readme_files_file], str):
    with open(locals()[readme_files_file], 'r') as f:
        readme_files = json.load(f)
else:
    readme_files = locals()[readme_files_file]

print(f"Total README.md files found: {len(readme_files)}")
print(f"Sample: {readme_files[:3]}")

# Now filter README files to only those in non-Python repos
filtered_readme_files = [f for f in readme_files if f['repo_name'] in non_python_set]
print(f"README.md files in non-Python repos: {len(filtered_readme_files)}")

# Group by repo_name to get unique repos with README.md
repos_with_readme = defaultdict(list)
for f in filtered_readme_files:
    repos_with_readme[f['repo_name']].append(f)

print(f"Unique non-Python repos with README.md: {len(repos_with_readme)}")

# Sample a few repos for debugging
sample_repos = list(repos_with_readme.keys())[:5]
for repo in sample_repos:
    print(f"Repo {repo} has {len(repos_with_readme[repo])} README files")
    for f in repos_with_readme[repo][:2]:
        print(f"  - {f['path']}")

print('__RESULT__:')
print(json.dumps({
    'non_python_repos': len(non_python_set),
    'readme_files_total': len(readme_files),
    'readme_files_filtered': len(filtered_readme_files),
    'repos_with_readme': len(repos_with_readme),
    'sample_repos': sample_repos
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['commits', 'contents', 'files'], 'var_functions.execute_python:10': 2774729, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
