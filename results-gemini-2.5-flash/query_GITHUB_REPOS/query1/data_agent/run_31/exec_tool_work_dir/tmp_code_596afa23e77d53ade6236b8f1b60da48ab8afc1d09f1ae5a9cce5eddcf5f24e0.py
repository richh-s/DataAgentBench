code = """import json
import pandas as pd

non_python_repos_file_path = locals()['var_function-call-4617459576807609499']
readme_contents_file_path = locals()['var_function-call-18260989266471861853']

with open(non_python_repos_file_path, 'r') as f:
    non_python_repos = json.load(f)

with open(readme_contents_file_path, 'r') as f:
    readme_contents_data = json.load(f)

non_python_repos_set = set(non_python_repos)

readme_df = pd.DataFrame(readme_contents_data)

# Filter README files for non-Python repositories
non_python_readme_df = readme_df[readme_df['sample_repo_name'].isin(non_python_repos_set)]

total_non_python_readmes = len(non_python_readme_df)

# Check for copyright information (case-insensitive and common patterns)
copyright_count = non_python_readme_df['content'].str.contains('(copyright|©|\(c\))', case=False, na=False).sum()

if total_non_python_readmes > 0:
    proportion = copyright_count / total_non_python_readmes
else:
    proportion = 0

print('__RESULT__:')
print(json.dumps({'proportion_with_copyright': proportion}))"""

env_args = {'var_function-call-341325014639098221': 'file_storage/function-call-341325014639098221.json', 'var_function-call-6822701452639428232': 'file_storage/function-call-6822701452639428232.json', 'var_function-call-4617459576807609499': 'file_storage/function-call-4617459576807609499.json', 'var_function-call-18260989266471861853': 'file_storage/function-call-18260989266471861853.json'}

exec(code, env_args)
