code = """import json
from pathlib import Path

# Load data from previous query results. These variables are provided by the environment.
# var_call_xS5xCF77YBJhp0uP1SDcMhM7 and var_call_hRwBi2MHnrQLLdVDer16Wi15

def load_var(v):
    # If v is a string path to a .json file, load it; otherwise assume it's already a list
    if isinstance(v, str) and Path(v).exists():
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

langs = load_var(var_call_xS5xCF77YBJhp0uP1SDcMhM7)
readmes = load_var(var_call_hRwBi2MHnrQLLdVDer16Wi15)

# Build set of non-Python repo names
non_python_repos = set()
for r in langs:
    if isinstance(r, dict) and 'repo_name' in r:
        non_python_repos.add(r['repo_name'])

# Build mapping of repo -> readme content (take first if multiple)
readme_map = {}
for item in readmes:
    if 'sample_repo_name' in item and 'content' in item:
        repo = item['sample_repo_name']
        if repo not in readme_map:
            readme_map[repo] = item['content']

# For repos that are non-python and have a README, check for copyright info
def has_copyright(text):
    if not text:
        return False
    tl = text.lower()
    if 'copyright' in tl:
        return True
    if '©' in text:
        return True
    if 'all rights reserved' in tl:
        return True
    return False

repos_with_readme = [r for r in non_python_repos if r in readme_map]
num_with_readme = len(repos_with_readme)
num_with_copyright = 0
for r in repos_with_readme:
    if has_copyright(readme_map[r]):
        num_with_copyright += 1

proportion = None
if num_with_readme > 0:
    proportion = num_with_copyright / num_with_readme

result = {
    'non_python_repos_with_readme': num_with_readme,
    'readmes_with_copyright': num_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xS5xCF77YBJhp0uP1SDcMhM7': 'file_storage/call_xS5xCF77YBJhp0uP1SDcMhM7.json', 'var_call_hRwBi2MHnrQLLdVDer16Wi15': 'file_storage/call_hRwBi2MHnrQLLdVDer16Wi15.json'}

exec(code, env_args)
