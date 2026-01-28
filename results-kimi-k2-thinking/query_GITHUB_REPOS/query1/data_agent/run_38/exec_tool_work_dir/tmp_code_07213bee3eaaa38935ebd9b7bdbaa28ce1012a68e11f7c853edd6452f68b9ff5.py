code = """import json
import os

# Get the path of the languages result file
languages_path = var_functions.query_db:8

print('Languages path:', languages_path)

# Load the JSON data
with open(languages_path, 'r') as f:
    languages = json.load(f)

print('Number of language rows:', len(languages))
print('First few rows:', languages[:3])

# Identify repos that do NOT use Python
non_python_repos = []
for row in languages:
    desc = row.get('language_description', '')
    # Check if description contains 'Python' case-insensitive
    if 'python' not in desc.lower():
        non_python_repos.append(row['repo_name'])

print('Number of non-Python repos:', len(non_python_repos))
print('Sample non-Python repos:', non_python_repos[:10])"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.execute_python:5': ['languages', 'repos', 'licenses'], 'var_functions.query_db:9': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['commits', 'contents', 'files']}

exec(code, env_args)
