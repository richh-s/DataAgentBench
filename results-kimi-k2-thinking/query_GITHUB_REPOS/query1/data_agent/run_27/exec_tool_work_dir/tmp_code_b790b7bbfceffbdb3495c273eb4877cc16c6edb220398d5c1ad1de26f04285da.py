code = """import json
import re

# Read the languages data from the file
with open('/tmp/tmp3tje4s7b.json', 'r') as f:
    languages_data = json.load(f)

# Function to check if Python is mentioned in the language description
def contains_python(lang_desc):
    return 'Python' in lang_desc

# Count Python vs non-Python repos
python_repos = []
non_python_repos = []

for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    if contains_python(lang_desc):
        python_repos.append(repo_name)
    else:
        non_python_repos.append(repo_name)

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(languages_data),
    'python_repos_count': len(python_repos),
    'non_python_repos_count': len(non_python_repos),
    'python_repos_sample': python_repos[:10],
    'non_python_repos_sample': non_python_repos[:10]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
