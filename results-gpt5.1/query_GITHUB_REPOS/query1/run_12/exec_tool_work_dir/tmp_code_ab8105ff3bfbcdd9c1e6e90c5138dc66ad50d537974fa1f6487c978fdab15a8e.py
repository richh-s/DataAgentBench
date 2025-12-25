code = """import json, pandas as pd

# Load full results from files
with open(var_call_4BGqYqNJBLGUjZzkZkUGRrGV, 'r') as f:
    readmes = json.load(f)
with open(var_call_7r9v5irq4j3s5ZWjE9N6psnn, 'r') as f:
    langs = json.load(f)

# Build DataFrames
df_readmes = pd.DataFrame(readmes)
df_langs = pd.DataFrame(langs)

# Identify repos that do NOT use Python
mask_no_python = ~df_langs['language_description'].str.contains('Python', case=False, na=False)
repos_no_python = df_langs.loc[mask_no_python, 'repo_name'].unique()

# Filter README.md files to those repos
readmes_no_python = df_readmes[df_readmes['sample_repo_name'].isin(repos_no_python)].copy()

# Define a simple heuristic for copyright info
copyright_terms = ['copyright', '\u00a9', '(c)']
pattern = '|'.join(copyright_terms)

readmes_no_python['has_copyright'] = readmes_no_python['content'].str.contains(pattern, case=False, na=False)

# Compute proportion
if len(readmes_no_python) == 0:
    proportion = None
else:
    proportion = float(readmes_no_python['has_copyright'].mean())

result = {
    'num_readmes_no_python': int(len(readmes_no_python)),
    'num_with_copyright': int(readmes_no_python['has_copyright'].sum()) if len(readmes_no_python) > 0 else 0,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4BGqYqNJBLGUjZzkZkUGRrGV': 'file_storage/call_4BGqYqNJBLGUjZzkZkUGRrGV.json', 'var_call_7r9v5irq4j3s5ZWjE9N6psnn': 'file_storage/call_7r9v5irq4j3s5ZWjE9N6psnn.json'}

exec(code, env_args)
