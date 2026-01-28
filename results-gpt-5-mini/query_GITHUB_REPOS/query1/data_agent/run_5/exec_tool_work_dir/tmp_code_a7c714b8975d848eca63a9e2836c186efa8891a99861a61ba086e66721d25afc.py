code = """import json
# Load non-Python repo list
path_repos = var_call_469uwtCdmJgIYohqYkrAXjJa
with open(path_repos, 'r') as f:
    non_python_repos = set(json.load(f))
# Load README contents
path_readmes = var_call_sWVSoRQSrqcWbCf8scUFHLpL
with open(path_readmes, 'r') as f:
    readmes = json.load(f)

import re
pattern = re.compile(r"copyright|\u00a9|\(c\)|©|all rights reserved", re.IGNORECASE)

# Filter readmes for non-python repos
filtered = [r for r in readmes if r.get('sample_repo_name') in non_python_repos]

total_readme_files = len(filtered)
count_with_copyright = 0
for r in filtered:
    content = r.get('content') or ''
    if pattern.search(content):
        count_with_copyright += 1

proportion = None
percentage = None
if total_readme_files > 0:
    proportion = count_with_copyright / total_readme_files
    percentage = proportion * 100

result = {
    'total_readme_files_in_non_python_repos': total_readme_files,
    'readme_files_with_copyright': count_with_copyright,
    'proportion': proportion,
    'percentage': percentage
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dzj0seDdcTOIX5c5FyXeUV5j': 'file_storage/call_dzj0seDdcTOIX5c5FyXeUV5j.json', 'var_call_469uwtCdmJgIYohqYkrAXjJa': 'file_storage/call_469uwtCdmJgIYohqYkrAXjJa.json', 'var_call_sWVSoRQSrqcWbCf8scUFHLpL': 'file_storage/call_sWVSoRQSrqcWbCf8scUFHLpL.json'}

exec(code, env_args)
