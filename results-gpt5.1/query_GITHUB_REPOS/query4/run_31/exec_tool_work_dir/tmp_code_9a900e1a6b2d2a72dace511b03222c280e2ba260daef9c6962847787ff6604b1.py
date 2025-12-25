code = """import json, pandas as pd
from pathlib import Path

# Load languages data from file path
path = Path(var_call_gcKns2ZBPRJTeJSAtjc4R6N1)
with open(path, 'r') as f:
    languages_data = json.load(f)

commits_df = pd.DataFrame(var_call_Jbz1uNM4piZKYQxLq65sLMYy)
languages_df = pd.DataFrame(languages_data)

# Determine main language: parse language_description to find language with max bytes
import re

def get_main_language(desc):
    if not isinstance(desc, str):
        return None
    # Pattern like: "Ruby (22,438 bytes)" possibly multiple separated by commas or "followed by"
    matches = re.findall(r"([A-Za-z+#]+) \(([0-9,]+) bytes\)", desc)
    if not matches:
        return None
    # pick language with max bytes
    max_lang = None
    max_bytes = -1
    for lang, bytes_str in matches:
        b = int(bytes_str.replace(',', ''))
        if b > max_bytes:
            max_bytes = b
            max_lang = lang
    return max_lang

languages_df['main_language'] = languages_df['language_description'].apply(get_main_language)

# Merge commits with languages on repo_name
merged = commits_df.merge(languages_df[['repo_name','main_language']], on='repo_name', how='left')

# Filter out Python main language
filtered = merged[merged['main_language'].str.lower() != 'python']

# Sort by commit_count desc and take top 5
a = filtered.copy()
a['commit_count'] = a['commit_count'].astype(int)
result_repos = a.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result_repos)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Jbz1uNM4piZKYQxLq65sLMYy': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_gcKns2ZBPRJTeJSAtjc4R6N1': 'file_storage/call_gcKns2ZBPRJTeJSAtjc4R6N1.json'}

exec(code, env_args)
