code = """import json, re, pandas as pd

# load languages full result
path = var_call_dGdHp4CqG5QOOgd6AtrEuYFj
with open(path, 'r', encoding='utf-8') as f:
    langs = json.load(f)

df_lang = pd.DataFrame(langs)

def main_lang(desc):
    if desc is None:
        return None
    # find all occurrences like 'Python (123 bytes)'
    pairs = re.findall(r'([A-Za-z0-9+#.\- ]+?)\s*\((\d[\d,]*)\s*bytes\)', desc)
    if not pairs:
        return None
    best = None
    best_bytes = -1
    for lang, b in pairs:
        lang = lang.strip().strip(':').strip(',')
        b = int(b.replace(',', ''))
        if b > best_bytes:
            best_bytes = b
            best = lang
    return best

df_lang['main_language'] = df_lang['language_description'].map(main_lang)

# commits result
commits = var_call_SJ9E7vSf2qIzNqjklQhCT6Gm
cdf = pd.DataFrame(commits)
if not cdf.empty:
    cdf['commit_count'] = cdf['commit_count'].astype(int)

# join and filter main language != Python
merged = pd.merge(cdf, df_lang[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[merged['main_language'].notna() & (merged['main_language'].str.lower() != 'python')]
filtered = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
result = filtered['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_dGdHp4CqG5QOOgd6AtrEuYFj': 'file_storage/call_dGdHp4CqG5QOOgd6AtrEuYFj.json', 'var_call_SJ9E7vSf2qIzNqjklQhCT6Gm': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
