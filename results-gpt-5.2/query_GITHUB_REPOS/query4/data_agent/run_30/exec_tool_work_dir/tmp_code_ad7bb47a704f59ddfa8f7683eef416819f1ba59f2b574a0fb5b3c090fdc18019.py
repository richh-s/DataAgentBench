code = """import json, re
import pandas as pd

commits = pd.DataFrame(var_call_oyFq292wtOiAmyIXVhcAKLE1)
commits['commit_count'] = commits['commit_count'].astype(int)

# load languages (may be file path)
langs_obj = var_call_dRNzW5y6JDC3nc6KIaVQXaCV
if isinstance(langs_obj, str):
    with open(langs_obj, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = langs_obj
langs_df = pd.DataFrame(langs)

# parse main language as the language with max bytes in description
pat = re.compile(r"([A-Za-z0-9_+.#-]+)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best = None
    best_bytes = -1
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best = lang
    return best

langs_df['main_language'] = langs_df['language_description'].map(main_lang)

merged = commits.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')
res = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower()!='python')]
res = res.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer_list = res['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_oyFq292wtOiAmyIXVhcAKLE1': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_dRNzW5y6JDC3nc6KIaVQXaCV': 'file_storage/call_dRNzW5y6JDC3nc6KIaVQXaCV.json'}

exec(code, env_args)
