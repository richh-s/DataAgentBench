code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_DNUnE4G5QigyDYljTukmnKyh, 'r') as f:
    readmes = json.load(f)
with open(var_call_P8zDP4z5GDvb787NMfwTIsOH, 'r') as f:
    langs = json.load(f)

# Build DataFrames
readmes_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)

# Identify repos that use Python (any amount)
python_mask = langs_df['language_description'].str.contains('Python', case=False, na=False)
python_repos = set(langs_df.loc[python_mask, 'repo_name'])

# Filter README.md files to repos that do NOT use Python
readmes_df = readmes_df.rename(columns={'sample_repo_name': 'repo_name'})
non_py_readmes = readmes_df[~readmes_df['repo_name'].isin(python_repos)].copy()

# Heuristic for copyright info in README content
pattern = re.compile(r"copyright|\bcopr?\b|\b(c)\b|\b\u00a9\b|\(c\)", re.IGNORECASE)

non_py_readmes['has_copyright'] = non_py_readmes['content'].fillna('').apply(
    lambda txt: bool(pattern.search(txt))
)

# Compute proportion
if len(non_py_readmes) == 0:
    proportion = None
else:
    proportion = float(non_py_readmes['copyright'].mean()) if 'copyright' in non_py_readmes.columns else float(non_py_readmes['has_copyright'].mean())

result = {
    'total_non_python_readmes': int(len(non_py_readmes)),
    'num_with_copyright': int(non_py_readmes['has_copyright'].sum()),
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_DNUnE4G5QigyDYljTukmnKyh': 'file_storage/call_DNUnE4G5QigyDYljTukmnKyh.json', 'var_call_P8zDP4z5GDvb787NMfwTIsOH': 'file_storage/call_P8zDP4z5GDvb787NMfwTIsOH.json', 'var_call_FO3tbyHqEpPn4CmOffuzzBwR': 'file_storage/call_FO3tbyHqEpPn4CmOffuzzBwR.json', 'var_call_hMKjyKDC3A5b9wfNZpGhSG1K': 'file_storage/call_hMKjyKDC3A5b9wfNZpGhSG1K.json', 'var_call_3bOhKaPDm5riH2HBAr9aDQO7': 'file_storage/call_3bOhKaPDm5riH2HBAr9aDQO7.json', 'var_call_I2xEXFpwsr0gOzk7tZTb6hDi': 'file_storage/call_I2xEXFpwsr0gOzk7tZTb6hDi.json'}

exec(code, env_args)
