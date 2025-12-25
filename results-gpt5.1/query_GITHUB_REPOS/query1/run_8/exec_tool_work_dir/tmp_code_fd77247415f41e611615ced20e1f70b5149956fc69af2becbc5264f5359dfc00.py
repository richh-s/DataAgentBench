code = """import json, re, pandas as pd

contents_path = var_call_xH0VZaMyvJSHZ0z00OOzxC4K
langs = var_call_ANhwcrC5xioFsXDrkOVIVWdQ

with open(contents_path, 'r') as f:
    contents = json.load(f)

df_readme = pd.DataFrame(contents)

# detect any mention of copyright, (c), ©, or "all rights reserved"
pattern = re.compile(r"copyright|\(c\)|©|all rights reserved", re.IGNORECASE)

df_readme['has_copyright'] = df_readme['content'].fillna('').apply(lambda x: bool(pattern.search(x)))

# build languages df
df_langs = pd.DataFrame(langs)

# identify repos that mention Python in language_description
mask_python = df_langs['language_description'].str.contains('Python', case=False, na=False)
python_repos = set(df_langs[mask_python]['repo_name'])

# filter readmes to repos that do NOT use Python
mask_not_python = ~df_readme['sample_repo_name'].isin(python_repos)

subset = df_readme[mask_not_python]

if len(subset) == 0:
    proportion = None
else:
    proportion = subset['has_copyright'].mean()

result = {"proportion_non_python_readmes_with_copyright": proportion,
          "total_non_python_readmes": int(len(subset))}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_xH0VZaMyvJSHZ0z00OOzxC4K': 'file_storage/call_xH0VZaMyvJSHZ0z00OOzxC4K.json', 'var_call_ANhwcrC5xioFsXDrkOVIVWdQ': 'file_storage/call_ANhwcrC5xioFsXDrkOVIVWdQ.json'}

exec(code, env_args)
