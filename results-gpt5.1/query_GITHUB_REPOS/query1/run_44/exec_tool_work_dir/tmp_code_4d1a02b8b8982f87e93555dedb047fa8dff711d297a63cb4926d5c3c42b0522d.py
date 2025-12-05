code = """import json, pandas as pd

# Load full results from files
import_path_readmes = var_call_0RCQtUXTlVCEPJbHrWxVVaVH
import_path_langs = var_call_2K2ZoDMjNUNZXkbywzTyu7o0
import_path_contents = var_call_X8aq7qf6cNKV0lyB4j5aNyO3

with open(import_path_readmes) as f:
    readmes = json.load(f)
with open(import_path_langs) as f:
    langs = json.load(f)
with open(import_path_contents) as f:
    contents = json.load(f)

# DataFrames
readmes_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)
contents_df = pd.DataFrame(contents)

# Determine repos that do not use Python (no 'Python (' substring in language_description)
no_python_langs_df = langs_df[~langs_df['language_description'].str.contains('Python (', case=False, na=False)]
no_python_repos = set(no_python_langs_df['repo_name'])

# README files and their repos
readmes_df = readmes_df.rename(columns={'sample_repo_name': 'repo_name'})
readme_repos = set(readmes_df['repo_name'])

# Repos that both have README.md and do not use Python
target_repos = readme_repos.intersection(no_python_repos)

# Map id -> content for README files
id_to_content = dict(zip(contents_df['id'], contents_df['content']))

# Filter README entries for target repos
target_readmes_df = readmes_df[readmes_df['repo_name'].isin(target_repos)].copy()

# Attach content
target_readmes_df['content'] = target_readmes_df['id'].map(id_to_content)

# Define a heuristic for copyright presence
keywords = ['copyright', '©', 'copr.']

def has_copyright(text):
    if not isinstance(text, str):
        return False
    lower = text.lower()
    return any(k in lower for k in keywords)

# Compute per-repo: does any README instance contain copyright
grouped = target_readmes_df.groupby('repo_name')['content'].apply(lambda col: any(copyright(text) if False else False))

# Oops, need correct function; recompute properly

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
