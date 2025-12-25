code = """import json, pandas as pd, os

commits_top = pd.DataFrame(var_call_sHh8kFYJfD5WaWOcLX0VYjSb)

with open(var_call_faPIJjYS0DrWVcYDGQbrSNFc, 'r') as f:
    languages = pd.DataFrame(json.load(f))

# infer main language from description (first mentioned language with highest bytes)
import re

def main_lang(desc):
    # pattern like "Python (123,456 bytes)"; we assume first mention is main if it says "mainly" or "majority" or list order
    m = re.search(r"([A-Za-z+#]+) \([0-9,]+ bytes\)", desc)
    return m.group(1) if m else None

languages['main_language'] = languages['language_description'].apply(main_lang)

merged = commits_top.merge(languages[['repo_name','main_language']], on='repo_name', how='left')

non_py = merged[merged['main_language'].str.lower() != 'python']

result_repos = non_py.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result_repos)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_sHh8kFYJfD5WaWOcLX0VYjSb': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_faPIJjYS0DrWVcYDGQbrSNFc': 'file_storage/call_faPIJjYS0DrWVcYDGQbrSNFc.json', 'var_call_n3lqHmZtRCS1Yr51wXmRSaxs': ['commits', 'contents', 'files']}

exec(code, env_args)
