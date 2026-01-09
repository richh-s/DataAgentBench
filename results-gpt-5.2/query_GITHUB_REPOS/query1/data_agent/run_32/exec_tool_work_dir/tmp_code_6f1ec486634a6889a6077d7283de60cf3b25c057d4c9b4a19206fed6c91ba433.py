code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

non_py = load_records(var_call_0HSAJHJ1lj5O2cQaI7julSpi)
readmes = load_records(var_call_riQqSTCzK9TlXJwBFa52KYbe)

non_py_set = set(r['repo_name'] for r in non_py)

# Only consider repos that (a) do not use Python and (b) have a README.md content record
readme_by_repo = {}
for r in readmes:
    repo = r.get('repo_name')
    if repo in non_py_set and repo not in readme_by_repo:
        readme_by_repo[repo] = r.get('content') or ''

repos_with_readme = list(readme_by_repo.keys())

# Heuristic: look for common copyright markers
pat = re.compile(r'(copyright\s*\(c\)|copyright\s*©|\bcopyright\b|©\s*\d{4}|\(c\)\s*\d{4})', re.IGNORECASE)
with_copyright = [repo for repo, txt in readme_by_repo.items() if pat.search(txt or '')]

total = len(repos_with_readme)
count = len(with_copyright)
prop = (count / total) if total else None

out = {
    'non_python_repos_with_readme_md': total,
    'readme_md_with_copyright_count': count,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0HSAJHJ1lj5O2cQaI7julSpi': 'file_storage/call_0HSAJHJ1lj5O2cQaI7julSpi.json', 'var_call_riQqSTCzK9TlXJwBFa52KYbe': 'file_storage/call_riQqSTCzK9TlXJwBFa52KYbe.json'}

exec(code, env_args)
