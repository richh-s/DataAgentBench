code = """import json
import re

def load_var(v):
    # If storage entry is a file path (string), open and load JSON, otherwise return as-is
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

langs = load_var(var_call_XwiWtaeujt8eNsxk56O978EL)
contents = load_var(var_call_21oHu4PEQ7nnm96nlUGePz6D)

# Build set of repos that do NOT use Python
non_python_repos = set()
for item in langs:
    # item expected to have 'repo_name'
    repo = item.get('repo_name')
    if repo:
        non_python_repos.add(repo)

# Filter contents for README.md files in those repos
readmes = []
for c in contents:
    repo = c.get('sample_repo_name')
    path = c.get('sample_path') or ''
    if not repo or not path:
        continue
    if repo in non_python_repos and path.lower().endswith('readme.md'):
        readmes.append(c)

# Define pattern to detect copyright information
pattern = re.compile(r"copyright|\u00A9|all rights reserved", flags=re.IGNORECASE)

num_with_copyright = 0
for r in readmes:
    content = r.get('content')
    if content is None:
        text = ''
    else:
        text = str(content)
    if pattern.search(text):
        num_with_copyright += 1

total_readmes = len(readmes)
proportion = None
if total_readmes > 0:
    proportion = num_with_copyright / total_readmes

result = {
    'total_readme_files_from_non_python_repos': total_readmes,
    'readme_files_with_copyright': num_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_XwiWtaeujt8eNsxk56O978EL': 'file_storage/call_XwiWtaeujt8eNsxk56O978EL.json', 'var_call_21oHu4PEQ7nnm96nlUGePz6D': 'file_storage/call_21oHu4PEQ7nnm96nlUGePz6D.json'}

exec(code, env_args)
