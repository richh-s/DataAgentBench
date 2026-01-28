code = """import json, re, pandas as pd

# load languages (may be large)
lang_src = var_call_b2ZIsaaa9hVrZ4JMlCJBa7Hl
if isinstance(lang_src, str) and lang_src.endswith('.json'):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src

commits = var_call_QkjD028FSLzcblpTq57HxTuC

lang_map = {r['repo_name']: r.get('language_description','') for r in langs}

def main_language(desc: str):
    if not desc:
        return None
    # extract "Language (123 bytes)" patterns
    pairs = re.findall(r'([A-Za-z0-9_+.#-]+)\s*\((\d[\d,]*)\s*bytes\)', desc)
    if not pairs:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pairs:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_lang, best_bytes = lang, n
    return best_lang

rows = []
for r in commits:
    repo = r['repo_name']
    ml = main_language(lang_map.get(repo))
    rows.append({'repo_name': repo, 'commit_count': int(r['commit_count']), 'main_language': ml})

df = pd.DataFrame(rows)
# exclude Python main language
out = df[df['main_language'].fillna('') != 'Python'].sort_values('commit_count', ascending=False).head(5)
answer_list = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_b2ZIsaaa9hVrZ4JMlCJBa7Hl': 'file_storage/call_b2ZIsaaa9hVrZ4JMlCJBa7Hl.json', 'var_call_QkjD028FSLzcblpTq57HxTuC': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
