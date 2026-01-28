code = """import json, os, re
from collections import defaultdict

# Load data
readme_file = 'var_functions.query_db:18'
non_python_file = 'var_functions.query_db:6'

# Load non-Python repos
if isinstance(locals()[non_python_file], str):
    with open(locals()[non_python_file], 'r') as f:
        non_python_repos = json.load(f)
else:
    non_python_repos = locals()[non_python_file]

non_python_set = set([r['repo_name'] for r in non_python_repos])
print(f"Total non-Python repos: {len(non_python_set)}")

# Load README files
if isinstance(locals()[readme_file], str):
    with open(locals()[readme_file], 'r') as f:
        readme_files = json.load(f)
else:
    readme_files = locals()[readme_file]

print(f"Total README files: {len(readme_files)}")

# Filter to non-Python repos only
filtered_readmes = []
for f in readme_files:
    if f['repo_name'] in non_python_set:
        filtered_readmes.append(f)

print(f"README files in non-Python repos: {len(filtered_readmes)}")
print(f"Sample: {filtered_readmes[:3]}")

# Get unique repos and their README ids
repos_to_check = {}
for f in filtered_readmes:
    repo = f['repo_name']
    if repo not in repos_to_check:
        repos_to_check[repo] = []
    repos_to_check[repo].append(f['id'])

print(f"Unique non-Python repos with top-level README: {len(repos_to_check)}")

# Prepare for content querying - sample for now
sample_size = 100
sample_items = list(repos_to_check.items())[:sample_size]
ids_to_query = []
for repo, id_list in sample_items:
    # Just take the first id for each repo
    if id_list:
        ids_to_query.append(id_list[0])

print(f"IDs to query for content: {len(ids_to_query)}")
print('__RESULT__:')
print(json.dumps({
    'total_repos': len(repos_to_check),
    'sample_size': len(sample_items),
    'ids_to_query_count': len(ids_to_query),
    'sample_ids': ids_to_query[:5]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['commits', 'contents', 'files'], 'var_functions.execute_python:10': 2774729, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'non_python_repos': 2774729, 'readme_files_total': 3086, 'readme_files_filtered': 2196, 'repos_with_readme': 1644, 'sample_repos': ['jgeboski/bitlbee-steam', 'nodesource/docker-node', 'iGEL/it', 'DaMSL/K3', 'IGS/OSDF']}, 'var_functions.execute_python:16': [{'repo_name': 'jgeboski/bitlbee-steam', 'id': '100b93820ade4c16225673b4ca62bb3ade63c313', 'path': 'README.md'}, {'repo_name': 'nodesource/docker-node', 'id': 'ff5c79602cf4f4964d15b6230c551f9d260ab007', 'path': 'centos/7/node/0.10.44/README.md'}, {'repo_name': 'iGEL/it', 'id': '9ed04c6e74db0e3606e716e64e1d7190d5027b15', 'path': 'README.md'}, {'repo_name': 'DaMSL/K3', 'id': '10f4a323a73e5da0d396326e68a7f4afb17a2356', 'path': 'tools/scripts/docker/README.md'}, {'repo_name': 'IGS/OSDF', 'id': '09bb97995c1ce09607e64ed72f9b1089e86c741f', 'path': 'node_modules/express/node_modules/depd/Readme.md'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
