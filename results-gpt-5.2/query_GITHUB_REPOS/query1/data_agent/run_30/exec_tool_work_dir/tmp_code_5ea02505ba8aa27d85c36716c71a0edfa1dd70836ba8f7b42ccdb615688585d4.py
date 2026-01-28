code = """import json, re

def load_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

langs = load_maybe(var_call_lHz2sNt0yHz1VpAcvz1m1jdj)
readmes = load_maybe(var_call_3rXLMLFki0Jv2acjWfhljhbV)

non_python_repos = set(r.get('repo_name') for r in langs if r.get('repo_name'))

readme_by_repo = {}
for r in readmes:
    rn = r.get('repo_name')
    if rn and rn not in readme_by_repo:
        readme_by_repo[rn] = r.get('content') or ''

repos_with_readme = non_python_repos.intersection(readme_by_repo.keys())

pat = re.compile(r"(?i)(?:copyright\s*(?:\(c\)|©)?\s*\d{0,4}(?:\s*[-–—]\s*\d{2,4})?\s*[^\n]{0,80})|(?:\b©\s*\d{2,4}\b)")

def has_copyright(text):
    return bool(text) and bool(pat.search(text))

num_total = len(repos_with_readme)
num_with = sum(1 for rn in repos_with_readme if has_copyright(readme_by_repo[rn]))
prop = (num_with / num_total) if num_total else None

out = {
    'non_python_repos_with_readme_md': num_total,
    'readme_md_with_copyright': num_with,
    'proportion': prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lHz2sNt0yHz1VpAcvz1m1jdj': 'file_storage/call_lHz2sNt0yHz1VpAcvz1m1jdj.json', 'var_call_3rXLMLFki0Jv2acjWfhljhbV': 'file_storage/call_3rXLMLFki0Jv2acjWfhljhbV.json'}

exec(code, env_args)
