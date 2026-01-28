code = """import json, re
# Load query results from files
with open(var_call_uwfNOEV9M9HB0gOXVWiaQIl2, 'r') as f:
    languages = json.load(f)
with open(var_call_qcuh4Q9GpHXC6HS76kZb8rzg, 'r') as f:
    readmes = json.load(f)

# Build set of repos that do NOT use Python
non_python_repos = set()
for row in languages:
    rd = row.get('language_description') or ''
    if 'python' not in rd.lower():
        non_python_repos.add(row.get('repo_name'))

# Map each repo to a README content (take first occurrence)
readme_map = {}
for r in readmes:
    repo = r.get('sample_repo_name')
    if repo not in readme_map:
        readme_map[repo] = r.get('content') or ''

# Consider only non-python repos that have a README
repos_with_readme = sorted([r for r in non_python_repos if r in readme_map])

def has_copyright(text):
    if not text:
        return False
    return bool(re.search(r'copyright|\u00A9|\(c\)|all rights reserved', text, re.I))

num_with = 0
for repo in repos_with_readme:
    if has_copyright(readme_map[repo]):
        num_with += 1

den = len(repos_with_readme)
prop = None
if den > 0:
    prop = num_with / den

result = {'numerator': num_with, 'denominator': den, 'proportion': prop}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qcuh4Q9GpHXC6HS76kZb8rzg': 'file_storage/call_qcuh4Q9GpHXC6HS76kZb8rzg.json', 'var_call_uwfNOEV9M9HB0gOXVWiaQIl2': 'file_storage/call_uwfNOEV9M9HB0gOXVWiaQIl2.json'}

exec(code, env_args)
