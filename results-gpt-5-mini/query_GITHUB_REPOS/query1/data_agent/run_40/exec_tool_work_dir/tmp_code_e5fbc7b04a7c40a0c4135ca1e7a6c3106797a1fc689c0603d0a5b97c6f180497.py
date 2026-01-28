code = """import json, re

# Load the results from previous query_db calls (file paths provided in storage variables)
with open(var_call_TX46Z7Eyihgp1k5AtUbu16k1, 'r') as f:
    non_py_list = json.load(f)
with open(var_call_77BV8njpxHQ4464gRMk4SzS0, 'r') as f:
    contents_list = json.load(f)

non_py_repos = set(r['repo_name'] for r in non_py_list if r.get('repo_name'))

# Filter contents to README files from non-Python repos
readme_records = [r for r in contents_list if r.get('sample_repo_name') in non_py_repos]

# Map repo -> list of README contents
from collections import defaultdict
repo_readmes = defaultdict(list)
for r in readme_records:
    repo = r.get('sample_repo_name')
    content = r.get('content') or ''
    repo_readmes[repo].append(content)

# Define copyright detection
def has_copyright(text):
    if not text:
        return False
    if re.search(r'copyright', text, re.I):
        return True
    if '©' in text:
        return True
    if re.search(r'\(c\)', text, re.I):
        return True
    return False

total_repos_with_readme = len(repo_readmes)
num_with_copyright = 0
for repo, texts in repo_readmes.items():
    if any(has_copyright(t) for t in texts):
        num_with_copyright += 1

proportion = None
if total_repos_with_readme > 0:
    proportion = num_with_copyright / total_repos_with_readme

result = {
    'total_repos_with_readme': total_repos_with_readme,
    'num_with_copyright': num_with_copyright,
    'proportion': proportion
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TX46Z7Eyihgp1k5AtUbu16k1': 'file_storage/call_TX46Z7Eyihgp1k5AtUbu16k1.json', 'var_call_77BV8njpxHQ4464gRMk4SzS0': 'file_storage/call_77BV8njpxHQ4464gRMk4SzS0.json'}

exec(code, env_args)
