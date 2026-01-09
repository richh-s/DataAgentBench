code = """import json, re

langs_src = var_call_nHhhU9lmMtXl7RPl8V6HmtMK
if isinstance(langs_src, str):
    with open(langs_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = langs_src

commits = var_call_MEefoDMSjre68gfGUEQ3mqQh

# Build map only for repos we need
needed = {r['repo_name'] for r in commits}
lang_map = {}
pat = re.compile(r'([A-Za-z0-9_+#\.\- ]+)\s*\((\d[\d,]*)\s*bytes\)')
for rec in langs:
    rn = rec.get('repo_name')
    if rn not in needed:
        continue
    desc = rec.get('language_description') or ''
    best_lang = None
    best_bytes = -1
    for lang, b in pat.findall(desc):
        bi = int(b.replace(',', ''))
        if bi > best_bytes:
            best_bytes = bi
            best_lang = lang.strip().rstrip(':')
    lang_map[rn] = best_lang

rows = []
for r in commits:
    rn = r['repo_name']
    ml = lang_map.get(rn)
    cc_raw = r.get('commit_count')
    cc = int(cc_raw) if isinstance(cc_raw, str) else int(cc_raw)
    if ml is None:
        continue
    if ml.lower() == 'python':
        continue
    rows.append((cc, rn))

rows.sort(reverse=True)
answer_list = [rn for cc, rn in rows[:5]]

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_nHhhU9lmMtXl7RPl8V6HmtMK': 'file_storage/call_nHhhU9lmMtXl7RPl8V6HmtMK.json', 'var_call_MEefoDMSjre68gfGUEQ3mqQh': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
