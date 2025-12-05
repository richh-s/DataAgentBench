code = """import json, pandas as pd
commits = pd.DataFrame(var_call_H71GuC534vQYGyED0jWucP2p)
langs_path = var_call_wRlSK2JLGhsimkRH6qXKPkah
with open(langs_path, 'r') as f:
    langs = pd.DataFrame(json.load(f))
# determine main language from language_description by picking language with max bytes
import re

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    # find all "Name (number bytes)"
    matches = re.findall(r"([A-Za-z+#]+) \((\d+[,_]?\d*) bytes\)", desc)
    if not matches:
        return None
    # pick with max bytes
    best = None
    maxb = -1
    for lang, num in matches:
        num = int(num.replace(',', '').replace('_',''))
        if num > maxb:
            maxb = num
            best = lang
    return best

langs['main_language'] = langs['language_description'].map(main_lang)
merged = commits.merge(langs[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[merged['main_language'].str.lower() != 'python']
filtered['commit_count'] = filtered['commit_count'].astype(int)
result = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()
import json as j
out = j.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_H71GuC534vQYGyED0jWucP2p': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_wRlSK2JLGhsimkRH6qXKPkah': 'file_storage/call_wRlSK2JLGhsimkRH6qXKPkah.json', 'var_call_jLYSryrmZSs6C8jWKFFWBZTe': ['languages', 'repos', 'licenses']}

exec(code, env_args)
