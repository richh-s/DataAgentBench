code = """import json, pandas as pd, re

def load_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

langs = load_maybe(var_call_b14I0im9Vtlkgx3zAcPD1DCB)
readme_contents = load_maybe(var_call_47HHSuhlOoYFgjRP8ma3EhYb)
readme_files = load_maybe(var_call_Enc0EHkt5xGozf6B9BwDtJT7)

non_python_repos = set(r['repo_name'] for r in langs)
readme_repos = set(r['repo_name'] for r in readme_files)

den_repos = non_python_repos & readme_repos

pattern = re.compile(r"copyright\s*(?:\(c\)|©)?\s*\d{0,4}|\b©\b", re.IGNORECASE)

has_copyright = set()
for r in readme_contents:
    repo = r.get('repo_name')
    if repo in den_repos:
        content = r.get('content') or ''
        if pattern.search(content):
            has_copyright.add(repo)

num = len(has_copyright)
den = len(den_repos)
prop = (num/den) if den else None

out = {
    "non_python_with_readme_md": den,
    "with_copyright_in_readme_md": num,
    "proportion": prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_b14I0im9Vtlkgx3zAcPD1DCB': 'file_storage/call_b14I0im9Vtlkgx3zAcPD1DCB.json', 'var_call_47HHSuhlOoYFgjRP8ma3EhYb': 'file_storage/call_47HHSuhlOoYFgjRP8ma3EhYb.json', 'var_call_Enc0EHkt5xGozf6B9BwDtJT7': 'file_storage/call_Enc0EHkt5xGozf6B9BwDtJT7.json'}

exec(code, env_args)
