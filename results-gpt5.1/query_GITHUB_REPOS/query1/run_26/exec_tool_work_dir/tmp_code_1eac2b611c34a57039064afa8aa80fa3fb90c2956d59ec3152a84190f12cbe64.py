code = """import json, re, pandas as pd

readmes_path = var_call_0m1SfS37lKB7R2jper2u3l0L
langs_path = var_call_JBTQhoFcCQgrQhqpu1SZIssP

with open(readmes_path) as f:
    readmes = json.load(f)
with open(langs_path) as f:
    langs = json.load(f)

readme_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)

languages_no_py = langs_df[~langs_df['language_description'].str.contains('Python', case=False, na=False)][['repo_name']].drop_duplicates()

readme_df = readme_df.rename(columns={'sample_repo_name': 'repo_name'})

merged = pd.merge(readme_df, languages_no_py, on='repo_name', how='inner')

pattern = re.compile(r'copyright|\bcopyright\b|\u00a9', re.IGNORECASE)

merged['has_copyright'] = merged['content'].fillna('').apply(lambda x: bool(pattern.search(x)))

if len(merged) == 0:
    proportion = None
else:
    proportion = merged['has_copyright'].mean()

result = {
    'total_non_python_repos_with_readme': int(len(merged)),
    'proportion_with_copyright': float(proportion) if proportion is not None else None
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_0m1SfS37lKB7R2jper2u3l0L': 'file_storage/call_0m1SfS37lKB7R2jper2u3l0L.json', 'var_call_JBTQhoFcCQgrQhqpu1SZIssP': 'file_storage/call_JBTQhoFcCQgrQhqpu1SZIssP.json', 'var_call_hKsTPpyReP4u8o6cABs0XvgH': 'file_storage/call_hKsTPpyReP4u8o6cABs0XvgH.json', 'var_call_iOL6yohIymx5nTHMT8dlmrRO': 'file_storage/call_iOL6yohIymx5nTHMT8dlmrRO.json', 'var_call_WuyYqbUmgdOOHARvQj9Xttwj': ['commits', 'contents', 'files'], 'var_call_HdqUTLvdcdgqDCV2c75P58ro': ['languages', 'repos', 'licenses']}

exec(code, env_args)
