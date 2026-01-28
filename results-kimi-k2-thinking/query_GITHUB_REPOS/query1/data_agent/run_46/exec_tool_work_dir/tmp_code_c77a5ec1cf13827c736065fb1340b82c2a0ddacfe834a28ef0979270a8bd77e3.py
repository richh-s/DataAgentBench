code = """import json
import re

# Read the languages data
with open('/tmp/tmpq6g8q7wk.json', 'r') as f:
    languages_data = json.load(f)

# Let's see how many records we have and check for Python
print(f"Total repositories in languages table: {len(languages_data)}")

# Check for Python in language descriptions
python_repos = []
non_python_repos = []

for repo in languages_data:
    lang_desc = repo['language_description'].lower()
    if 'python' in lang_desc:
        python_repos.append(repo['repo_name'])
    else:
        non_python_repos.append(repo['repo_name'])

print(f"Repos with Python: {len(python_repos)}")
print(f"Repos without Python: {len(non_python_repos)}")

# Show a few examples
print("\nFirst 5 non-Python repos:")
for repo in non_python_repos[:5]:
    print(f"  {repo}")

print("\nFirst 5 Python repos:")
for repo in python_repos[:5]:
    print(f"  {repo}")

# Store the non_python_repos list for later use
result = {
    "non_python_repos": non_python_repos,
    "python_repos": python_repos,
    "total_repos": len(languages_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
