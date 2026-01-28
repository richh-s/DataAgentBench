code = """import json, re

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

non_py = load_records(var_call_EF9qwiy7nPdtGxr7p1hEpwAj)
readmes = load_records(var_call_hDKxo2iHkP5jiKFq6j3kE75n)

non_py_set = set(r.get('repo_name') for r in non_py if r.get('repo_name'))

repo_to_texts = {}
for r in readmes:
    repo = r.get('repo_name')
    if not repo or repo not in non_py_set:
        continue
    txt = r.get('content') or ''
    repo_to_texts.setdefault(repo, []).append(txt)

copyright_re = re.compile(r'\\bcopyright\\b|\\b\\(c\\)\\b|\\b©\\b', re.IGNORECASE)

total = len(repo_to_texts)
with_cp = 0
for repo, texts in repo_to_texts.items():
    combined = "\\n\\n".join(texts)
    if copyright_re.search(combined):
        with_cp += 1

prop = (with_cp / total) if total else None
out = {
    'non_python_repos_with_readme_md': total,
    'readme_md_with_copyright': with_cp,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_EF9qwiy7nPdtGxr7p1hEpwAj': 'file_storage/call_EF9qwiy7nPdtGxr7p1hEpwAj.json', 'var_call_hDKxo2iHkP5jiKFq6j3kE75n': 'file_storage/call_hDKxo2iHkP5jiKFq6j3kE75n.json'}

exec(code, env_args)
