code = """import json, re, pandas as pd

lang_src = var_call_EJ5jzH5Gr1V7kCKy3QKIzgQZ
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        lang_rows = json.load(f)
else:
    lang_rows = lang_src

comm_rows = var_call_MpO0ovNv65HAndBNjzplCZ95

lang_df = pd.DataFrame(lang_rows)
comm_df = pd.DataFrame(comm_rows)

pattern = re.compile(r'([A-Za-z0-9_+#\-\.]+)\s*\((\d[\d,]*)\s*bytes\)')

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pattern.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        try:
            val = int(b.replace(',', ''))
        except Exception:
            continue
        if val > best_bytes:
            best_lang, best_bytes = lang, val
    return best_lang

lang_df['main_language'] = lang_df['language_description'].map(main_lang)
merged = comm_df.merge(lang_df[['repo_name','main_language']], on='repo_name', how='left')
merged['commit_count'] = pd.to_numeric(merged['commit_count'], errors='coerce')
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')]
out = filtered.sort_values('commit_count', ascending=False).head(5)
answer = "\\n".join(out['repo_name'].tolist())
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_EJ5jzH5Gr1V7kCKy3QKIzgQZ': 'file_storage/call_EJ5jzH5Gr1V7kCKy3QKIzgQZ.json', 'var_call_MpO0ovNv65HAndBNjzplCZ95': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
