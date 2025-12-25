code = """import json, pandas as pd

commits = pd.DataFrame(var_call_YZJBarfubFE3c0pPMJFnrgUH)
langs_path = var_call_FF1dXQg4yJkrolVGUHmynSSi
langs = pd.read_json(langs_path)

# Normalize types
commits['commit_count'] = commits['commit_count'].astype(int)

# Determine main language: parse between first '(' after a language name
# language_description examples mention "mainly written in Ruby ..." or "The majority of the code is in Ruby", or listing with bytes.
import re

def extract_main_lang(desc):
    # get first 'Language (' or pattern 'mainly written in X (' or 'The majority of the code is in X ('
    m = re.search(r"(mainly written in|majority of the code is in|built in|is in) ([A-Za-z+#]+) \(", desc)
    if m:
        return m.group(2)
    # fallback: first 'Word (digits bytes)'
    m = re.search(r"([A-Za-z+#]+) \(\d", desc)
    if m:
        return m.group(1)
    return None

langs['main_language'] = langs['language_description'].apply(extract_main_lang)

# Exclude Python main language
non_py_langs = langs[langs['main_language'].str.lower() != 'python']

merged = commits.merge(non_py_langs[['repo_name']], on='repo_name', how='inner')

result = merged.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_YZJBarfubFE3c0pPMJFnrgUH': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_FF1dXQg4yJkrolVGUHmynSSi': 'file_storage/call_FF1dXQg4yJkrolVGUHmynSSi.json'}

exec(code, env_args)
