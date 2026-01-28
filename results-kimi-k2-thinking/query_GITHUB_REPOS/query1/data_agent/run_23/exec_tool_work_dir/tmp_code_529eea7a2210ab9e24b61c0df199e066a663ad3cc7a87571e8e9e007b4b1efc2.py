code = """import json

# Read the languages data from the previous query result
languages_data = locals()['var_functions.query_db:2']

# Function to check if Python is present in a language description
def has_python(lang_desc):
    if not lang_desc:
        return False
    return 'Python' in lang_desc or 'python' in lang_desc

# Get repos that do NOT use Python
non_python_repos = []
for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    if not has_python(lang_desc):
        non_python_repos.append(repo_name)

# Print result in the required format
__RESULT__:
print(json.dumps({"non_python_count": len(non_python_repos), "example_repos": non_python_repos[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
