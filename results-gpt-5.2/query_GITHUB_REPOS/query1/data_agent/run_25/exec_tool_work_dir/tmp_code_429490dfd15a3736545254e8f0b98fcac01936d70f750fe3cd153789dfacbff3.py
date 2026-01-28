code = """import json, re
import pandas as pd

# Load non-python repos list
non_py = var_call_mt29Qn9QEkS4tOAr0F0GQjaZ
if isinstance(non_py, str):
    with open(non_py, 'r', encoding='utf-8') as f:
        non_py = json.load(f)
non_py_set = set(r['repo_name'] for r in non_py if r.get('repo_name'))

# Load README contents
readmes = var_call_59kTH58V84VQyFBaubUNI8z4
if isinstance(readmes, str):
    with open(readmes, 'r', encoding='utf-8') as f:
        readmes = json.load(f)

# If multiple readme.md per repo, treat repo as having README.md if any record exists
# Detect copyright info
pat = re.compile(r'(?i)\bcopyright\b|\b\(c\)\b|\b©\b')

repo_has_readme = set()
repo_has_copyright = set()
for r in readmes:
    repo = r.get('repo_name')
    if not repo or repo not in non_py_set:
        continue
    repo_has_readme.add(repo)
    content = r.get('content') or ''
    if pat.search(content):
        repo_has_copyright.add(repo)

num_readme = len(repo_has_readme)
num_copyright = len(repo_has_copyright)
prop = (num_copyright / num_readme) if num_readme else None

out = {
    "non_python_repos_with_readme_md": num_readme,
    "with_copyright_in_readme_md": num_copyright,
    "proportion": prop
}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_mt29Qn9QEkS4tOAr0F0GQjaZ': 'file_storage/call_mt29Qn9QEkS4tOAr0F0GQjaZ.json', 'var_call_59kTH58V84VQyFBaubUNI8z4': 'file_storage/call_59kTH58V84VQyFBaubUNI8z4.json'}

exec(code, env_args)
