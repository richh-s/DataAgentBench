code = """import json
import pandas as pd

with open(locals()['var_function-call-10151192167235551714'], 'r') as f:
    non_python_repo_names_str = json.load(f)

# The content is a string of comma-separated quoted repo names, convert it to a list
non_python_repo_names = [name.strip("' ") for name in non_python_repo_names_str.split(', ')]

with open(locals()['var_function-call-6054804810167290335'], 'r') as f:
    readme_contents = json.load(f)

readme_df = pd.DataFrame(readme_contents)

# Filter for READMEs from non-Python repositories
non_python_readmes = readme_df[readme_df['sample_repo_name'].isin(non_python_repo_names)]

if non_python_readmes.empty:
    print('__RESULT__:')
    print(json.dumps(0.0))
else:
    # Check for copyright information in the content
    copyright_count = non_python_readmes['content'].str.contains(r'copyright|Copyright|COPYRIGHT|\xc2\xa9', regex=True, na=False).sum()
    total_non_python_readmes = len(non_python_readmes)
    proportion = copyright_count / total_non_python_readmes if total_non_python_readmes > 0 else 0.0

    print('__RESULT__:')
    print(json.dumps(proportion))"""

env_args = {'var_function-call-949677833785488607': 'file_storage/function-call-949677833785488607.json', 'var_function-call-10151192167235551714': 'file_storage/function-call-10151192167235551714.json', 'var_function-call-6054804810167290335': 'file_storage/function-call-6054804810167290335.json'}

exec(code, env_args)
