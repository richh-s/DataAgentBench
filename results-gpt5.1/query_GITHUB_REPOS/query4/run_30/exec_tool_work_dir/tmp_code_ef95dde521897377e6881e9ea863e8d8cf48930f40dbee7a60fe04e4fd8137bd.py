code = """import json, pandas as pd, os

# Load languages table from file
path = var_call_6lvpiDZFvmaTmHejQGLV1it2
with open(path, 'r') as f:
    languages_data = json.load(f)

langs_df = pd.DataFrame(languages_data)
commits_df = pd.DataFrame(var_call_qAIbBfmWfSd3Qb1Gwy5ePGTq)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

# Function to extract main language by max bytes from the natural language description
import re

def main_language(desc):
    if not isinstance(desc, str):
        return None
    # pattern like "Python (123,456 bytes)" or "Shell (40,034 bytes)"
    matches = re.findall(r"([A-Za-z+#]+) \(([0-9,]+) bytes\)", desc)
    if not matches:
        return None
    # pick language with max bytes
    max_lang, max_bytes = None, -1
    for lang, bytes_str in matches:
        b = int(bytes_str.replace(',', ''))
        if b > max_bytes:
            max_bytes = b
            max_lang = lang
    return max_lang

langs_df['main_language'] = langs_df['language_description'].apply(main_language)

# Merge commits with languages on repo_name
merged = commits_df.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')

# Filter out Python main language
filtered = merged[merged['main_language'].str.lower() != 'python']

# Sort by commit_count desc and take top 5
Top5 = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(Top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_qAIbBfmWfSd3Qb1Gwy5ePGTq': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_6lvpiDZFvmaTmHejQGLV1it2': 'file_storage/call_6lvpiDZFvmaTmHejQGLV1it2.json'}

exec(code, env_args)
