code = """import json, pandas as pd

commits = pd.DataFrame(var_call_JpQRmMtqMaUW4XrHCdR1EQ1o)
langs_path = var_call_vCoAxr7MbyviF68GbXuF8G2P
langs = pd.read_json(langs_path)

# Determine main language from natural language description by picking the language with max bytes
import re

def main_lang(desc):
    parts = re.findall(r"([A-Za-z0-9#++]+) \((\d+) bytes\)", desc)
    if not parts:
        return None
    return max(parts, key=lambda x: int(x[1]))[0]

langs['main_language'] = langs['language_description'].apply(main_lang)

merged = commits.merge(langs[['repo_name','main_language']], on='repo_name', how='left')

non_py = merged[merged['main_language'].str.lower() != 'python']
non_py_sorted = non_py.sort_values('commit_count', ascending=False).head(5)

result = non_py_sorted['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_JpQRmMtqMaUW4XrHCdR1EQ1o': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_vCoAxr7MbyviF68GbXuF8G2P': 'file_storage/call_vCoAxr7MbyviF68GbXuF8G2P.json'}

exec(code, env_args)
