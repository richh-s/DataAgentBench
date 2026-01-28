code = """import json, re
import pandas as pd

commit_counts = pd.DataFrame(var_call_ScmsiMrXOwoBIHINJ3uGrhjn)
commit_counts['commit_count'] = commit_counts['commit_count'].astype(int)

# load languages (may be a file path)
lang_data = var_call_SYTMafizsfQUT7H4DshQGRnT
if isinstance(lang_data, str):
    with open(lang_data, 'r', encoding='utf-8') as f:
        lang_records = json.load(f)
else:
    lang_records = lang_data
langs = pd.DataFrame(lang_records)

# function to extract main language (max bytes)
pat = re.compile(r'([A-Za-z0-9#+\-\. ]+?)\s*\((\d[\d,]*)\s*bytes\)')

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best_lang = lang.strip()
    return best_lang

langs['main_language'] = langs['language_description'].map(main_lang)

merged = commit_counts.merge(langs[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[merged['main_language'].notna() & (merged['main_language'].str.lower() != 'python')]

top5 = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_ScmsiMrXOwoBIHINJ3uGrhjn': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_SYTMafizsfQUT7H4DshQGRnT': 'file_storage/call_SYTMafizsfQUT7H4DshQGRnT.json'}

exec(code, env_args)
