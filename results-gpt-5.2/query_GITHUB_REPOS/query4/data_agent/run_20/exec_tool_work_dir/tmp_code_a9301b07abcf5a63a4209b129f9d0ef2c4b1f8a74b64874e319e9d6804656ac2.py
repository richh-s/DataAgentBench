code = """import json, re, pandas as pd

commits = pd.DataFrame(var_call_r1tQBdutY9g29MBlLqpkBEjS)
commits['commit_count'] = commits['commit_count'].astype(int)

# load full languages table
lang_src = var_call_v9yGVklepgw4UVQaO7NfJect
if isinstance(lang_src, str) and lang_src.endswith('.json'):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs_records = json.load(f)
else:
    langs_records = lang_src
langs = pd.DataFrame(langs_records)

# parse main language from language_description by extracting (Language, bytes) pairs and picking max bytes
pat = re.compile(r"([A-Za-z0-9_+\-#.]+) \((\d[\d,]*) bytes\)")

def main_lang(desc):
    if desc is None:
        return None
    pairs = [(m.group(1), int(m.group(2).replace(',', ''))) for m in pat.finditer(desc)]
    if not pairs:
        return None
    return max(pairs, key=lambda x: x[1])[0]

langs['main_language'] = langs['language_description'].map(main_lang)

df = commits.merge(langs[['repo_name','main_language']], on='repo_name', how='left')
# exclude Python main language
res = df[(df['main_language'].notna()) & (df['main_language'].str.lower() != 'python')]
res = res.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer_list = res['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_r1tQBdutY9g29MBlLqpkBEjS': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_call_v9yGVklepgw4UVQaO7NfJect': 'file_storage/call_v9yGVklepgw4UVQaO7NfJect.json'}

exec(code, env_args)
