code = """import json, pandas as pd, os

# Load commit counts
commits = pd.DataFrame(var_call_TtVtyeRwNhczVBt94qmFnEki)
commits['commit_count'] = commits['commit_count'].astype(int)

# Load full languages data from file
path = var_call_Gkxlr9Nz3m6uUgbXtgTIqDMy
with open(path, 'r') as f:
    languages = pd.DataFrame(json.load(f))

# Derive main language from language_description by taking the first 'X (n bytes)' entry
import re

def main_lang(desc):
    m = re.search(r"([A-Za-z+#]+) \(\d+ bytes\)", desc)
    return m.group(1) if m else None

languages['main_language'] = languages['language_description'].apply(main_lang)

# Filter out repos where main language is Python
non_py = languages[languages['main_language'].str.lower() != 'python']

# Join with commits
merged = commits.merge(non_py[['repo_name']], on='repo_name', how='inner')

# Get top 5 by commit_count
top5 = merged.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_TtVtyeRwNhczVBt94qmFnEki': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_Gkxlr9Nz3m6uUgbXtgTIqDMy': 'file_storage/call_Gkxlr9Nz3m6uUgbXtgTIqDMy.json'}

exec(code, env_args)
