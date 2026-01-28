code = """import json

langs_path = 'var_functions.query_db:10'
readme_path = 'var_functions.query_db:16'

with open(langs_path, 'r') as f:
    languages_data = json.load(f)

with open(readme_path, 'r') as f:
    readme_data = json.load(f)

total_langs = len(languages_data)
total_readmes = len(readme_data)

python_repos = set()
all_repos = set()

for item in languages_data[:10000]:
    repo_name = item.get('repo_name', '')
    if repo_name:
        all_repos.add(repo_name)
        lang = item.get('language_description', '').lower()
        if 'python' in lang:
            python_repos.add(repo_name)

result = {
    'total_processed': total_langs,
    'python_repos': len(python_repos),
    'non_python_repos': len(all_repos) - len(python_repos),
    'readmes_found': total_readmes
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'total_repos': '3325634'}], 'var_functions.query_db:28': [{'count': '550905'}]}

exec(code, env_args)
