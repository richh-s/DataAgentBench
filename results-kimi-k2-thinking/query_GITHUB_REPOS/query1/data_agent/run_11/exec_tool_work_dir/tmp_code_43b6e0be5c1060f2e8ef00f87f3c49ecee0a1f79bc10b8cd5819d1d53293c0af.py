code = """import json
import os

# Read the non-Python repos data
non_python_file = var_functions.query_db_52
with open(non_python_file, 'r') as f:
    non_python_data = json.load(f)

# Read the README contents data  
readme_file = var_functions.query_db_54
with open(readme_file, 'r') as f:
    readme_data = json.load(f)

non_python_repos = [item['repo_name'] for item in non_python_data]

# Count copyright information in READMEs of non-Python repos
copyright_indicators = ['copyright', '©', 'all rights reserved', 'licensed under']
total_readmes = 0
copyright_readmes = 0

for readme_item in readme_data:
    repo_name = readme_item['sample_repo_name']
    content = readme_item.get('content', '') or ''
    
    if repo_name in non_python_repos:
        total_readmes += 1
        content_lower = content.lower()
        has_copyright = any(indicator in content_lower for indicator in copyright_indicators)
        if has_copyright:
            copyright_readmes += 1

proportion = copyright_readmes / total_readmes if total_readmes > 0 else 0

print('__RESULT__:')
print(json.dumps({
    'total_readmes_analyzed': total_readmes,
    'copyright_readmes_found': copyright_readmes,
    'proportion': round(proportion, 4)
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:50': {'temp_files': [], 'cwd': '/workspace'}, 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
