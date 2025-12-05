code = """import json, pandas as pd

readmes_path = var_call_sB9WIjPKTJnUoXOeHiLqaoWp
langs_path = var_call_lTQcNTn5lpSwP7eYO5O7IGuQ

with open(readmes_path) as f:
    readmes = json.load(f)
with open(langs_path) as f:
    langs = json.load(f)

readmes_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)

langs_df['has_python'] = langs_df['language_description'].str.contains('Python', case=False, na=False)

non_py_repos = langs_df.loc[~langs_df['has_python'], 'repo_name'].unique()

readmes_df = readmes_df.dropna(subset=['content'])

non_py_readmes = readmes_df[readmes_df['repo_name'].isin(non_py_repos)].copy()

patterns = ['copyright', 'all rights reserved', '\u00a9', '(c)']
pat = '|'.join(patterns)

non_py_readmes['has_copyright'] = non_py_readmes['content'].str.contains(pat, case=False, na=False)

total = int(len(non_py_readmes))
with_c = int(non_py_readmes['copyright'].sum()) if 'copyright' in non_py_readmes.columns else int(non_py_readmes['has_copyright'].sum())

prop = with_c / total if total > 0 else None

result = {
  'total_non_python_readmes': total,
  'with_copyright': with_c,
  'proportion': prop
}

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_sB9WIjPKTJnUoXOeHiLqaoWp': 'file_storage/call_sB9WIjPKTJnUoXOeHiLqaoWp.json', 'var_call_lTQcNTn5lpSwP7eYO5O7IGuQ': 'file_storage/call_lTQcNTn5lpSwP7eYO5O7IGuQ.json', 'var_call_0WYLamofsMTqKs81TPeTmsBU': 'file_storage/call_0WYLamofsMTqKs81TPeTmsBU.json', 'var_call_CZvkGXzOH2SFsLzAHsL11tca': 'file_storage/call_CZvkGXzOH2SFsLzAHsL11tca.json'}

exec(code, env_args)
