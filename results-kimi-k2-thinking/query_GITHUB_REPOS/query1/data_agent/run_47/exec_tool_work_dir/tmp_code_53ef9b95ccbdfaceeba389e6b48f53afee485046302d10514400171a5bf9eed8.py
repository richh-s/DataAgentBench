code = """import json
import re

# Access the results from previous queries
non_python_repos = locals()['var_functions.query_db:4']
readme_files = locals()['var_functions.query_db:5']

# Extract repo names for non-Python repositories
non_python_repo_names = {repo['repo_name'] for repo in non_python_repos}

# Filter README files to only those from non-Python repositories
filtered_readmes = [
    readme for readme in readme_files 
    if readme['sample_repo_name'] in non_python_repo_names
]

# Check for copyright information in README content
copyright_pattern = re.compile(r'copyright|©|\(c\)|\(C\)', re.IGNORECASE)

total_readmes = len(filtered_readmes)
readmes_with_copyright = 0

for readme in filtered_readmes:
    content = readme.get('content', '')
    if content and content != 'None' and copyright_pattern.search(content):
        readmes_with_copyright += 1

# Calculate proportion
proportion = readmes_with_copyright / total_readmes if total_readmes > 0 else 0.0

result = {
    'total_readmes': total_readmes,
    'readmes_with_copyright': readmes_with_copyright,
    'proportion': proportion
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
