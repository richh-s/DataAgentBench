code = """import json, pandas as pd

languages_path = var_call_3hLjzhG6sOr5kYjhMxYGUJbN
with open(languages_path, 'r') as f:
    languages_data = json.load(f)

langs_df = pd.DataFrame(languages_data)

# Determine main language from the natural language description by taking the language with the highest bytes value
import re

def main_language(desc):
    # Find all occurrences of 'Language (bytes bytes)'
    pairs = re.findall(r"([A-Za-z+#]+) \((\d+) bytes\)", desc)
    if not pairs:
        return None
    # Select language with max bytes
    lang, _ = max(((lang, int(bytes_)) for lang, bytes_ in pairs), key=lambda x: x[1])
    return lang

langs_df['main_language'] = langs_df['language_description'].apply(main_language)

# Filter out Python as main language
non_python_langs = langs_df[langs_df['main_language'].str.lower() != 'python'][['repo_name']]

commits_df = pd.DataFrame(var_call_RgZb1naKcgcJTWfU3nc3LeQN)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

merged = commits_df.merge(non_python_langs, on='repo_name', how='inner')

top5 = merged.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_3hLjzhG6sOr5kYjhMxYGUJbN': 'file_storage/call_3hLjzhG6sOr5kYjhMxYGUJbN.json', 'var_call_RgZb1naKcgcJTWfU3nc3LeQN': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
