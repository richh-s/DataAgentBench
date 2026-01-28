code = """import json, re, pandas as pd

commits_df = pd.DataFrame(var_call_dqqKvGzunQQ8spywDWrfTwzz)
commits_df['commit_count'] = pd.to_numeric(commits_df['commit_count'], errors='coerce').fillna(0).astype(int)

# load languages (may be in file)
lang_data = var_call_mSeL4BRqRIQoYjFg4b2Uxtav
if isinstance(lang_data, str):
    with open(lang_data, 'r', encoding='utf-8') as f:
        lang_data = json.load(f)
langs_df = pd.DataFrame(lang_data)

# infer main language as the language with max bytes mentioned in description
pat = re.compile(r"([A-Za-z0-9_+.#-]+)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc: str):
    if not isinstance(desc, str):
        return None
    pairs = pat.findall(desc)
    if not pairs:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pairs:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best_lang = lang
    return best_lang

langs_df['main_language'] = langs_df['language_description'].map(main_lang)

merged = commits_df.merge(langs_df[['repo_name','main_language']], on='repo_name', how='inner')
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')]

top5 = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_dqqKvGzunQQ8spywDWrfTwzz': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_call_mSeL4BRqRIQoYjFg4b2Uxtav': 'file_storage/call_mSeL4BRqRIQoYjFg4b2Uxtav.json'}

exec(code, env_args)
