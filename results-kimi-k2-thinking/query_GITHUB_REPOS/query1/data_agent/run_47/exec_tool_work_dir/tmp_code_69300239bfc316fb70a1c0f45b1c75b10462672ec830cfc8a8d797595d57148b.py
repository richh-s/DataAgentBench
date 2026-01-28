code = """import json
import re

# Get the file paths from the variables
non_python_file_path = var_functions.query_db:26
readme_file_path = var_functions.query_db:18

# Read the data from file paths
with open(non_python_file_path, 'r') as f:
    non_python_data = json.load(f)

with open(readme_file_path, 'r') as f:
    readme_data = json.load(f)

# Extract repo names for non-Python repositories
non_python_repo_names = {repo['repo_name'] for repo in non_python_data}

# Filter README files to only those from non-Python repositories
filtered_readmes = []
for readme in readme_data:
    if readme.get('sample_repo_name') in non_python_repo_names:
        filtered_readmes.append(readme)

# Check for copyright information in README content
copyright_pattern = re.compile(r'copyright|©', re.IGNORECASE)

total_readmes = len(filtered_readmes)
readmes_with_copyright = 0
for readme in filtered_readmes:
    content = readme.get('content')
    if content and content != 'None' and copyright_pattern.search(content):
        readmes_with_copyright += 1

# Calculate proportion
proportion = readmes_with_copyright / total_readmes if total_readmes > 0 else 0.0

result_string = f"Among {total_readmes:,} README files from non-Python repositories, {readmes_with_copyright:,} contain copyright information. This represents {proportion:.4f} or {proportion*100:.2f}%."

print('__RESULT__:')
print(result_string)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [{'total_non_python': '2774729'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
