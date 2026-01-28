code = """import json
# Load repos_with_readme mapping from previous step
readme_file = 'var_functions.query_db:12'
non_python_file = 'var_functions.query_db:6'

# Load non-Python repos
if isinstance(locals()[non_python_file], str):
    with open(locals()[non_python_file], 'r') as f:
        non_python_repos = json.load(f)
else:
    non_python_repos = locals()[non_python_file]

non_python_set = set([r['repo_name'] for r in non_python_repos])

# Load README files
if isinstance(locals()[readme_file], str):
    with open(locals()[readme_file], 'r') as f:
        readme_files = json.load(f)
else:
    readme_files = locals()[readme_file]

# Filter to non-Python repos
filtered_readme_files = [f for f in readme_files if f['repo_name'] in non_python_set]

print(f"Total README files to check: {len(filtered_readme_files)}")

# Get unique repos
repos_with_paths = {}
for f in filtered_readme_files:
    if f['repo_name'] not in repos_with_paths:
        repos_with_paths[f['repo_name']] = []
    repos_with_paths[f['repo_name']].append(f['path'])

# Count how many files we have
file_count = sum(len(paths) for paths in repos_with_paths.values())
print(f"Total files: {file_count}")
print(f"Total unique repos: {len(repos_with_paths)}")

# Take a sample of files to query
sample_size = 100
sample_files = []
for repo_name, paths in list(repos_with_paths.items())[:sample_size]:
    sample_files.append({
        'repo_name': repo_name,
        'id': [f['id'] for f in filtered_readme_files if f['repo_name'] == repo_name][0],
        'path': paths[0] if paths else ''
    })

print(f"Sample files for query: {len(sample_files)}")
print('__RESULT__:')
print(json.dumps(sample_files[:5]))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['commits', 'contents', 'files'], 'var_functions.execute_python:10': 2774729, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'non_python_repos': 2774729, 'readme_files_total': 3086, 'readme_files_filtered': 2196, 'repos_with_readme': 1644, 'sample_repos': ['jgeboski/bitlbee-steam', 'nodesource/docker-node', 'iGEL/it', 'DaMSL/K3', 'IGS/OSDF']}}

exec(code, env_args)
