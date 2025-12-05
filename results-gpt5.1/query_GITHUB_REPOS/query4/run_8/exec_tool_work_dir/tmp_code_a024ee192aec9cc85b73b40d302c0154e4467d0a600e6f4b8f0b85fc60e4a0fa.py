code = """import json, pandas as pd

commits_df = pd.DataFrame(var_call_3paL9MAsrAfjFa7WN7yDgJHT)

with open(var_call_stwOxTBbKmbQqGPqJB2qgNG7, 'r') as f:
    languages_data = json.load(f)
langs_df = pd.DataFrame(languages_data)

# Extract main language as the one with the largest bytes number mentioned first
# Pattern examples: "mainly written in Ruby (1,897 bytes)" or "includes: Ruby (22,438 bytes), Shell..." or "majority of the code is in Ruby (25,709 bytes)"

import re

def extract_main_language(desc):
    if not isinstance(desc, str):
        return None
    # Look for patterns like "Language (number bytes)" and take the first match
    matches = re.findall(r'([A-Za-z+#]+) \(([0-9,]+) bytes\)', desc)
    if not matches:
        return None
    # take the first tuple's language as main
    return matches[0][0]

langs_df['main_language'] = langs_df['language_description'].apply(extract_main_language)

# Filter out Python main language
non_py_langs = langs_df[langs_df['main_language'].str.lower() != 'python']

# Join with commits on repo_name
merged = commits_df.merge(non_py_langs[['repo_name','main_language']], on='repo_name', how='inner')

# Sort by commit_count desc and take top 5
merged['commit_count'] = merged['commit_count'].astype(int)
result = merged.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3paL9MAsrAfjFa7WN7yDgJHT': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_stwOxTBbKmbQqGPqJB2qgNG7': 'file_storage/call_stwOxTBbKmbQqGPqJB2qgNG7.json'}

exec(code, env_args)
