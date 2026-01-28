code = """import re
import json

# Read the results from storage
try:
    non_python_repos = locals()['var_functions.query_db:14']
    print("Successfully accessed non_python_repos")
except Exception as e:
    print(f"Error accessing non_python_repos: {e}")
    non_python_repos = []

try:
    readme_files = locals()['var_functions.query_db:18']
    print("Successfully accessed readme_files")
except Exception as e:
    print(f"Error accessing readme_files: {e}")
    readme_files = []

print(f"Number of non-Python repos: {len(non_python_repos)}")
print(f"Number of README files: {len(readme_files)}")

# Show first few entries to inspect structure
if non_python_repos:
    print("First non-Python repo entry:", non_python_repos[0])

if readme_files:
    print("First README entry:", readme_files[0])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [{'total_non_python': '2774729'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
