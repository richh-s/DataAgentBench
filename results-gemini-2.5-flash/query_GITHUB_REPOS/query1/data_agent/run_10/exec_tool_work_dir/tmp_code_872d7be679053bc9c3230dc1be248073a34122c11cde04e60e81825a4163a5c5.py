code = """import pandas as pd
import json

non_python_repos_path = locals()['var_function-call-16727474972992641538']
readme_contents_path = locals()['var_function-call-15228303712561524877']

with open(non_python_repos_path, 'r') as f:
    non_python_repos = json.load(f)

with open(readme_contents_path, 'r') as f:
    readme_contents = json.load(f)

non_python_repos_df = pd.DataFrame(non_python_repos)
readme_contents_df = pd.DataFrame(readme_contents)

merged_df = pd.merge(non_python_repos_df, readme_contents_df, left_on='repo_name', right_on='sample_repo_name', how='inner')

total_non_python_readmes = len(merged_df)

copyright_keywords = ["copyright", "Copyright", "©"]
copyright_count = 0

for content in merged_df['content']:
    if any(keyword in content for keyword in copyright_keywords):
        copyright_count += 1

if total_non_python_readmes > 0:
    proportion = copyright_count / total_non_python_readmes
else:
    proportion = 0

print("__RESULT__:")
print(json.dumps(proportion))"""

env_args = {'var_function-call-16727474972992641538': 'file_storage/function-call-16727474972992641538.json', 'var_function-call-15228303712561524877': 'file_storage/function-call-15228303712561524877.json'}

exec(code, env_args)
