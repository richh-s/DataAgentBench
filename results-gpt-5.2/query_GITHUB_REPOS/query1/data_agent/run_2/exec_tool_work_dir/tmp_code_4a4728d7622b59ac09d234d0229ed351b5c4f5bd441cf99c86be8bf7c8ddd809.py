code = """import json, pandas as pd, re

def load(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

repos_no_py = load(var_call_9bHDQPQOIlYSfePPu5DCQOxg)
readmes = load(var_call_NkEgIczC4sXSQYGbXCM2U66g)

no_py_set = set(r['repo_name'] for r in repos_no_py if r.get('repo_name') is not None)

# In case multiple README.md entries per repo, treat repo as having copyright if any README.md contains it.
# Heuristic: presence of word 'copyright' or '(c)' or '©'
pat = re.compile(r'(copyright|\(c\)|©)', re.IGNORECASE)

repo_has_readme = set()
repo_has_copyright = set()
for r in readmes:
    repo = r.get('repo_name')
    if repo in no_py_set:
        repo_has_readme.add(repo)
        content = r.get('content') or ''
        if pat.search(content):
            repo_has_copyright.add(repo)

num_readme = len(repo_has_readme)
num_c = len(repo_has_copyright)
prop = (num_c / num_readme) if num_readme else None

out = {
    'denominator_repos_no_python_with_readme_md': num_readme,
    'numerator_with_copyright_in_readme_md': num_c,
    'proportion': prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9bHDQPQOIlYSfePPu5DCQOxg': 'file_storage/call_9bHDQPQOIlYSfePPu5DCQOxg.json', 'var_call_NkEgIczC4sXSQYGbXCM2U66g': 'file_storage/call_NkEgIczC4sXSQYGbXCM2U66g.json'}

exec(code, env_args)
