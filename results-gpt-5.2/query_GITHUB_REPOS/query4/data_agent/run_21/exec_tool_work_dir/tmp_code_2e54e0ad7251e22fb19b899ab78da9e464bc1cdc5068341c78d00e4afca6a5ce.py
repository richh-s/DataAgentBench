code = """import json, re
import pandas as pd

langs_src = var_call_TftN9nuOyHHVA3T4dgPur5oM
# If large result stored as json file path
if isinstance(langs_src, str) and langs_src.endswith('.json'):
    with open(langs_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = langs_src

commits = var_call_mlZFWcAf95aRTTSzKVIwL1jm

# Parse language_description to determine main language (largest bytes)
pat = re.compile(r"([A-Za-z0-9#+\-\.]+)\s*\((\d[\d,]*)\s*bytes\)")
main_lang = {}
for r in langs:
    desc = r.get('language_description') or ''
    matches = pat.findall(desc)
    if not matches:
        continue
    best_lang = None
    best_bytes = -1
    for lang, b in matches:
        try:
            n = int(b.replace(',', ''))
        except:
            continue
        if n > best_bytes:
            best_bytes = n
            best_lang = lang
    if best_lang is not None:
        main_lang[r['repo_name']] = best_lang

# Take commit counts, filter main language != Python
rows = []
for c in commits:
    repo = c['repo_name']
    if repo not in main_lang:
        continue
    if str(main_lang[repo]).lower() == 'python':
        continue
    rows.append((repo, int(c['commit_count'])))

rows_sorted = sorted(rows, key=lambda x: x[1], reverse=True)[:5]
repo_names = [r[0] for r in rows_sorted]

print('__RESULT__:')
print(json.dumps(repo_names))"""

env_args = {'var_call_TftN9nuOyHHVA3T4dgPur5oM': 'file_storage/call_TftN9nuOyHHVA3T4dgPur5oM.json', 'var_call_mlZFWcAf95aRTTSzKVIwL1jm': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
