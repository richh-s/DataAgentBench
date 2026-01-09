code = """import json, re
import pandas as pd

# commits counts
df_commits = pd.DataFrame(var_call_jQ66rxMAAmIXQToo179kfQ0n)
df_commits['commit_count'] = df_commits['commit_count'].astype(int)

# load languages (possibly from file)
lang_data = var_call_Q0ptOmJE4eTmy3ITUv907P1a
if isinstance(lang_data, str):
    with open(lang_data, 'r', encoding='utf-8') as f:
        lang_data = json.load(f)

df_lang = pd.DataFrame(lang_data)

# parse main language: choose language with max bytes in description
pattern = re.compile(r"([A-Za-z][A-Za-z0-9+.#\- ]*)\s*\((\d{1,3}(?:,\d{3})*)\s*bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pattern.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best_lang = lang.strip()
    return best_lang

df_lang['main_language'] = df_lang['language_description'].apply(main_lang)

# join and filter main_language != Python
merged = df_commits.merge(df_lang[['repo_name','main_language']], on='repo_name', how='inner')
filtered = merged[merged['main_language'].str.lower().ne('python')].copy()

# top 5 by commit_count desc
res = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer_list = res['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_jQ66rxMAAmIXQToo179kfQ0n': [{'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}], 'var_call_Q0ptOmJE4eTmy3ITUv907P1a': 'file_storage/call_Q0ptOmJE4eTmy3ITUv907P1a.json'}

exec(code, env_args)
