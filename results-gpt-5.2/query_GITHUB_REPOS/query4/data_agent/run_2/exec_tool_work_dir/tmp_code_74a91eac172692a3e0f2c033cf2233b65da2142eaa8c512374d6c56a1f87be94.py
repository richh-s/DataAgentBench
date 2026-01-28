code = """import json, re, pandas as pd

# Load languages (may be file path)
lang_src = var_call_ygqhYDBOGBiN2fgYJI2XOrUi
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src

commits = var_call_dsRFpCPOtUW4ZvD4K2UbuK1q

# Parse main language from language_description by extracting (Language, bytes)
pat = re.compile(r"([A-Za-z0-9_+.#-]+)\s*\((\d[\d,]*)\s*bytes\)")
main_lang = {}
for r in langs:
    desc = r.get('language_description') or ''
    pairs = [(m.group(1), int(m.group(2).replace(',',''))) for m in pat.finditer(desc)]
    if not pairs:
        continue
    pairs.sort(key=lambda x: x[1], reverse=True)
    main_lang[r['repo_name']] = pairs[0][0]

# Filter commits to repos with known main language != Python
rows = []
for r in commits:
    repo = r['repo_name']
    if repo in main_lang and main_lang[repo] != 'Python':
        rows.append((repo, int(r['commit_count'])))

rows.sort(key=lambda x: x[1], reverse=True)
top5 = [repo for repo,_ in rows[:5]]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_ygqhYDBOGBiN2fgYJI2XOrUi': 'file_storage/call_ygqhYDBOGBiN2fgYJI2XOrUi.json', 'var_call_dsRFpCPOtUW4ZvD4K2UbuK1q': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_call_yyg6cjg8nuPYlm1cNPGGquap': 'file_storage/call_yyg6cjg8nuPYlm1cNPGGquap.json'}

exec(code, env_args)
