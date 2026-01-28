code = """import json
import re

# Load the large results from the query_db calls. The variables are file paths.
with open(var_call_MGj68APUtYHAjwRFrfM9YSWZ, 'r') as f:
    no_python_list = json.load(f)
with open(var_call_nO0EJJ2a8qnIzeewdeZlFBol, 'r') as f:
    readmes = json.load(f)

# Extract set of repo names that do NOT use Python
no_python_repos = set()
for row in no_python_list:
    # rows contain {'repo_name': 'owner/repo'}
    no_python_repos.add(row.get('repo_name'))

# Filter README files that belong to these repos
filtered_readmes = [r for r in readmes if r.get('sample_repo_name') in no_python_repos]

total = len(filtered_readmes)

# Define regex for copyright indicators
pattern = re.compile(r'copyright|©|\(c\)|all rights reserved', re.IGNORECASE)

count_with_copyright = 0
for r in filtered_readmes:
    content = r.get('content') or ''
    if pattern.search(content):
        count_with_copyright += 1

proportion = (count_with_copyright / total) if total > 0 else None

result = {
    'total_readme_files_in_non_python_repos': total,
    'readme_files_with_copyright': count_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MGj68APUtYHAjwRFrfM9YSWZ': 'file_storage/call_MGj68APUtYHAjwRFrfM9YSWZ.json', 'var_call_nO0EJJ2a8qnIzeewdeZlFBol': 'file_storage/call_nO0EJJ2a8qnIzeewdeZlFBol.json'}

exec(code, env_args)
