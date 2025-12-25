code = """import json, pandas as pd

readme_meta_path = var_call_arljmdkJ3JVVJr6ahmIacQXF
langs_path = var_call_rHIrFsR7VO6tARfC70ZPJqWd
readme_contents_path = var_call_wIBASnvsXuPwXucemnUc6SbH

with open(readme_meta_path) as f:
    readme_meta = json.load(f)
with open(langs_path) as f:
    langs = json.load(f)
with open(readme_contents_path) as f:
    readme_contents = json.load(f)

readme_df = pd.DataFrame(readme_meta)
langs_df = pd.DataFrame(langs)
contents_df = pd.DataFrame(readme_contents)

joined = readme_df.merge(langs_df, left_on='sample_repo_name', right_on='repo_name', how='left')
non_python = joined[~joined['language_description'].str.contains('Python', case=False, na=False)].copy()

non_python = non_python.merge(contents_df, on='id', how='left')

patterns = ['copyright', '©', '(c)']
mask = non_python['content'].str.contains('|'.join(patterns), case=False, na=False)

count_with = int(mask.sum())
total = int(len(non_python))
prop = count_with / total if total else None

result = {
  'total_non_python_readmes': total,
  'with_copyright_info': count_with,
  'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_arljmdkJ3JVVJr6ahmIacQXF': 'file_storage/call_arljmdkJ3JVVJr6ahmIacQXF.json', 'var_call_rHIrFsR7VO6tARfC70ZPJqWd': 'file_storage/call_rHIrFsR7VO6tARfC70ZPJqWd.json', 'var_call_wIBASnvsXuPwXucemnUc6SbH': 'file_storage/call_wIBASnvsXuPwXucemnUc6SbH.json'}

exec(code, env_args)
