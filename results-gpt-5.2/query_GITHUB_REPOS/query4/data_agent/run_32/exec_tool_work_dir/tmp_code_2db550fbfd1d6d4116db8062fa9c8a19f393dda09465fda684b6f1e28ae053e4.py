code = """import json, re, pandas as pd

commit_counts = var_call_cjMAfozHlKvSQoZWrcP0k1Dn

# load languages (may be file path)
lang_src = var_call_N0wA9h0EOmfTmlXmfnwAmV2H
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        languages = json.load(f)
else:
    languages = lang_src

def main_language(desc: str):
    if desc is None:
        return None
    pairs = re.findall(r'([A-Za-z0-9+#\-\. ]+)\s*\((\d[\d,]*)\s*bytes\)', desc)
    if not pairs:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pairs:
        b_int = int(b.replace(',', ''))
        lang = lang.strip()
        if b_int > best_bytes:
            best_bytes = b_int
            best_lang = lang
    return best_lang

lang_map = {}
for r in languages:
    lang_map[r['repo_name']] = main_language(r.get('language_description',''))

rows = []
for r in commit_counts:
    repo = r['repo_name']
    ml = lang_map.get(repo)
    if ml is None:
        continue
    if ml.lower() == 'python':
        continue
    rows.append({'repo_name': repo, 'commit_count': int(r['commit_count']), 'main_language': ml})

rows_sorted = sorted(rows, key=lambda x: (-x['commit_count'], x['repo_name']))
top5 = [r['repo_name'] for r in rows_sorted[:5]]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_cjMAfozHlKvSQoZWrcP0k1Dn': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_N0wA9h0EOmfTmlXmfnwAmV2H': 'file_storage/call_N0wA9h0EOmfTmlXmfnwAmV2H.json', 'var_call_eCwvOT8R79zBng1Bf4bSihZg': 'file_storage/call_eCwvOT8R79zBng1Bf4bSihZg.json'}

exec(code, env_args)
