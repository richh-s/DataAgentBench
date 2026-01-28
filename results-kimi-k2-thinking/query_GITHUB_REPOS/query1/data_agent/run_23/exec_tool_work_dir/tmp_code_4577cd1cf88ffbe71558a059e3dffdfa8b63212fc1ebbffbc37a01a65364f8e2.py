code = """import json
import os

# Read the file path from the storage
file_path = locals()['var_functions.query_db:2']
print("File path:", file_path)

# Read the actual data from the file
with open(file_path, 'r') as f:
    languages_data = json.load(f)

print("Number of repos:", len(languages_data))
print("First item:", languages_data[0])

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

result = {"total_repos": len(languages_data), "non_python_count": len(non_python_repos), "example_repos": non_python_repos[:5]}

# Print result in the required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'data_type': "<class 'str'>"}}

exec(code, env_args)
