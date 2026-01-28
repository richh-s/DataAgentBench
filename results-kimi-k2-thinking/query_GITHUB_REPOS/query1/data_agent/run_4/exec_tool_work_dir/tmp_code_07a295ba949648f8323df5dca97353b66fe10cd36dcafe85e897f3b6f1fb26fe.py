code = """# Process the languages data to identify non-Python repositories
languages_data = locals()['var_functions.query_db:14']
if isinstance(languages_data, str):
    import json
    import os
    # Read from file if it's a string path
    file_path = languages_data
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            languages_data = json.load(f)
    else:
        # Try alternative path
        path = '/tmp/data_analyst_agent/' + file_path
        with open(path, 'r') as f:
            languages_data = json.load(f)

# Filter non-Python repositories
non_python_repos = []
for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    if 'python' not in lang_desc.lower():
        non_python_repos.append(repo_name)

print("__RESULT__:")
print(len(non_python_repos))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.execute_python:2': 'Sample data loaded', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': 38, 'var_functions.list_db:12': ['languages', 'repos', 'licenses'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'type': "<class 'str'>", 'is_string': True, 'value_short': 'file_storage/functions.query_db:14.json', 'file_exists': False}, 'var_functions.execute_python:20': {'status': 'success', 'total_repos': 3325634, 'sample': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}]}}

exec(code, env_args)
