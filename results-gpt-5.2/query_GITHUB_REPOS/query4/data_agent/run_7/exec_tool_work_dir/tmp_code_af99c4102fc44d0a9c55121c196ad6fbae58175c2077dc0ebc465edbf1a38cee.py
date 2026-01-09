code = """import json, re
import pandas as pd

# load languages (may be a file path)
lang_src = var_call_9Tt48dXEwYgvgY4UkwG1AoWS
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src

commits = var_call_VY4pIAE4PQMWJ5I7Xr3rnHNI

lang_df = pd.DataFrame(langs)
comm_df = pd.DataFrame(commits)

comm_df['commit_count'] = pd.to_numeric(comm_df['commit_count'])

# parse primary language by max bytes in description
def primary_language(desc: str):
    if desc is None:
        return None
    pairs = re.findall(r'([A-Za-z0-9+#\-\. ]+)\s*\((\d[\d,]*)\s*bytes\)', desc)
    if not pairs:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pairs:
        b_int = int(b.replace(',', ''))
        lang_clean = lang.strip()
        if b_int > best_bytes:
            best_bytes = b_int
            best_lang = lang_clean
    return best_lang

lang_df['primary_language'] = lang_df['language_description'].map(primary_language)

merged = pd.merge(comm_df, lang_df[['repo_name','primary_language']], on='repo_name', how='left')

# main language is not Python
filtered = merged[(merged['primary_language'].notna()) & (merged['primary_language'].str.lower() != 'python')]

top5 = filtered.sort_values('commit_count', ascending=False).head(5)
answer_list = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_9Tt48dXEwYgvgY4UkwG1AoWS': 'file_storage/call_9Tt48dXEwYgvgY4UkwG1AoWS.json', 'var_call_VY4pIAE4PQMWJ5I7Xr3rnHNI': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
