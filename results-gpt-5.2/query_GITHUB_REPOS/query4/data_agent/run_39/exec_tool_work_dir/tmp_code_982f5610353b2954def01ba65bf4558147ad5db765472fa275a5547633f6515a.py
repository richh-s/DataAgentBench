code = """import json, re, pandas as pd

# Load languages
lang_path = var_call_GS6jT83MhNcOahoAgqApkumS
with open(lang_path, 'r', encoding='utf-8') as f:
    langs = json.load(f)
df_lang = pd.DataFrame(langs)

# Parse main language from language_description by extracting (Language, bytes) pairs and taking max bytes
pat = re.compile(r"([A-Za-z0-9_+.#-]+) \((\d[\d,]*) bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    pairs = pat.findall(desc)
    if not pairs:
        return None
    best = None
    best_bytes = -1
    for lang, b in pairs:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best = lang
    return best

df_lang['main_language'] = df_lang['language_description'].map(main_lang)

# Top 5 by commits
df_comm = pd.DataFrame(var_call_L8YQuQ62Dw7uG3nGUd6WCF8r)
df_comm['commit_count'] = df_comm['commit_count'].astype(int)

# Join and filter out Python
merged = df_comm.merge(df_lang[['repo_name','main_language']], on='repo_name', how='left')
res = merged[merged['main_language'].str.lower().ne('python')].sort_values('commit_count', ascending=False).head(5)
answer_list = res['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_GS6jT83MhNcOahoAgqApkumS': 'file_storage/call_GS6jT83MhNcOahoAgqApkumS.json', 'var_call_lcCv8qZroB5uf3R94foTvwO6': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_L8YQuQ62Dw7uG3nGUd6WCF8r': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}]}

exec(code, env_args)
