code = """import json, re, pandas as pd

# Load languages (may be stored as json file path)
lang_src = var_call_oFdlmxDutTXLmg5JcVkePkzM
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        languages = json.load(f)
else:
    languages = lang_src

commits = var_call_RqdBNgh9qmSuzGLukUKVmPJA

lang_df = pd.DataFrame(languages)
comm_df = pd.DataFrame(commits)

# parse language bytes from description, choose max bytes as main language
pat = re.compile(r"([A-Za-z0-9_+\-#/\.]+)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc: str):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        try:
            n = int(b.replace(',', ''))
        except Exception:
            continue
        if n > best_bytes:
            best_bytes = n
            best_lang = lang
    return best_lang

lang_df['main_language'] = lang_df['language_description'].map(main_lang)

# combine with commits counts
comm_df['commit_count'] = comm_df['commit_count'].astype(int)
merged = comm_df.merge(lang_df[['repo_name','main_language']], on='repo_name', how='left')

# filter main language is not Python
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')]

# top 5 by commits
out = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_oFdlmxDutTXLmg5JcVkePkzM': 'file_storage/call_oFdlmxDutTXLmg5JcVkePkzM.json', 'var_call_RqdBNgh9qmSuzGLukUKVmPJA': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'facebook/react', 'commit_count': '178'}]}

exec(code, env_args)
