code = """import json
import os
import glob

# Find all result files
print('=== Looking for result files ===')
result_files = []
for pattern in ['/tmp/*.json', '/tmp/tmp_query_result_*', '*.json']:
    result_files.extend(glob.glob(pattern))

print('Found result files:', result_files)

# Try to read the non-Python repos file
non_python_path = '/tmp/tmp_query_result_66.json'
readme_path = '/tmp/tmp_query_result_54.json'

print('\n=== Reading non-Python data ===')
if os.path.exists(non_python_path):
    with open(non_python_path, 'r') as f:
        non_python_data = json.load(f)
    print('Loaded', len(non_python_data), 'non-Python repos')
else:
    print('File not found:', non_python_path)
    non_python_data = []

print('\n=== Reading README data ===')
if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        readme_data = json.load(f)
    print('Loaded', len(readme_data), 'README files')
else:
    print('File not found:', readme_path)
    readme_data = []

print('\n=== Processing data ===')
if non_python_data and readme_data:
    non_python_repos = set(item['repo_name'] for item in non_python_data)
    print('Non-Python repos:', len(non_python_repos))
    
    # Check copyright in READMEs
    copyright_indicators = ['copyright', '©', 'all rights reserved', 'licensed under', 'license']
    total = 0
    copyright_count = 0
    
    for readme in readme_data:
        if readme['sample_repo_name'] in non_python_repos:
            total += 1
            content = readme.get('content', '').lower()
            if any(indicator in content for indicator in copyright_indicators):
                copyright_count += 1
    
    proportion = copyright_count / total if total > 0 else 0
    
    print('__RESULT__:')
    print(json.dumps({
        'total_readmes': total,
        'copyright_readmes': copyright_count,
        'proportion': round(proportion, 4)
    }))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:50': {'temp_files': [], 'cwd': '/workspace'}, 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
