code = """import json, re, pandas as pd

commits = pd.DataFrame(var_call_UlVW2pqHP6LeW57xTF5p5N5O)
commits['commit_count'] = commits['commit_count'].astype(int)

# load full languages
lang_src = var_call_RU2NoLIQFpBBjdmQl0YDIUzs
if isinstance(lang_src, str) and lang_src.endswith('.json'):
    with open(lang_src, 'r', encoding='utf-8') as f:
        languages = json.load(f)
else:
    languages = lang_src
lang_df = pd.DataFrame(languages)

# parse primary language as the max bytes entry in language_description
pat = re.compile(r"([A-Za-z0-9_+#.-]+) \((\d[\d,]*) bytes\)")

def primary_lang(desc: str):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_lang, best_bytes = lang, n
    return best_lang

lang_df['primary_language'] = lang_df['language_description'].map(primary_lang)

# join with commits counts
df = commits.merge(lang_df[['repo_name','primary_language']], on='repo_name', how='left')

# filter main language != Python
filtered = df[df['primary_language'].str.lower().ne('python')]

# order by commits desc; take top 5
out = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
repo_names = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(repo_names))"""

env_args = {'var_call_UlVW2pqHP6LeW57xTF5p5N5O': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_RU2NoLIQFpBBjdmQl0YDIUzs': 'file_storage/call_RU2NoLIQFpBBjdmQl0YDIUzs.json', 'var_call_7xn35E6NuBfeSmTxO5H0vjJL': 'file_storage/call_7xn35E6NuBfeSmTxO5H0vjJL.json'}

exec(code, env_args)
