code = """import json, re, pandas as pd

# commits counts
commits_df = pd.DataFrame(var_call_oMUhIUPeELoxJrvb2s617diG)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

# load languages full
lang_src = var_call_BQqcVHNeZCao6fQCy7q8TpRA
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src
langs_df = pd.DataFrame(langs)

# parse main language as the language with max bytes
pat = re.compile(r"([A-Za-z0-9_+#\-\.]+)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        nb = int(b.replace(',', ''))
        if nb > best_bytes:
            best_lang, best_bytes = lang, nb
    return best_lang

langs_df['main_language'] = langs_df['language_description'].map(main_lang)

# join and filter not Python
merged = commits_df.merge(langs_df[['repo_name','main_language']], on='repo_name', how='inner')
res = merged[merged['main_language'].notna() & (merged['main_language'].str.lower() != 'python')]
res = res.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer_list = res['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_oMUhIUPeELoxJrvb2s617diG': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_call_BQqcVHNeZCao6fQCy7q8TpRA': 'file_storage/call_BQqcVHNeZCao6fQCy7q8TpRA.json'}

exec(code, env_args)
