code = """import json
import re

# Read the languages data from the file
with open('/storage/emulated/0/Download/result_2.json', 'r') as f:
    languages_data = json.load(f)

# Function to check if Python is present in a language description
def has_python(lang_desc):
    if not lang_desc:
        return False
    # Check if 'Python' appears in the description
    return 'Python' in lang_desc or 'python' in lang_desc

# Get repos that do NOT use Python
non_python_repos = []
for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    if not has_python(lang_desc):
        non_python_repos.append(repo_name)

print(f"Total repos: {len(languages_data)}")
print(f"Non-Python repos: {len(non_python_repos)}")

# Now check for README.md files in these repos
# First, let's query the contents table for README.md files from non-python repos
import sqlite3

# Let's create a query to get README.md content for non-Python repos
# We'll need to query the artifacts_database for this
query_vars = {
    'non_python_repos': non_python_repos
}

# To check the result format
__RESULT__:
print(json.dumps({"non_python_count": len(non_python_repos), "example_repos": non_python_repos[:10]}))
----END PRINT FORMAT----"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
