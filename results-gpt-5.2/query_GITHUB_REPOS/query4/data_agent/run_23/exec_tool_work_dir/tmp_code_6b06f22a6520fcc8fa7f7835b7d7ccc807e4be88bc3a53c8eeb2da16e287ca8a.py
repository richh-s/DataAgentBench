code = """import json, re, pandas as pd

# Load languages table (may be file path)
lang_src = var_call_98sLe8meEKWwA8en4RwmMXT2
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src

commits = var_call_Upfnzn6Xzug4EBNwPZZi2FQ3

lang_df = pd.DataFrame(langs)
comm_df = pd.DataFrame(commits)

# Parse main language as the language with highest byte count in language_description
pattern = re.compile(r"([A-Za-z0-9+#\-\. ]+)\s*\((\d[\d,]*)\s*bytes\)")

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
            best_lang, best_bytes = lang.strip(), n
    return best_lang

lang_df['main_language'] = lang_df['language_description'].map(main_lang)

# join with commit counts
comm_df['commit_count'] = comm_df['commit_count'].astype(int)
merged = comm_df.merge(lang_df[['repo_name','main_language']], on='repo_name', how='left')

# filter main language not Python
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')]

top5 = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
ans = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_98sLe8meEKWwA8en4RwmMXT2': 'file_storage/call_98sLe8meEKWwA8en4RwmMXT2.json', 'var_call_Upfnzn6Xzug4EBNwPZZi2FQ3': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
