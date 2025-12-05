code = """import json, re, pandas as pd

# langs is a list already; contents is in file
langs = var_call_ANhwcrC5xioFsXDrkOVIVWdQ
contents_path = var_call_xH0VZaMyvJSHZ0z00OOzxC4K

with open(contents_path, 'r') as f:
    contents = json.load(f)

# ensure they are lists of dicts
assert isinstance(contents, list)
assert isinstance(langs, list)

df_readme = pd.DataFrame(contents)

pattern = re.compile(r"copyright|\(c\)|©|all rights reserved", re.IGNORECASE)

df_readme['content'] = df_readme['content'].fillna('')

df_readme['has_copyright'] = df_readme['content'].apply(lambda x: bool(pattern.search(x)))

# languages

# each element should have repo_name, language_description

rows = []
for row in langs:
    if isinstance(row, dict) and 'repo_name' in row:
        rows.append(row)

df_langs = pd.DataFrame(rows)

mask_python = df_langs['language_description'].str.contains('Python', case=False, na=False)
python_repos = set(df_langs[mask_python]['repo_name'])

mask_not_python = ~df_readme['sample_repo_name'].isin(python_repos)
subset = df_readme[mask_not_python]

if len(subset) == 0:
    proportion = None
else:
    proportion = float(subset['has_copyright'].mean())

result = {"proportion_non_python_readmes_with_copyright": proportion,
          "total_non_python_readmes": int(len(subset))}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_xH0VZaMyvJSHZ0z00OOzxC4K': 'file_storage/call_xH0VZaMyvJSHZ0z00OOzxC4K.json', 'var_call_ANhwcrC5xioFsXDrkOVIVWdQ': 'file_storage/call_ANhwcrC5xioFsXDrkOVIVWdQ.json'}

exec(code, env_args)
