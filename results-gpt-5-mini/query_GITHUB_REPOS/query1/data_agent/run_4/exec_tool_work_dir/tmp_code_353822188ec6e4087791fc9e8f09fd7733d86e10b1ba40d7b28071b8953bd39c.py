code = """import json

# Load previous query results from storage file paths
with open(var_call_IWh4iqbwhC9ToPgDylXGJk1w, 'r', encoding='utf-8') as f:
    non_python_list = json.load(f)
with open(var_call_6mlWhk6rQySwr44uYcM69hYB, 'r', encoding='utf-8') as f:
    contents_list = json.load(f)

non_python_repos = set(r['repo_name'] for r in non_python_list)

total_readme_files = 0
matching_files = 0

for rec in contents_list:
    repo = rec.get('sample_repo_name')
    path = rec.get('sample_path') or ''
    if not repo or not path:
        continue
    if repo not in non_python_repos:
        continue
    path_l = path.lower()
    # consider README.md files only
    if not path_l.endswith('readme.md'):
        continue
    total_readme_files += 1
    content = rec.get('content')
    if content is None:
        continue
    # Some records may have the string "None"
    if isinstance(content, str) and content.strip().lower() == 'none':
        continue
    c = ''
    try:
        c = str(content)
    except Exception:
        c = ''
    cl = c.lower()
    if ('copyright' in cl) or ('©' in c) or ('(c)' in cl):
        matching_files += 1

proportion = None
if total_readme_files > 0:
    proportion = matching_files / total_readme_files

result = {
    'total_readme_files_in_non_python_repos': total_readme_files,
    'readme_files_with_copyright': matching_files,
    'proportion': proportion
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IWh4iqbwhC9ToPgDylXGJk1w': 'file_storage/call_IWh4iqbwhC9ToPgDylXGJk1w.json', 'var_call_6mlWhk6rQySwr44uYcM69hYB': 'file_storage/call_6mlWhk6rQySwr44uYcM69hYB.json'}

exec(code, env_args)
