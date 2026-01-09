code = """import json, re, pandas as pd

# Load languages (may be in a file)
langs_src = var_call_dflmcS9E1UPx5BaPwjfVVTvc
if isinstance(langs_src, str):
    with open(langs_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = langs_src

commits = var_call_hLbySwgFA44u6gRvWhkihj0l

df_lang = pd.DataFrame(langs)
df_comm = pd.DataFrame(commits)

# Parse main language as the language with the largest byte count in language_description
pat = re.compile(r'([A-Za-z0-9+#\-]+)\s*\((\d[\d,]*)\s*bytes\)')

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best = None
    best_bytes = -1
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best = lang
    return best

df_lang['main_language'] = df_lang['language_description'].apply(main_lang)

# Join to commits; count is string -> int
if 'commit_count' in df_comm.columns:
    df_comm['commit_count'] = df_comm['commit_count'].astype(int)

df = df_comm.merge(df_lang[['repo_name','main_language']], on='repo_name', how='left')

# Filter main language not Python (also exclude unknown)
df = df[df['main_language'].notna() & (df['main_language'].str.lower() != 'python')]

# Top 5 by commit_count
out = df.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dflmcS9E1UPx5BaPwjfVVTvc': 'file_storage/call_dflmcS9E1UPx5BaPwjfVVTvc.json', 'var_call_hLbySwgFA44u6gRvWhkihj0l': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}]}

exec(code, env_args)
