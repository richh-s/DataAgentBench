code = """import json, re, pandas as pd

# load languages (may be large file)
lang_src = var_call_CvGOsrRkPgtjpbN6f35kuM8Y
if isinstance(lang_src, str) and lang_src.endswith('.json'):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src

commits = var_call_wDslhU38sE3GrsOOrRlpRgWb

df_lang = pd.DataFrame(langs)
df_comm = pd.DataFrame(commits)

def main_language(desc: str):
    if desc is None:
        return None
    pairs = re.findall(r'([A-Za-z][A-Za-z0-9+#\-\. ]*) \((\d[\d,]*) bytes\)', desc)
    if not pairs:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pairs:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_lang, best_bytes = lang.strip(), n
    return best_lang

df_lang['main_language'] = df_lang['language_description'].map(main_language)

# join and filter non-Python
merged = df_comm.merge(df_lang[['repo_name','main_language']], on='repo_name', how='left')
merged['commit_count'] = merged['commit_count'].astype(int)
merged_non_py = merged[merged['main_language'].fillna('') != 'Python']

out = merged_non_py.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer_lines = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_lines))"""

env_args = {'var_call_CvGOsrRkPgtjpbN6f35kuM8Y': 'file_storage/call_CvGOsrRkPgtjpbN6f35kuM8Y.json', 'var_call_wDslhU38sE3GrsOOrRlpRgWb': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}]}

exec(code, env_args)
