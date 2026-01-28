code = """import json, re

commit_counts = var_call_cjMAfozHlKvSQoZWrcP0k1Dn

lang_src = var_call_N0wA9h0EOmfTmlXmfnwAmV2H
with open(lang_src, 'r', encoding='utf-8') as f:
    languages = json.load(f)

repo_set = {r['repo_name'] for r in commit_counts}

pat = re.compile(r'([A-Za-z0-9+#\-\. ]+)\s*\((\d[\d,]*)\s*bytes\)')

def main_language(desc):
    best_lang = None
    best_bytes = -1
    for lang, b in pat.findall(desc or ''):
        bi = int(b.replace(',', ''))
        if bi > best_bytes:
            best_bytes = bi
            best_lang = lang.strip()
    return best_lang

lang_map = {}
for r in languages:
    repo = r.get('repo_name')
    if repo in repo_set:
        lang_map[repo] = main_language(r.get('language_description',''))

rows = []
for r in commit_counts:
    repo = r['repo_name']
    ml = lang_map.get(repo)
    if ml and ml.lower() != 'python':
        rows.append((int(r['commit_count']), repo))

rows.sort(key=lambda x: (-x[0], x[1]))
ans = [repo for _, repo in rows[:5]]

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_cjMAfozHlKvSQoZWrcP0k1Dn': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_N0wA9h0EOmfTmlXmfnwAmV2H': 'file_storage/call_N0wA9h0EOmfTmlXmfnwAmV2H.json', 'var_call_eCwvOT8R79zBng1Bf4bSihZg': 'file_storage/call_eCwvOT8R79zBng1Bf4bSihZg.json'}

exec(code, env_args)
