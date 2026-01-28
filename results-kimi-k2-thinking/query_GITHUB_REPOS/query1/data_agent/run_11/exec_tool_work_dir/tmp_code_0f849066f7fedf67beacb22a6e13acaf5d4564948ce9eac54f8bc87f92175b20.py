code = """import json
import os

# Direct file paths
non_python_file = '/tmp/tmp_query_result_76.json'
readme_file = '/tmp/tmp_query_result_54.json'

# Check if files exist
print('File existence check:')
print('Non-Python file exists:', os.path.exists(non_python_file))
print('README file exists:', os.path.exists(readme_file))

# Load data if files exist
non_python_repos = []
readme_data = []

if os.path.exists(non_python_file):
    with open(non_python_file) as f:
        non_python_data = json.load(f)
        non_python_repos = [item['repo_name'] for item in non_python_data]

if os.path.exists(readme_file):
    with open(readme_file) as f:
        readme_data = json.load(f)

print('Total non-Python repos:', len(non_python_repos))
print('Total README entries:', len(readme_data))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:50': {'temp_files': [], 'cwd': '/workspace'}, 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json'}

exec(code, env_args)
