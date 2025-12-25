code = """import json, pandas as pd, os

commits_top = pd.DataFrame(var_call_Ul0B3HiYQ54cVphsCk2o435j)

with open(var_call_4hVspWw6o6w2zAj9N6BxG78q, 'r') as f:
    languages = pd.DataFrame(json.load(f))

# determine main language from language_description by picking the language with max bytes
import re

def main_lang(desc):
    parts = re.findall(r'([A-Za-z+#]+) \((\d+[,_]?\d*) bytes\)', desc)
    if not parts:
        return None
    best = max(parts, key=lambda x: int(x[1].replace(',', '').replace('_','')))
    return best[0]

languages['main_language'] = languages['language_description'].apply(main_lang)

merged = commits_top.merge(languages[['repo_name','main_language']], on='repo_name', how='left')

filtered = merged[merged['main_language'].str.lower() != 'python']

result = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Ul0B3HiYQ54cVphsCk2o435j': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_4hVspWw6o6w2zAj9N6BxG78q': 'file_storage/call_4hVspWw6o6w2zAj9N6BxG78q.json'}

exec(code, env_args)
