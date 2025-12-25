code = """import json, re, pandas as pd

# Load large query results from JSON files if needed
contents_path = var_call_o7oTBbO7Yb7Xpd7lAAlILRAL
languages_records = var_call_F7qOtWbscC1zUmhNv8XDAaYO

with open(contents_path, 'r') as f:
    contents_records = json.load(f)

# Build DataFrames
contents_df = pd.DataFrame(contents_records)
languages_df = pd.DataFrame(languages_records)

# Filter repos that do NOT use Python (language_description does not contain 'Python')
no_python_lang = languages_df[~languages_df['language_description'].str.contains('Python', case=False, na=False)].copy()

# README files per repo
readme_df = contents_df[contents_df['sample_path'].str.lower() == 'readme.md'][['sample_repo_name','content']].copy()

# Join: keep only repos without Python that have a README
merged = pd.merge(no_python_lang, readme_df, left_on='repo_name', right_on='sample_repo_name', how='inner')

# Define a simple heuristic for copyright info
pattern = re.compile(r'copyright|\bc\s*\d{4}', re.IGNORECASE)

merged['has_copyright'] = merged['content'].fillna('').apply(lambda x: bool(pattern.search(x)))

# Compute proportion
if len(merged) == 0:
    proportion = None
else:
    proportion = merged['copyright'].mean() if 'copyright' in merged.columns else merged['has_copyright'].mean()

result = {
    'num_repos_no_python_with_readme': int(len(merged)),
    'num_with_copyright_info': int(merged['has_copyright'].sum()) if len(merged) > 0 else 0,
    'proportion': float(proportion) if proportion is not None else None
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_o7oTBbO7Yb7Xpd7lAAlILRAL': 'file_storage/call_o7oTBbO7Yb7Xpd7lAAlILRAL.json', 'var_call_F7qOtWbscC1zUmhNv8XDAaYO': 'file_storage/call_F7qOtWbscC1zUmhNv8XDAaYO.json'}

exec(code, env_args)
