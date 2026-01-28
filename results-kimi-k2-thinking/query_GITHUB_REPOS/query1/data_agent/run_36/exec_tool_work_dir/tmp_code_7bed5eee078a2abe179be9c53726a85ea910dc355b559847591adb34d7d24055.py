code = """import json

langs_data_path = var_functions.query_db:10
readme_data_path = var_functions.query_db:16

with open(langs_data_path, 'r') as f:
    languages_data = json.load(f)

with open(readme_data_path, 'r') as f:
    readme_data = json.load(f)

python_repos = set()
all_repos = set()

for item in languages_data:
    repo_name = item.get('repo_name', '')
    if repo_name:
        all_repos.add(repo_name)
        lang_desc = item.get('language_description', '').lower()
        if 'python' in lang_desc:
            python_repos.add(repo_name)

non_python_repos = all_repos - python_repos

# Find README files for non-Python repos
non_python_readmes = []
for readme in readme_data:
    repo_name = readme.get('sample_repo_name', '')
    if repo_name in non_python_repos:
        non_python_readmes.append(readme)

total_non_python_readmes = len(non_python_readmes)

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(all_repos),
    'python_repos': len(python_repos),
    'non_python_repos': len(non_python_repos),
    'non_python_readmes': total_non_python_readmes
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'total_repos': '3325634'}], 'var_functions.query_db:28': [{'count': '550905'}]}

exec(code, env_args)
