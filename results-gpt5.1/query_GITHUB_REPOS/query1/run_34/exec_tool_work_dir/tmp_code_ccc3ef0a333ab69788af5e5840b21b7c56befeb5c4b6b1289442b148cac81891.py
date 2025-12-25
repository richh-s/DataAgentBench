code = """import json, pandas as pd
contents_path = var_call_8NHBNJWb15ScuOyodCcpNP9B
langs = var_call_dwalPEZ4NpSHEccsW5zGiDf1
with open(contents_path) as f:
    contents = json.load(f)
contents_df = pd.DataFrame(contents)
readmes = contents_df[['repo_name','content']]
langs_df = pd.DataFrame(langs)
no_py = langs_df[~langs_df['language_description'].str.contains('Python', case=False, na=False)][['repo_name']]
merged = pd.merge(no_py, readmes, on='repo_name', how='inner')
merged['has_copyright'] = merged['content'].str.contains('copyright', case=False, na=False)
result = {
  'num_no_python_with_readme': int(len(merged)),
  'num_with_copyright': int(merged['has_copyright'].sum()),
  'proportion': (float(merged['has_copyright'].mean()) if len(merged)>0 else None)
}
import json as _json
result_json = _json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_8NHBNJWb15ScuOyodCcpNP9B': 'file_storage/call_8NHBNJWb15ScuOyodCcpNP9B.json', 'var_call_dwalPEZ4NpSHEccsW5zGiDf1': 'file_storage/call_dwalPEZ4NpSHEccsW5zGiDf1.json', 'var_call_LQeb8OB4uxrE4tN7PrsZqrcu': 'file_storage/call_LQeb8OB4uxrE4tN7PrsZqrcu.json'}

exec(code, env_args)
