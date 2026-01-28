code = """import json

# Get the file path from storage
file_path_var = 'var_functions.query_db:14'
file_path = locals()[file_path_var]

# Load the JSON data
with open(file_path, 'r') as f:
    repos_list = json.load(f)

# Extract just the repo names
repo_names = [repo['repo_name'] for repo in repos_list]

# Limit to first 100 to avoid query being too long
limited_repos = repo_names[:100]

# Format for SQL IN clause
formatted_repos = ', '.join([\"'\" + repo.replace(\"'\", \"''\") + \"'\" for repo in limited_repos])

print(\"__RESULT__:\")
print(json.dumps(formatted_repos))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
