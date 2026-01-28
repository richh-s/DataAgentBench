code = """import json, re
import pandas as pd

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

non_py = load_var(var_call_6sSyisU7zLUXsz5xLuHaecu5)
readmes = load_var(var_call_OugEpRWZhyMbAvsZ17v2kgP3)

non_py_set = set(r['repo_name'] for r in non_py)

# detect copyright info in README
pat = re.compile(r"(?is)(?:\bcopyright\b|\(c\)|©|all\s+rights\s+reserved)")

eligible = 0
with_copyright = 0

for r in readmes:
    repo = r.get('repo_name')
    if repo in non_py_set:
        eligible += 1
        content = r.get('content') or ''
        if pat.search(content):
            with_copyright += 1

prop = (with_copyright / eligible) if eligible else None
out = {
    'eligible_repos_with_readme_md': eligible,
    'readmes_with_copyright_info': with_copyright,
    'proportion': prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6sSyisU7zLUXsz5xLuHaecu5': 'file_storage/call_6sSyisU7zLUXsz5xLuHaecu5.json', 'var_call_OugEpRWZhyMbAvsZ17v2kgP3': 'file_storage/call_OugEpRWZhyMbAvsZ17v2kgP3.json'}

exec(code, env_args)
