code = """import json, re
import pandas as pd

# commits top list
commits = pd.DataFrame(var_call_Lbi4bRfbXvULPEQUN95MTnYh)
commits['commit_count'] = commits['commit_count'].astype(int)

# load languages full
path = var_call_e61kBjEFTFRDf76u21OFETrW
with open(path, 'r', encoding='utf-8') as f:
    langs_list = json.load(f)
langs = pd.DataFrame(langs_list)

# parse main language from language_description by extracting (Language, bytes)
pat = re.compile(r'([A-Za-z0-9+#\-\. ]+?)\s*\((\d[\d,]*)\s*bytes\)')

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    pairs = [(m.group(1).strip(), int(m.group(2).replace(',',''))) for m in pat.finditer(desc)]
    if not pairs:
        return None
    return max(pairs, key=lambda x: x[1])[0]

langs['main_language'] = langs['language_description'].map(main_lang)

# merge and filter main_language != Python
m = commits.merge(langs[['repo_name','main_language']], on='repo_name', how='left')
non_py = m[(m['main_language'].notna()) & (m['main_language'].str.lower() != 'python')]

# order by commit_count desc and take top 5
res = non_py.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer = res['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_Lbi4bRfbXvULPEQUN95MTnYh': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_e61kBjEFTFRDf76u21OFETrW': 'file_storage/call_e61kBjEFTFRDf76u21OFETrW.json'}

exec(code, env_args)
