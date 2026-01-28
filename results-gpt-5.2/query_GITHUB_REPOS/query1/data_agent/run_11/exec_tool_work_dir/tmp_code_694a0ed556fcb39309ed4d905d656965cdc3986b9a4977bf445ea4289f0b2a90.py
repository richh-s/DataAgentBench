code = """import json, re, pandas as pd

def load(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

non_py = load(var_call_blLbRqshgkBUHMOlGU4MSw1y)
readmes = load(var_call_VgoX0JEshyOlUupNKJMTbLZD)

non_py_set = set(r['repo_name'] for r in non_py)

# README.md entries might have multiple refs; collapse per repo (any README has copyright)
pat = re.compile(r'(?i)(copyright\s*(?:\(c\)|©)?\s*\d{0,4})|\b©\b')

repo_has = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo in non_py_set:
        content = r.get('content') or ''
        has = bool(pat.search(content))
        repo_has[repo] = repo_has.get(repo, False) or has

# denominator: non-python repos that have a README.md in contents
repos_with_readme = set(repo_has.keys())
num = sum(1 for v in repo_has.values() if v)
den = len(repo_has)
prop = (num/den) if den else None

out = {"non_python_repos_with_readme": den, "readmes_with_copyright": num, "proportion": prop}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_blLbRqshgkBUHMOlGU4MSw1y': 'file_storage/call_blLbRqshgkBUHMOlGU4MSw1y.json', 'var_call_VgoX0JEshyOlUupNKJMTbLZD': 'file_storage/call_VgoX0JEshyOlUupNKJMTbLZD.json'}

exec(code, env_args)
