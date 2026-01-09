code = """import json, re

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

non_py = load_records(var_call_afzn0zjxSATs0ECFJdeWkFPn)
readmes = load_records(var_call_32dMjoxhG6EemYYMGfI7OL6C)

non_py_set = set(r['repo_name'] for r in non_py)

readme_by_repo = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo in non_py_set:
        readme_by_repo.setdefault(repo, []).append(r.get('content') or '')

pattern = re.compile(r'(?i)\bcopyright\b|\b\(c\)\b|\b©\b')

repos_with_readme = set(readme_by_repo.keys())
repos_with_copyright = set()
for repo, contents in readme_by_repo.items():
    text = "\n\n".join(contents)
    if pattern.search(text):
        repos_with_copyright.add(repo)

n_readme = len(repos_with_readme)
n_copy = len(repos_with_copyright)
prop = (n_copy / n_readme) if n_readme else None

out = {
    'non_python_repos_with_readme_md': n_readme,
    'repos_with_copyright_in_readme_md': n_copy,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_afzn0zjxSATs0ECFJdeWkFPn': 'file_storage/call_afzn0zjxSATs0ECFJdeWkFPn.json', 'var_call_32dMjoxhG6EemYYMGfI7OL6C': 'file_storage/call_32dMjoxhG6EemYYMGfI7OL6C.json'}

exec(code, env_args)
