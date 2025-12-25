code = """import pandas as pd
import json

non_python_repos_path = locals()['var_function-call-748244518148299778']
all_readmes_path = locals()['var_function-call-16004592168912845592']

with open(non_python_repos_path, 'r') as f:
    non_python_repos_data = json.load(f)

with open(all_readmes_path, 'r') as f:
    all_readmes_data = json.load(f)

non_python_repos_df = pd.DataFrame(non_python_repos_data)
all_readmes_df = pd.DataFrame(all_readmes_data)

# Filter READMEs for non-Python repositories
filtered_readmes_df = all_readmes_df[all_readmes_df['sample_repo_name'].isin(non_python_repos_df['repo_name'])]

# Check for copyright information
filtered_readmes_df['has_copyright'] = filtered_readmes_df['content'].apply(lambda x: 'copyright' in str(x).lower())

total_non_python_readmes = len(filtered_readmes_df)
readmes_with_copyright = filtered_readmes_df['has_copyright'].sum()

if total_non_python_readmes > 0:
    proportion = readmes_with_copyright / total_non_python_readmes
else:
    proportion = 0

print('__RESULT__:')
print(json.dumps(proportion))"""

env_args = {'var_function-call-748244518148299778': 'file_storage/function-call-748244518148299778.json', 'var_function-call-16004592168912845592': 'file_storage/function-call-16004592168912845592.json'}

exec(code, env_args)
