code = """import json, os, sys

# Load languages result
p1 = var_call_fSaS8zbaEpqOWXfcbt1XvTSa
if isinstance(p1, str) and os.path.exists(p1):
    with open(p1, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = p1

# Load contents result
p2 = var_call_ahOwDU07Kbjtl7ByGpql8HX5
if isinstance(p2, str) and os.path.exists(p2):
    with open(p2, 'r', encoding='utf-8') as f:
        contents = json.load(f)
else:
    contents = p2

# Build set of repos that do NOT mention Python in language_description
non_python_repos = set()
for r in langs:
    desc = r.get('language_description') or ''
    if 'python' not in desc.lower():
        non_python_repos.add(r.get('repo_name'))

# Filter contents to README files belonging to non-python repos
readme_records = []
for rec in contents:
    repo = rec.get('sample_repo_name')
    path = (rec.get('sample_path') or '').lower()
    if repo in non_python_repos and 'readme' in path:
        readme_records.append(rec)

# Function to detect copyright
import re
pattern = re.compile(r'(copyright|\u00A9|\(c\)|all rights reserved)', re.IGNORECASE)

count_total = 0
count_with = 0
for r in readme_records:
    content = r.get('content') or ''
    count_total += 1
    if pattern.search(content):
        count_with += 1

proportion = None
if count_total > 0:
    proportion = count_with / count_total

result = {'total_readme_files_in_non_python_repos': count_total,
          'readme_files_with_copyright': count_with,
          'proportion': proportion}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_fSaS8zbaEpqOWXfcbt1XvTSa': 'file_storage/call_fSaS8zbaEpqOWXfcbt1XvTSa.json', 'var_call_ahOwDU07Kbjtl7ByGpql8HX5': 'file_storage/call_ahOwDU07Kbjtl7ByGpql8HX5.json'}

exec(code, env_args)
