code = """import json, re, pandas as pd

# load languages (may be stored in a file path)
langs_src = var_call_crNwGSZSGEugQJgB4s27ckeN
if isinstance(langs_src, str):
    with open(langs_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = langs_src

commits = var_call_7cQhpudqjzCpngWewF8O7iI3

df_lang = pd.DataFrame(langs)
df_comm = pd.DataFrame(commits)

df_comm['commit_count'] = pd.to_numeric(df_comm['commit_count'])

# parse main language as the language with max bytes in description
pat = re.compile(r'([A-Za-z0-9_+.#-]+)\s*\((\d[\d,]*)\s*bytes\)')

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best = None
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if best is None or n > best[1]:
            best = (lang, n)
    return best[0]

df_lang['main_language'] = df_lang['language_description'].map(main_lang)

# join with commits and filter main language != Python
merged = df_comm.merge(df_lang[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')]

# top five by commits
res = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_crNwGSZSGEugQJgB4s27ckeN': 'file_storage/call_crNwGSZSGEugQJgB4s27ckeN.json', 'var_call_7cQhpudqjzCpngWewF8O7iI3': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}]}

exec(code, env_args)
