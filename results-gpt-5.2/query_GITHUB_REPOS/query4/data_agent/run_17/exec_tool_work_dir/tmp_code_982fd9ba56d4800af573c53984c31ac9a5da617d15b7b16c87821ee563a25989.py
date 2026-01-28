code = """import json, re, pandas as pd

# Load commits counts
commits = pd.DataFrame(var_call_wghmUFRkUg8rd4NvjkxLopJu)
commits['commit_count'] = commits['commit_count'].astype(int)

# Load languages (may be file path)
lang_src = var_call_boPwqgu2thQL1WuiknATKCKy
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src
langs_df = pd.DataFrame(langs)

# Determine main language from language_description by max bytes
pat = re.compile(r'([^,()]+?)\s*\(([-\d,]+)\s*bytes\)')

def main_lang(desc):
    if desc is None:
        return None
    matches = pat.findall(desc)
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        lang = lang.strip().strip('.')
        b = int(b.replace(',', ''))
        if b > best_bytes:
            best_bytes = b
            best_lang = lang
    return best_lang

langs_df['main_language'] = langs_df['language_description'].map(main_lang)

# Join and filter main_language != Python
merged = commits.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[merged['main_language'].notna() & (merged['main_language'].str.lower() != 'python')]

# Top 5 by commits
out = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_wghmUFRkUg8rd4NvjkxLopJu': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_boPwqgu2thQL1WuiknATKCKy': 'file_storage/call_boPwqgu2thQL1WuiknATKCKy.json'}

exec(code, env_args)
