code = """import json, re, pandas as pd

# load languages table result (may be a file path)
lang_src = var_call_6VW0cBxnaF57dQlFuucklk33
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        lang_records = json.load(f)
else:
    lang_records = lang_src

commits_records = var_call_KqI9O0Rkk7cfpElLHNQunZVs

lang_df = pd.DataFrame(lang_records)
comm_df = pd.DataFrame(commits_records)

# parse primary language from language_description by picking max bytes
pat = re.compile(r"([A-Za-z0-9_+#\.\- ]+?)\s*\((\d[\d,]*)\s*bytes\)")

def primary_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        b_int = int(b.replace(',', ''))
        if b_int > best_bytes:
            best_bytes = b_int
            best_lang = lang.strip()
    return best_lang

lang_df['primary_language'] = lang_df['language_description'].map(primary_lang)

# join with commit counts
comm_df['commit_count'] = pd.to_numeric(comm_df['commit_count'], errors='coerce')
merged = pd.merge(comm_df, lang_df[['repo_name','primary_language']], on='repo_name', how='left')

# filter primary language not Python
filtered = merged[(merged['primary_language'].notna()) & (merged['primary_language'].str.lower() != 'python')]

# top 5 by commits
out = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
repo_names = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(repo_names))"""

env_args = {'var_call_6VW0cBxnaF57dQlFuucklk33': 'file_storage/call_6VW0cBxnaF57dQlFuucklk33.json', 'var_call_KqI9O0Rkk7cfpElLHNQunZVs': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}]}

exec(code, env_args)
