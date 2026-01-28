code = """import json
import re

# Get the file paths
non_python_file_path = globals()['var_functions.query_db:26']
readme_file_path = globals()['var_functions.query_db:18']

# Read the data
with open(non_python_file_path, 'r') as f1:
    non_python_repos = json.load(f1)

with open(readme_file_path, 'r') as f2:
    readme_files = json.load(f2)

# Extract non-Python repo names
non_python_repo_names = set()
for repo in non_python_repos:
    if isinstance(repo, dict) and 'repo_name' in repo:
        non_python_repo_names.add(repo['repo_name'])

# Filter README files
filtered_readmes = []
for readme in readme_files:
    if isinstance(readme, dict) and readme.get('sample_repo_name') in non_python_repo_names:
        filtered_readmes.append(readme)

# Count copyright mentions
copyright_pattern = re.compile(r'copyright|©|\(c\)', re.I)
total = len(filtered_readmes)
with_copyright = sum(1 for r in filtered_readmes 
                     if r.get('content') and r.get('content') != 'None' 
                     and copyright_pattern.search(r.get('content', '')))

proportion = with_copyright / total if total > 0 else 0

# Prepare JSON-serializable result
result_dict = {
    'total_readmes': total,
    'readmes_with_copyright': with_copyright,
    'proportion': proportion,
    'percentage': proportion * 100
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [{'total_non_python': '2774729'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
