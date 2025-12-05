code = """import json, pandas as pd
readmes_exact_file = var_call_MHEKyHqPsY7gcgKG85sqyHsJ
langs_file = var_call_zanbOg8j8Z0NOlWFKceblIHB
readmes_like_file = var_call_Pq2dHDyTT6yKXgXrd2qotMVS

with open(readmes_exact_file) as f:
    readmes_exact = json.load(f)
with open(langs_file) as f:
    langs = json.load(f)
with open(readmes_like_file) as f:
    readmes_like = json.load(f)

# Use exact README.md matches
df_readme = pd.DataFrame(readmes_exact)
# Drop rows with null content
df_readme = df_readme.dropna(subset=['content'])

# Languages
df_langs = pd.DataFrame(langs)
# Determine repos that use Python
uses_python = df_langs[df_langs['language_description'].str.contains('Python', case=False, na=False)]['repo_name'].unique()
uses_python_set = set(uses_python)

# Restrict to repos that do NOT use Python
df_readme['has_python'] = df_readme['repo_name'].isin(uses_python_set)
non_py_readmes = df_readme[~df_readme['has_python']].copy()

# Copyright detection heuristic
patterns = ['copyright', '©', 'copr.']
content_lower = non_py_readmes['content'].str.lower()
mask = content_lower.str.contains('|'.join(patterns), na=False)
non_py_readmes['has_copyright'] = mask

total = int(len(non_py_readmes))
copyright_count = int(non_py_readmes['copyright'].sum()) if 'copyright' in non_py_readmes.columns else int(mask.sum())
prop = float(copyright_count) / total if total > 0 else None

result = {
  'total_non_python_readmes': total,
  'non_python_readmes_with_copyright': copyright_count,
  'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MHEKyHqPsY7gcgKG85sqyHsJ': 'file_storage/call_MHEKyHqPsY7gcgKG85sqyHsJ.json', 'var_call_zanbOg8j8Z0NOlWFKceblIHB': 'file_storage/call_zanbOg8j8Z0NOlWFKceblIHB.json', 'var_call_eiMBddqLl6nYgUBRjUNsh1I5': 'file_storage/call_eiMBddqLl6nYgUBRjUNsh1I5.json', 'var_call_Pq2dHDyTT6yKXgXrd2qotMVS': 'file_storage/call_Pq2dHDyTT6yKXgXrd2qotMVS.json'}

exec(code, env_args)
