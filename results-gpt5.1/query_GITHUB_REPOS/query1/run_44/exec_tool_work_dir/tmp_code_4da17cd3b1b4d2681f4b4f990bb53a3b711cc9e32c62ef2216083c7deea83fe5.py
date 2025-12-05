code = """import json, pandas as pd, re

import_path_readmes = var_call_0RCQtUXTlVCEPJbHrWxVVaVH
import_path_langs = var_call_2K2ZoDMjNUNZXkbywzTyu7o0
import_path_contents = var_call_X8aq7qf6cNKV0lyB4j5aNyO3

with open(import_path_readmes) as f:
    readmes = json.load(f)
with open(import_path_langs) as f:
    langs = json.load(f)
with open(import_path_contents) as f:
    contents = json.load(f)

readmes_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)
contents_df = pd.DataFrame(contents)

# Use regex=False to avoid interpreting pattern chars
no_python_langs_df = langs_df[~langs_df['language_description'].str.contains('Python (', case=False, na=False, regex=False)]
no_python_repos = set(no_python_langs_df['repo_name'])

readmes_df = readmes_df.rename(columns={'sample_repo_name': 'repo_name'})
readme_repos = set(readmes_df['repo_name'])

target_repos = readme_repos.intersection(no_python_repos)

id_to_content = dict(zip(contents_df['id'], contents_df['content']))

target_readmes_df = readmes_df[readmes_df['repo_name'].isin(target_repos)].copy()

target_readmes_df['content'] = target_readmes_df['id'].map(id_to_content)

keywords = ['copyright', '©', 'copr.']

def repo_has_copyright(group):
    for text in group['content']:
        if not isinstance(text, str):
            continue
        lower = text.lower()
        if any(k in lower for k in keywords):
            return True
    return False

repo_grouped = target_readmes_df.groupby('repo_name').apply(repo_has_copyright)

num_repos = len(target_repos)
num_with_copyright = int(repo_grouped.sum())
proportion = float(num_with_copyright) / num_repos if num_repos > 0 else None

result = {
    'num_repos_with_readme_and_no_python': num_repos,
    'num_with_copyright_readme': num_with_copyright,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_0RCQtUXTlVCEPJbHrWxVVaVH': 'file_storage/call_0RCQtUXTlVCEPJbHrWxVVaVH.json', 'var_call_2K2ZoDMjNUNZXkbywzTyu7o0': 'file_storage/call_2K2ZoDMjNUNZXkbywzTyu7o0.json', 'var_call_X8aq7qf6cNKV0lyB4j5aNyO3': 'file_storage/call_X8aq7qf6cNKV0lyB4j5aNyO3.json'}

exec(code, env_args)
