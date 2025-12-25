code = """import json, re
import pandas as pd

# languages data is in a JSON file path
path = var_call_GrUsPee5YeDoSS2hdZ9MdVEy
with open(path, 'r') as f:
    languages_data = json.load(f)

langs_df = pd.DataFrame(languages_data)

# helper to extract main language as the one with max bytes
lang_re = re.compile(r"([A-Za-z+#]+) \((\d+,?\d*) bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = lang_re.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, bytes_str in matches:
        b = int(bytes_str.replace(',', ''))
        if b > best_bytes:
            best_lang, best_bytes = lang, b
    return best_lang

langs_df['main_language'] = langs_df['language_description'].apply(main_lang)

# commits data
commits_df = pd.DataFrame(var_call_6gR2OoBbhCbBzZisaAgPHUEr)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

merged = commits_df.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')

non_py = merged[merged['main_language'].str.lower() != 'python']

top5 = non_py.sort_values('commit_count', ascending=False).head(5)

result = top5['repo_name'].tolist()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GrUsPee5YeDoSS2hdZ9MdVEy': 'file_storage/call_GrUsPee5YeDoSS2hdZ9MdVEy.json', 'var_call_6gR2OoBbhCbBzZisaAgPHUEr': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
