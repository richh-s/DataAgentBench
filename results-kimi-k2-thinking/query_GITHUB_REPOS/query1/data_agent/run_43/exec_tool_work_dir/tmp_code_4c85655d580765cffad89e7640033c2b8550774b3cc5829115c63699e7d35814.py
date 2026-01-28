code = """import json
import os

# Determine which variable holds the languages file path
# The query was executed with id 'functions.query_db:2', but we need to see what variable name is used.
# The storage key is var_functions.query_db:2
languages_file = locals().get('var_functions.query_db:2')
if not languages_file:
    # maybe it's var_functions.query_db:0
    languages_file = locals().get('var_functions.query_db:0')
print('languages_file var:', languages_file)
# It's likely a string path
if isinstance(languages_file, str):
    with open(languages_file, 'r') as f:
        languages = json.load(f)
else:
    # It's directly the list
    languages = languages_file

print('Number of language rows:', len(languages))
# Inspect a sample
print('Sample row:', languages[0])

# Determine repos that use Python
python_repos = set()
all_repos = set()
for row in languages:
    repo = row['repo_name']
    all_repos.add(repo)
    desc = row.get('language_description', '')
    # Case-insensitive check for 'Python'
    if 'python' in desc.lower():
        python_repos.add(repo)

print('Total repos:', len(all_repos))
print('Python repos:', len(python_repos))
non_python_repos = all_repos - python_repos
print('Non-Python repos:', len(non_python_repos))

# Save non_python_repos list for later use
result = {'non_python_repos': list(non_python_repos)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
