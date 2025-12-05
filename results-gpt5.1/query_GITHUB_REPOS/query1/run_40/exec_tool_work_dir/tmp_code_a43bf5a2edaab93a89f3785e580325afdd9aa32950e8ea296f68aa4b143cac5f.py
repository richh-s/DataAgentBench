code = """import json, pandas as pd

readmes_path = var_call_kR7lZtp4iq7rLqooqGfQLrkR
langs_path = var_call_nNFGj2BV5EBw5sARb9QgjMxJ

with open(readmes_path) as f:
    readmes = json.load(f)
with open(langs_path) as f:
    langs = json.load(f)

readmes_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)

langs_df['uses_python'] = langs_df['language_description'].str.contains('Python (', case=False, na=False)

no_py_repos = set(langs_df.loc[~langs_df['uses_python'], 'repo_name'])

readmes_no_py = readmes_df[readmes_df['repo_name'].isin(no_py_repos)].copy()

# simple case-insensitive substring search without regex to avoid errors
patterns = ['copyright', '©', 'copr.']

def has_copyright(text):
    if not isinstance(text, str):
        return False
    lower = text.lower()
    if '©' in text:
        return True
    if 'copr.' in lower:
        return True
    if 'copyright' in lower:
        return True
    return False

readmes_no_py['has_copyright'] = readmes_no_py['content'].apply(has_copyright)

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
