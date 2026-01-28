code = """import json, re

# load languages safely
lang_src = var_call_9Tt48dXEwYgvgY4UkwG1AoWS
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src

# build repo->primary_language
repo_primary = {}
pat = re.compile(r'([A-Za-z0-9+#\-\. ]+)\s*\((\d[\d,]*)\s*bytes\)')
for rec in langs:
    rn = rec.get('repo_name')
    desc = rec.get('language_description') or ''
    best_lang = None
    best_bytes = -1
    for lang, b in pat.findall(desc):
        bi = int(b.replace(',', ''))
        if bi > best_bytes:
            best_bytes = bi
            best_lang = lang.strip()
    if rn is not None:
        repo_primary[rn] = best_lang

commits = var_call_VY4pIAE4PQMWJ5I7Xr3rnHNI

rows = []
for c in commits:
    rn = c.get('repo_name')
    cc = int(c.get('commit_count'))
    pl = repo_primary.get(rn)
    if pl and pl.lower() != 'python':
        rows.append((cc, rn))

rows.sort(reverse=True)
answer_list = [rn for cc, rn in rows[:5]]

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_9Tt48dXEwYgvgY4UkwG1AoWS': 'file_storage/call_9Tt48dXEwYgvgY4UkwG1AoWS.json', 'var_call_VY4pIAE4PQMWJ5I7Xr3rnHNI': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
