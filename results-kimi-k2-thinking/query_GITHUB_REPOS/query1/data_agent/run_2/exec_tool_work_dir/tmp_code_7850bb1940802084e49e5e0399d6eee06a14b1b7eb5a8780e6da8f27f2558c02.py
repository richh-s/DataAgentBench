code = """import json
import re

# Load non-Python repositories
with open(locals()['var_functions.query_db:0'], 'r') as f:
    non_python_repos = json.load(f)

# Load README.md files
with open(locals()['var_functions.query_db:10'], 'r') as f:
    readme_files = json.load(f)

# Create a set of non-Python repository names for fast lookup
non_python_repo_names = set(repo['repo_name'] for repo in non_python_repos)

# Filter README.md files to only those in non-Python repositories
non_python_readmes = [
    readme for readme in readme_files 
    if readme['sample_repo_name'] in non_python_repo_names
]

# Count total and copyright-containing files
total_readmes = len(non_python_readmes)
copyright_pattern = re.compile(r'copyright', re.IGNORECASE)
readmes_with_copyright = 0

for readme in non_python_readmes:
    if readme.get('content') and copyright_pattern.search(readme['content']):
        readmes_with_copyright += 1

# Calculate proportion
proportion = readmes_with_copyright / total_readmes if total_readmes > 0 else 0

print('__RESULT__:')
print(json.dumps({
    'total_readmes': total_readmes,
    'readmes_with_copyright': readmes_with_copyright,
    'proportion': proportion
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': 2774729, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
