code = """import json
import os
import re

# Load non-python repos
non_python_file = locals().get('var_functions.execute_python:5')
if isinstance(non_python_file, str):
    with open(non_python_file, 'r') as f:
        data = json.load(f)
else:
    data = non_python_file

non_python_repos = set(data['non_python_repos'])
print('Non-python repos count:', len(non_python_repos))

# Load README.md files
readme_file = locals().get('var_functions.query_db:10')
if isinstance(readme_file, str):
    print(f'Loading README file from {readme_file}...')
    with open(readme_file, 'r') as f:
        readme_data = json.load(f)
else:
    readme_data = readme_file

print('Total README.md entries:', len(readme_data))

# Filter README files for non-Python repos and check for copyright
readme_in_non_python = []
readme_with_copyright = []

for idx, entry in enumerate(readme_data):
    repo = entry.get('sample_repo_name')
    if repo in non_python_repos:
        readme_in_non_python.append(entry)
        content = entry.get('content', '')
        if content and 'copyright' in content.lower():
            readme_with_copyright.append(entry)

    if idx % 10000 == 0:
        print(f'Processed {idx} entries...')

print('README.md in non-Python repos:', len(readme_in_non_python))
print('README.md with copyright:', len(readme_with_copyright))

# Calculate proportion
if len(readme_in_non_python) > 0:
    proportion = len(readme_with_copyright) / len(readme_in_non_python)
    print('Proportion:', proportion)
else:
    proportion = 0
    print('No README.md files found in non-Python repos')

result = {
    'total_readme_in_non_python': len(readme_in_non_python),
    'readme_with_copyright': len(readme_with_copyright),
    'proportion': proportion
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': {'non_python_repos_count': 2774729}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
