code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

non_py = load_records(var_call_afzn0zjxSATs0ECFJdeWkFPn)
readmes = load_records(var_call_32dMjoxhG6EemYYMGfI7OL6C)

non_py_set = set(r['repo_name'] for r in non_py)

# if multiple readmes per repo, consider repo has readme if any record exists
readme_by_repo = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo is None:
        continue
    if repo not in non_py_set:
        continue
    c = r.get('content') or ''
    readme_by_repo.setdefault(repo, []).append(c)

# copyright detection
pattern = re.compile(r"(?i)\bcopyright\b|\b\(c\)\b|\b©\b")

repos_with_readme = set(readme_by_repo.keys())
repos_with_copyright = set()
for repo, contents in readme_by_repo.items():
    joined = "\n\n".join(contents)
    if pattern.search(joined):
        repos_with_copyright.add(repo)

n_readme = len(repos_with_readme)
n_copy = len(repos_with_copyright)
prop = (n_copy / n_readme) if n_readme else None

out = {
    "non_python_repos_with_readme_md": n_readme,
    "repos_with_copyright_in_readme_md": n_copy,
    "proportion": prop
}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_afzn0zjxSATs0ECFJdeWkFPn': 'file_storage/call_afzn0zjxSATs0ECFJdeWkFPn.json', 'var_call_32dMjoxhG6EemYYMGfI7OL6C': 'file_storage/call_32dMjoxhG6EemYYMGfI7OL6C.json'}

exec(code, env_args)
