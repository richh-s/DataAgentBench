code = """import json, re
# paths provided by previous tool calls
repo_list_path = var_call_UI24fsF369fmJfz4ZSVt2bV3
contents_path = var_call_L0UHfOkLUcARd0hnjgOFew21

with open(repo_list_path, 'r') as f:
    non_python_repos = set(json.load(f))

with open(contents_path, 'r') as f:
    contents = json.load(f)

# Filter README.md files belonging to non-Python repos
readme_rows = [r for r in contents if r.get('sample_repo_name') in non_python_repos and r.get('sample_path') and r.get('sample_path').lower().endswith('readme.md')]

total = len(readme_rows)

# Define copyright detection
pattern = re.compile(r"copyright|\u00A9|all rights reserved", re.IGNORECASE)

count_with_copyright = 0
for r in readme_rows:
    content = r.get('content') or ''
    if pattern.search(content):
        count_with_copyright += 1

proportion = None
if total > 0:
    proportion = count_with_copyright / total

result = {
    'total_readme_files_in_non_python_repos': total,
    'readme_files_with_copyright': count_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_j9s5pMsMzshGe0Xi6qIK4nPa': 'file_storage/call_j9s5pMsMzshGe0Xi6qIK4nPa.json', 'var_call_UI24fsF369fmJfz4ZSVt2bV3': 'file_storage/call_UI24fsF369fmJfz4ZSVt2bV3.json', 'var_call_L0UHfOkLUcARd0hnjgOFew21': 'file_storage/call_L0UHfOkLUcARd0hnjgOFew21.json'}

exec(code, env_args)
