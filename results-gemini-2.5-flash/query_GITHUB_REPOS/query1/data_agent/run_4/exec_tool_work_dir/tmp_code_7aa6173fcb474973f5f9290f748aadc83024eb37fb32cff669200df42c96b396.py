code = """import json
import pandas as pd

non_python_repos = json.load(open(locals()['var_function-call-6945448570652704172'], 'r'))
readme_contents = json.load(open(locals()['var_function-call-6760363720540279938'], 'r'))

df_non_python_repos = pd.DataFrame(non_python_repos, columns=['repo_name'])
df_readme_contents = pd.DataFrame(readme_contents)

df_merged = pd.merge(df_non_python_repos, df_readme_contents, left_on='repo_name', right_on='sample_repo_name', how='inner')

copyright_count = 0
total_non_python_readme = len(df_merged)

for index, row in df_merged.iterrows():
    if 'content' in row and isinstance(row['content'], str):
        if 'copyright' in row['content'].lower() or '©' in row['content']:
            copyright_count += 1

if total_non_python_readme > 0:
    proportion = copyright_count / total_non_python_readme
else:
    proportion = 0

print('__RESULT__:')
print(json.dumps({'proportion': proportion}))"""

env_args = {'var_function-call-7467599405428873075': 'file_storage/function-call-7467599405428873075.json', 'var_function-call-6945448570652704172': 'file_storage/function-call-6945448570652704172.json', 'var_function-call-6760363720540279938': 'file_storage/function-call-6760363720540279938.json'}

exec(code, env_args)
