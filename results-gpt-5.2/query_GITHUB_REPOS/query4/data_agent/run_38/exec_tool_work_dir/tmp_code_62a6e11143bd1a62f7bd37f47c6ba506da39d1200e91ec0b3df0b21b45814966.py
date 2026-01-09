code = """import json, re, pandas as pd

# commits counts
commits_df = pd.DataFrame(var_call_C0Ntv5UmEPWzFQsWFhkCBJPm)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

# languages (load full if needed)
lang_src = var_call_UNO3GFYtV4SSxOAWDrQU8M63
if isinstance(lang_src, str) and lang_src.endswith('.json'):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src
langs_df = pd.DataFrame(langs)

# parse primary language from language_description by taking language with max bytes
pat = re.compile(r'([A-Za-z][A-Za-z0-9+#\- ]*)\s*\((\d[\d,]*)\s*bytes\)')

def primary_lang(desc):
    if not isinstance(desc, str):
        return None
    pairs = pat.findall(desc)
    if not pairs:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pairs:
        b_int = int(b.replace(',', ''))
        if b_int > best_bytes:
            best_bytes = b_int
            best_lang = lang.strip()
    return best_lang

langs_df['primary_language'] = langs_df['language_description'].map(primary_lang)

merged = commits_df.merge(langs_df[['repo_name','primary_language']], on='repo_name', how='inner')
filtered = merged[merged['primary_language'].notna() & (merged['primary_language'].str.lower() != 'python')]

top5 = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_C0Ntv5UmEPWzFQsWFhkCBJPm': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}], 'var_call_UNO3GFYtV4SSxOAWDrQU8M63': 'file_storage/call_UNO3GFYtV4SSxOAWDrQU8M63.json'}

exec(code, env_args)
