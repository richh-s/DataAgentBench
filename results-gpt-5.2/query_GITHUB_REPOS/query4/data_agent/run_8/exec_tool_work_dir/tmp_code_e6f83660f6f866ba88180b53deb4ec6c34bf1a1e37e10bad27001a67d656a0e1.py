code = """import json, re, pandas as pd

# load languages (may be file path)
lang_src = var_call_M6Z5iTnhPcrIIqRgqRsN9eL6
if isinstance(lang_src, str) and lang_src.endswith('.json'):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src

commits = var_call_431tL4nyelCHNii4uMKtbrhh

df_lang = pd.DataFrame(langs)
df_comm = pd.DataFrame(commits)

# parse main language by max bytes in language_description
pat = re.compile(r"([A-Za-z0-9+.#-]+)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best_lang = lang
    return best_lang

df_lang['main_language'] = df_lang['language_description'].map(main_lang)

# join with commit counts
# commit_count may be string
if 'commit_count' in df_comm.columns:
    df_comm['commit_count'] = pd.to_numeric(df_comm['commit_count'], errors='coerce')

merged = pd.merge(df_comm, df_lang[['repo_name','main_language']], on='repo_name', how='left')

# filter not Python main language (including unknown treated as not python?)
filtered = merged[(merged['main_language'].str.lower() != 'python') | (merged['main_language'].isna())]

# order by commits desc; take top 5
out = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer_list = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_M6Z5iTnhPcrIIqRgqRsN9eL6': 'file_storage/call_M6Z5iTnhPcrIIqRgqRsN9eL6.json', 'var_call_431tL4nyelCHNii4uMKtbrhh': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
