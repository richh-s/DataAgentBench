code = """import json, re
import pandas as pd

# load languages (may be file path)
lang_src = var_call_rk5Lf0dlPCNSXNUdfqJbNqdb
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src

commits = var_call_HYXEqZbeugu8a3XWs3AH6DZJ

# parse main language as the one with max bytes in description
pat = re.compile(r'([A-Za-z0-9_+\-#.]+)\s*\(([,0-9]+)\s*bytes\)')
main_lang = {}
for r in langs:
    desc = r.get('language_description') or ''
    matches = pat.findall(desc)
    if not matches:
        continue
    best = None
    for lang, num in matches:
        b = int(num.replace(',', ''))
        if best is None or b > best[1]:
            best = (lang, b)
    main_lang[r['repo_name']] = best[0]

# compute top 5 by commits where main language != Python
rows = []
for r in commits:
    repo = r['repo_name']
    cc = int(r['commit_count'])
    lang = main_lang.get(repo)
    rows.append({'repo_name': repo, 'commit_count': cc, 'main_language': lang})

df = pd.DataFrame(rows)
# exclude python and unknown
out = df[(df['main_language'].notna()) & (df['main_language'].str.lower() != 'python')].sort_values('commit_count', ascending=False).head(5)
answer = out['repo_name'].tolist()
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_rk5Lf0dlPCNSXNUdfqJbNqdb': 'file_storage/call_rk5Lf0dlPCNSXNUdfqJbNqdb.json', 'var_call_HYXEqZbeugu8a3XWs3AH6DZJ': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
