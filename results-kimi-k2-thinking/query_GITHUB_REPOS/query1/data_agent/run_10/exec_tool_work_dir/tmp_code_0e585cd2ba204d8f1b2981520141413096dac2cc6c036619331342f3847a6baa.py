code = """# Get the full languages data
import json
import re

# Read the languages data file
with open('/root/tool_results/var_functions.query_db:8.json', 'r') as f:
    languages_data = json.load(f)

# Filter out repositories that use Python
python_repos = []
non_python_repos = []

for record in languages_data:
    repo_name = record['repo_name']
    lang_desc = record['language_description']
    
    # Check if Python is mentioned in the language description
    if 'Python' in lang_desc:
        python_repos.append(repo_name)
    else:
        non_python_repos.append(repo_name)

print('Total repositories: ' + str(len(languages_data)))
print('Python repositories: ' + str(len(python_repos)))
print('Non-Python repositories: ' + str(len(non_python_repos)))

# Print in required format
import json as js
print('__RESULT__:')
print(js.dumps(non_python_repos))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
