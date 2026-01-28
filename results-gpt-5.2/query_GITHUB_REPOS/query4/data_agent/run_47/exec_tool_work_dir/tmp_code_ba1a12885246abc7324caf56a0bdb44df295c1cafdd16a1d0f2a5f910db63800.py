code = """import json, pandas as pd, re

lang_src = var_call_6VW0cBxnaF57dQlFuucklk33
# stream-parse minimal from file to avoid heavy pandas
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        lang_records = json.load(f)
else:
    lang_records = lang_src

# only need languages for repos that appear in commits table
commit_recs = var_call_KqI9O0Rkk7cfpElLHNQunZVs
repos_needed = {r['repo_name'] for r in commit_recs}

pat = re.compile(r"([A-Za-z0-9_+#\.\- ]+?)\s*\((\d[\d,]*)\s*bytes\)")

def primary_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        bi = int(b.replace(',', ''))
        if bi > best_bytes:
            best_bytes = bi
            best_lang = lang.strip()
    return best_lang

lang_map = {}
for rec in lang_records:
    rn = rec.get('repo_name')
    if rn in repos_needed:
        pl = primary_lang(rec.get('language_description'))
        if pl is not None:
            lang_map[rn] = pl

rows = []
for r in commit_recs:
    rn = r['repo_name']
    pl = lang_map.get(rn)
    if pl is None:
        continue
    if pl.strip().lower() == 'python':
        continue
    cc = int(r['commit_count'])
    rows.append((cc, rn))

rows.sort(key=lambda x: (-x[0], x[1]))
result = [rn for cc, rn in rows[:5]]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6VW0cBxnaF57dQlFuucklk33': 'file_storage/call_6VW0cBxnaF57dQlFuucklk33.json', 'var_call_KqI9O0Rkk7cfpElLHNQunZVs': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}]}

exec(code, env_args)
