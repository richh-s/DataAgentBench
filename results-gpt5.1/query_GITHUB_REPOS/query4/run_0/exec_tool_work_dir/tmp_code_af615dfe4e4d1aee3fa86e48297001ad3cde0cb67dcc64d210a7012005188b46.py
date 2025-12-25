code = """import json, re, pandas as pd
from pathlib import Path

# Load full languages data from file
path = Path(var_call_wTooyK5GY8EfnRLWEcmZ0VA4)
with path.open() as f:
    languages_data = json.load(f)

# Create DataFrame
lang_df = pd.DataFrame(languages_data)

# Function to extract main language assuming it's the one with 'mainly' or 'majority' or first listed
def extract_main_language(desc: str) -> str:
    if not isinstance(desc, str):
        return None
    m = re.search(r"mainly written in ([A-Za-z+#]+)", desc)
    if m:
        return m.group(1)
    m = re.search(r"majority of the code is in ([A-Za-z+#]+)", desc)
    if m:
        return m.group(1)
    m = re.search(r"built in ([A-Za-z+#]+)", desc)
    if m:
        return m.group(1)
    m = re.search(r"includes: ([A-Za-z+#]+)", desc)
    if m:
        return m.group(1)
    return None

lang_df['main_language'] = lang_df['language_description'].apply(extract_main_language)

# Filter out Python main language
non_python = lang_df[lang_df['main_language'].str.lower() != 'python'][['repo_name', 'main_language']]

commits_df = pd.DataFrame(var_call_sKQNFH62ajEuLWd9H4ZAFQSS)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

merged = commits_df.merge(non_python, on='repo_name', how='inner')

top5 = merged.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_wTooyK5GY8EfnRLWEcmZ0VA4': 'file_storage/call_wTooyK5GY8EfnRLWEcmZ0VA4.json', 'var_call_sKQNFH62ajEuLWd9H4ZAFQSS': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
