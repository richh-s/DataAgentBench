code = """import json, os, re

# Load the stored query results. The variables var_call_iIVmjynGg3rKQJiiTciDfRz2 and var_call_qkNCzXWFNpec4aBln0ov95kX are provided in the execution environment.

def load_var(v):
    # If v is a string path to a json file, open and load it. If it's already a list, return it.
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

records_non_python = load_var(var_call_iIVmjynGg3rKQJiiTciDfRz2)
records_readmes = load_var(var_call_qkNCzXWFNpec4aBln0ov95kX)

# Build set of non-python repo names
non_python_repos = set()
for r in records_non_python:
    # r expected to be dict with repo_name
    name = r.get('repo_name')
    if name:
        non_python_repos.add(name)

# Filter README.md files (case-insensitive basename == 'readme.md') and belonging to non-python repos
readme_records = []
for r in records_readmes:
    repo = r.get('sample_repo_name')
    path = r.get('sample_path')
    if not repo or not path:
        continue
    basename = os.path.basename(path).lower()
    if basename == 'readme.md' and repo in non_python_repos:
        readme_records.append(r)

# Define detection regex for copyright-like phrases
pat = re.compile(r"copyright|\u00A9|all rights reserved|copyright \(c\)", re.IGNORECASE)

total = len(readme_records)
with_copyright = 0
for r in readme_records:
    content = r.get('content')
    if content is None:
        continue
    if isinstance(content, str):
        # Some contents may be the literal string 'None'
        if content.strip().lower() == 'none' or content.strip() == '':
            continue
        if pat.search(content):
            with_copyright += 1

proportion = None
if total > 0:
    proportion = with_copyright / total

result = {
    'total_readme_md_in_non_python_repos': total,
    'readme_md_with_copyright': with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_iIVmjynGg3rKQJiiTciDfRz2': 'file_storage/call_iIVmjynGg3rKQJiiTciDfRz2.json', 'var_call_qkNCzXWFNpec4aBln0ov95kX': 'file_storage/call_qkNCzXWFNpec4aBln0ov95kX.json'}

exec(code, env_args)
