code = """import json, re, pandas as pd

# load languages from file
path = var_call_BlTh32g3ZCuWe5PtHzCFelXB
with open(path, 'r', encoding='utf-8') as f:
    langs = json.load(f)
langs_df = pd.DataFrame(langs)

# parse primary language as max bytes in description
pat = re.compile(r'([A-Za-z][A-Za-z0-9+.#\- ]*)\s*\((\d[\d,]*)\s*bytes\)')

def primary_lang(desc):
    if desc is None:
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best = None
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if best is None or n > best[1]:
            best = (lang.strip(), n)
    return best[0]

langs_df['primary_language'] = langs_df['language_description'].map(primary_lang)
primary = langs_df[['repo_name','primary_language']]

commits_df = pd.DataFrame(var_call_lYrqbyYL52Jc6hxKu5xSOBfK)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

merged = commits_df.merge(primary, on='repo_name', how='left')
non_py = merged[merged['primary_language'].str.lower().ne('python') | merged['primary_language'].isna()]
non_py = non_py.sort_values('commit_count', ascending=False).head(5)
ans = non_py['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_BlTh32g3ZCuWe5PtHzCFelXB': 'file_storage/call_BlTh32g3ZCuWe5PtHzCFelXB.json', 'var_call_lYrqbyYL52Jc6hxKu5xSOBfK': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
