code = """import json, pandas as pd, re

commits_df = pd.DataFrame(var_call_kUfMNOHGUXsD7TdjLNrpOmqg)

with open(var_call_7S8QPJmi2FYNY1uzySjlcX7E, 'r') as f:
    languages_data = json.load(f)

languages_df = pd.DataFrame(languages_data)

# Determine main language from language_description by picking the language with max bytes

def extract_main_language(desc):
    matches = re.findall(r'([A-Za-z0-9#[++-]+) \(([0-9,]+) bytes\)', desc)
    if not matches:
        return None
    max_lang = None
    max_bytes = -1
    for lang, bytes_str in matches:
        try:
            b = int(bytes_str.replace(',', ''))
        except Exception:
            continue
        if b > max_bytes:
            max_bytes = b
            max_lang = lang
    return max_lang

languages_df['main_language'] = languages_df['language_description'].apply(extract_main_language)

merged = commits_df.merge(languages_df[['repo_name','main_language']], on='repo_name', how='left')

filtered = merged[merged['main_language'].str.lower() != 'python']

filtered['commit_count'] = filtered['commit_count'].astype(int)

result_names = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result_names)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kUfMNOHGUXsD7TdjLNrpOmqg': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_7S8QPJmi2FYNY1uzySjlcX7E': 'file_storage/call_7S8QPJmi2FYNY1uzySjlcX7E.json'}

exec(code, env_args)
