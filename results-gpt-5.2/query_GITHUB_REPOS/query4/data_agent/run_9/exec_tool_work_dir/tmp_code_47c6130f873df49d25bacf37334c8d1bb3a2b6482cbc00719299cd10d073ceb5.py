code = """import json, re, pandas as pd

# load languages (may be file path)
lang_src = var_call_PF67cjw72jfoCjzKHDeRM2qk
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src

commits = var_call_jX75u9nKz15h8U0vBJx2RLET

# parse primary language by max bytes mentioned
pat = re.compile(r"([A-Za-z0-9+#+.-]+)\s*\((\d[\d,]*)\s*bytes\)")
primary = {}
for r in langs:
    desc = r.get('language_description') or ''
    matches = pat.findall(desc)
    if not matches:
        continue
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        bb = int(b.replace(',',''))
        if bb > best_bytes:
            best_bytes = bb
            best_lang = lang
    if best_lang:
        primary[r['repo_name']] = best_lang

# filter commit top where primary != Python
rows=[]
for r in commits:
    repo = r['repo_name']
    cc = int(r['commit_count']) if r.get('commit_count') is not None else 0
    lang = primary.get(repo)
    if lang is None:
        continue
    if lang.lower() != 'python':
        rows.append((repo, cc, lang))

rows_sorted = sorted(rows, key=lambda x: x[1], reverse=True)[:5]
answer_list = [r[0] for r in rows_sorted]

print('__RESULT__:')
print(json.dumps({'repos': answer_list}))"""

env_args = {'var_call_PF67cjw72jfoCjzKHDeRM2qk': 'file_storage/call_PF67cjw72jfoCjzKHDeRM2qk.json', 'var_call_jX75u9nKz15h8U0vBJx2RLET': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
