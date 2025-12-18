code = """import pandas as pd
import json

non_python_repos_file = locals()['var_function-call-11136162337862174779']
readme_contents_file = locals()['var_function-call-15718315968014468951']

with open(non_python_repos_file, 'r') as f:
    non_python_repos_data = json.load(f)

with open(readme_contents_file, 'r') as f:
    readme_contents_data = json.load(f)

non_python_repos_df = pd.DataFrame(non_python_repos_data)
readme_contents_df = pd.DataFrame(readme_contents_data)

non_python_repo_names = non_python_repos_df['repo_name'].tolist()

filtered_readmes = readme_contents_df[readme_contents_df['sample_repo_name'].isin(non_python_repo_names)]

def contains_copyright(text):
    if isinstance(text, str):
        return 'copyright' in text.lower()
    return False

filtered_readmes['has_copyright'] = filtered_readmes['content'].apply(contains_copyright)

proportion_with_copyright = filtered_readmes['has_copyright'].sum() / len(filtered_readmes)

print('__RESULT__:')
print(json.dumps(proportion_with_copyright))"""

env_args = {'var_function-call-11136162337862174779': 'file_storage/function-call-11136162337862174779.json', 'var_function-call-15718315968014468951': 'file_storage/function-call-15718315968014468951.json'}

exec(code, env_args)
