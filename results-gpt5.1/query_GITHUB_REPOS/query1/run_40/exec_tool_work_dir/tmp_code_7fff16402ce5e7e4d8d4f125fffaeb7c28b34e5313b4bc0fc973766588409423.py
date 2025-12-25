code = """import json, pandas as pd

readmes_path = var_call_kR7lZtp4iq7rLqooqGfQLrkR
langs_path = var_call_nNFGj2BV5EBw5sARb9QgjMxJ

with open(readmes_path) as f:
    readmes = json.load(f)
with open(langs_path) as f:
    langs = json.load(f)

readmes_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)

# identify repos that use Python (language_description mentioning 'Python (')
langs_df['uses_python'] = langs_df['language_description'].str.contains('Python (', case=False, na=False)

# repos that do NOT use Python
no_py_repos = set(langs_df.loc[~langs_df['uses_python'], 'repo_name'])

# filter readmes to those repos
readmes_no_py = readmes_df[readmes_df['repo_name'].isin(no_py_repos)].copy()

# simple heuristic for copyright info
patterns = ['copyright', '©', 'copr.']
readmes_no_py['has_copyright'] = readmes_no_py['content'].str.contains('|'.join(patterns), case=False, na=False)

if len(readmes_no_py) == 0:
    result = {"proportion": None, "count_with_copyright": 0, "total_readmes_no_python": 0}
else:
    prop = float(readmes_no_py['copyright'].mean())

result = {
    "proportion": float(readmes_no_py['has_copyright'].mean()) if len(readmes_no_py) > 0 else None,
    "count_with_copyright": int(readmes_no_py['has_copyright'].sum()),
    "total_readmes_no_python": int(len(readmes_no_py))
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kR7lZtp4iq7rLqooqGfQLrkR': 'file_storage/call_kR7lZtp4iq7rLqooqGfQLrkR.json', 'var_call_nNFGj2BV5EBw5sARb9QgjMxJ': 'file_storage/call_nNFGj2BV5EBw5sARb9QgjMxJ.json', 'var_call_TQpzpFanzflkdIGaKUfYzRSl': 'file_storage/call_TQpzpFanzflkdIGaKUfYzRSl.json', 'var_call_3z1VJ97v4FW1ezZCgeSvJezJ': 'file_storage/call_3z1VJ97v4FW1ezZCgeSvJezJ.json', 'var_call_De0ye2LgDcXXQXp5vxBzVj1e': 'file_storage/call_De0ye2LgDcXXQXp5vxBzVj1e.json', 'var_call_r5gKoLfMVLkxe3FE7N39eHRB': 'file_storage/call_r5gKoLfMVLkxe3FE7N39eHRB.json'}

exec(code, env_args)
