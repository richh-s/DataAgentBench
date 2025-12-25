code = """import json, pandas as pd

commits_df = pd.DataFrame(var_call_0X8VHc94DCDuLSEJlV2K3cK6)
langs = json.load(open(var_call_pj7cQLU0T3nDbAv3aeenob4Z))
langs_df = pd.DataFrame(langs)

def main_language(desc):
    parts = desc.split('bytes')
    if not parts:
        return None
    first = parts[0]
    if '(' in first:
        lang_part = first.split('(')[0]
    else:
        lang_part = first
    for token in ['The codebase includes:', 'This repository is mainly written in', 'The majority of the code is in', 'While most of the project is built in', 'This repository is mainly written in', 'The project is primarily composed of']:
        lang_part = lang_part.replace(token, '')
    return lang_part.strip().strip(':').strip()

langs_df['main_language'] = langs_df['language_description'].apply(main_language)
merged = commits_df.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[merged['main_language'].str.lower() != 'python']
result = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_0X8VHc94DCDuLSEJlV2K3cK6': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_pj7cQLU0T3nDbAv3aeenob4Z': 'file_storage/call_pj7cQLU0T3nDbAv3aeenob4Z.json'}

exec(code, env_args)
