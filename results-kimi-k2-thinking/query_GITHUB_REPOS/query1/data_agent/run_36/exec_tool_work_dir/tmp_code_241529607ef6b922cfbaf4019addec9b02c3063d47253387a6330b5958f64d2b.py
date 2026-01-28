code = """import json
import re

# Count Python vs non-Python repos
python_repos = 0
non_python_repos = 0
python_repo_names = set()
non_python_repo_names = set()

# Process languages data
lang_file = 'var_functions.query_db:10'
with open(lang_file, 'r') as f:
    languages_data = json.load(f)

for item in languages_data:
    repo_name = item.get('repo_name', '')
    lang_desc = item.get('language_description', '').lower()
    
    if 'python' in lang_desc:
        python_repos += 1
        if repo_name:
            python_repo_names.add(repo_name)
    else:
        non_python_repos += 1
        if repo_name:
            non_python_repo_names.add(repo_name)

# Save for later use
with open('/tmp/language_analysis.json', 'w') as f:
    json.dump({
        'python_repos': python_repos,
        'non_python_repos': non_python_repos,
        'python_repo_names': list(python_repo_names),
        'non_python_repo_names': list(non_python_repo_names)
    }, f)

result = {
    'total_repos': len(languages_data),
    'python_repos': python_repos,
    'non_python_repos': non_python_repos,
    'sample_python_repos': list(python_repo_names)[:10],
    'sample_non_python_repos': list(non_python_repo_names)[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'total_repos': '3325634'}]}

exec(code, env_args)
