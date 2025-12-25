code = """import json, pandas as pd

commits = pd.DataFrame(var_call_0NK8h2kuHDUHIFg8d6mF89gV)
commits['commit_count'] = commits['commit_count'].astype(int)

import os
with open(var_call_AYEL5lrbTqVfV8izG9Aijg4K, 'r') as f:
    languages = pd.DataFrame(json.load(f))

# determine main language from language_description by picking the language with max bytes
import re

def main_lang(desc):
    parts = re.findall(r'([A-Za-z+#]+) \((\d+[\d,]*) bytes\)', desc)
    if not parts:
        return None
    # normalize and pick max bytes
    best = None
    best_b = -1
    for lang, b in parts:
        b_int = int(b.replace(',', ''))
        if b_int > best_b:
            best_b = b_int
            best = lang
    return best

languages['main_language'] = languages['language_description'].apply(main_lang)

# join commits with languages on repo_name
merged = commits.merge(languages[['repo_name','main_language']], on='repo_name', how='left')

# filter out main_language == 'Python'
filtered = merged[merged['main_language'].ne('Python')]

# sort by commit_count desc and take top 5
result = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_0NK8h2kuHDUHIFg8d6mF89gV': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_AYEL5lrbTqVfV8izG9Aijg4K': 'file_storage/call_AYEL5lrbTqVfV8izG9Aijg4K.json'}

exec(code, env_args)
