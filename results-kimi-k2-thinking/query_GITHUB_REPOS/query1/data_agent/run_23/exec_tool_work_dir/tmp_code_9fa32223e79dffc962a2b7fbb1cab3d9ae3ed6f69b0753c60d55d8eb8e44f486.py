code = """import json

# Get the languages data
languages_file = locals()['var_functions.query_db:2']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Create a set of non-Python repos
non_python_repos = set()
python_repos = set()

for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item.get('language_description', '') or ''
    
    # Check if Python is mentioned
    has_python = 'python' in lang_desc.lower()
    
    if has_python:
        python_repos.add(repo_name)
    else:
        non_python_repos.add(repo_name)

print(f"Total repos: {len(languages_data)}")
print(f"Python repos: {len(python_repos)}")
print(f"Non-Python repos: {len(non_python_repos)}")

# Store for later use
result = {
    "total_repos": len(languages_data),
    "python_repos": len(python_repos),
    "non_python_repos": len(non_python_repos)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'data_type': "<class 'str'>"}, 'var_functions.execute_python:14': {'total_repos': 3325634, 'non_python_count': 2774729, 'example_repos': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
