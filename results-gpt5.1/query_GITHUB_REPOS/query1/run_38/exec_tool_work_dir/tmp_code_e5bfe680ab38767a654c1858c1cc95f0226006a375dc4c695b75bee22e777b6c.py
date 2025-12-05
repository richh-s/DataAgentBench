code = """import json, re, pandas as pd

# Load full results for README repo mapping and README contents
with open(var_call_1dGFjv38vHpbxJ4fOx7rIB3S, 'r') as f:
    readme_meta = json.load(f)
with open(var_call_kfVKyyGrqTIpnwg5Z1WGoZJB, 'r') as f:
    readme_contents = json.load(f)
with open(var_call_fpCIlbzRPwlzPSjz7yZ2e059, 'r') as f:
    languages = json.load(f)

readme_meta_df = pd.DataFrame(readme_meta)
readme_contents_df = pd.DataFrame(readme_contents)
languages_df = pd.DataFrame(languages)

# Merge README meta with contents
readmes = pd.merge(readme_meta_df, readme_contents_df, on='id', how='inner')

# Determine which repos use Python based on language_description
lang = languages_df.copy()
lang['uses_python'] = lang['language_description'].str.contains(r"Python", case=False, na=False)

# Repos that do NOT use Python
no_py_repos = lang.loc[~lang['uses_python'], 'repo_name'].unique()

# Filter READMEs to those repos
readmes_no_py = readmes[readmes['sample_repo_name'].isin(no_py_repos)].copy()

# Define a heuristic for copyright info
pattern = re.compile(r"copyright|\bc\s*\d{4}|\u00a9|\(c\)\s*\d{4}", re.IGNORECASE)

readmes_no_py['has_copyright'] = readmes_no_py['content'].fillna('').apply(lambda x: bool(pattern.search(x)))

if len(readmes_no_py) == 0:
    proportion = None
else:
    proportion = float(readmes_no_py['copyright'].mean()) if 'copyright' in readmes_no_py.columns else float(readmes_no_py['has_copyright'].mean())

result = {
    'total_readmes_non_python_repos': int(len(readmes_no_py)),
    'num_with_copyright': int(readmes_no_py['has_copyright'].sum()) if len(readmes_no_py) > 0 else 0,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1dGFjv38vHpbxJ4fOx7rIB3S': 'file_storage/call_1dGFjv38vHpbxJ4fOx7rIB3S.json', 'var_call_fpCIlbzRPwlzPSjz7yZ2e059': 'file_storage/call_fpCIlbzRPwlzPSjz7yZ2e059.json', 'var_call_kfVKyyGrqTIpnwg5Z1WGoZJB': 'file_storage/call_kfVKyyGrqTIpnwg5Z1WGoZJB.json'}

exec(code, env_args)
