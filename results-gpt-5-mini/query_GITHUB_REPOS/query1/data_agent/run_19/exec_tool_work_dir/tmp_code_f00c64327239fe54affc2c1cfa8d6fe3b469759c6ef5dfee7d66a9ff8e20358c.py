code = """import json

# Load variables from storage
var1 = var_call_gqdpHN9XbCVI0gxsVbPI565V
var2 = var_call_E48YkfCdinTIxZ0Zqwf0GRQE

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

languages = load_var(var1)
contents = load_var(var2)

# Build set of repos that do NOT use Python
non_python_repos = set()
all_repos = set()
for rec in languages:
    repo = rec.get('repo_name')
    all_repos.add(repo)
    desc = rec.get('language_description') or ''
    if 'python' not in desc.lower():
        non_python_repos.add(repo)

# Filter contents to README.md files in non-python repos
readme_records = []
for rec in contents:
    repo = rec.get('sample_repo_name')
    path = rec.get('sample_path') or ''
    if not repo or not path:
        continue
    if repo not in non_python_repos:
        continue
    if path.lower().endswith('readme.md'):
        readme_records.append(rec)

num_readme_files = 0
num_with_copyright = 0

for rec in readme_records:
    content = rec.get('content')
    # Normalize content
    if content is None:
        continue
    if isinstance(content, str):
        if content.strip() == '' or content.strip().lower() == 'none':
            continue
    else:
        # non-string content, skip
        continue
    num_readme_files += 1
    lc = content.lower()
    if ('copyright' in lc) or ('©' in content) or ('all rights reserved' in lc) or ('(c)' in lc):
        num_with_copyright += 1

proportion = None
if num_readme_files > 0:
    proportion = num_with_copyright / num_readme_files

result = {
    'num_readme_files': num_readme_files,
    'num_with_copyright': num_with_copyright,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gqdpHN9XbCVI0gxsVbPI565V': 'file_storage/call_gqdpHN9XbCVI0gxsVbPI565V.json', 'var_call_E48YkfCdinTIxZ0Zqwf0GRQE': 'file_storage/call_E48YkfCdinTIxZ0Zqwf0GRQE.json'}

exec(code, env_args)
