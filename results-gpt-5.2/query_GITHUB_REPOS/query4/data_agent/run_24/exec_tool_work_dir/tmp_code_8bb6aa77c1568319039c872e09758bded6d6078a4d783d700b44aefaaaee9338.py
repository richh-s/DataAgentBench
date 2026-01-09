code = """import json, re

commit_counts = var_call_I9iQR3OmWIOnYh2TBPWJ7Ks3
lang_path_or_list = var_call_Wj05X3gCVCSAO1iL50VhLPjY

# Load languages table
if isinstance(lang_path_or_list, str):
    with open(lang_path_or_list, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_path_or_list

# Build map repo -> main language by max bytes parsed from description
pat = re.compile(r"([A-Za-z0-9_+.#-]+)\s*\((\d[\d,]*)\s*bytes\)")
main_lang = {}
for r in langs:
    desc = r.get('language_description') or ''
    matches = pat.findall(desc)
    if not matches:
        continue
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        b_int = int(b.replace(',', ''))
        if b_int > best_bytes:
            best_bytes = b_int
            best_lang = lang
    if best_lang:
        main_lang[r['repo_name']] = best_lang

# Filter commit_counts where main language != Python
rows = []
for r in commit_counts:
    repo = r['repo_name']
    cnt = int(r['commit_count'])
    lang = main_lang.get(repo)
    if lang is None:
        continue
    if lang.lower() != 'python':
        rows.append((repo, cnt, lang))

rows.sort(key=lambda x: x[1], reverse=True)
Top5 = [repo for repo, cnt, lang in rows[:5]]

print('__RESULT__:')
print(json.dumps(Top5))"""

env_args = {'var_call_I9iQR3OmWIOnYh2TBPWJ7Ks3': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_Wj05X3gCVCSAO1iL50VhLPjY': 'file_storage/call_Wj05X3gCVCSAO1iL50VhLPjY.json'}

exec(code, env_args)
