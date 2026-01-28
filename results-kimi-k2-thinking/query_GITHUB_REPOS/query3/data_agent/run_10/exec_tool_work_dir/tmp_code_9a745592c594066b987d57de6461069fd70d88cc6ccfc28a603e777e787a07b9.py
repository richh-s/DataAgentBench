code = """import json

# Read the repo names from the file
with open(locals()['var_functions.execute_python:20'], 'r') as f:
    repo_names = json.load(f)

# Build the SQL query with the list of repos
repo_list = ', '.join([f"'{repo}'" for repo in repo_names])
query = f"""
SELECT COUNT(*) as commit_count 
FROM commits 
WHERE repo_name IN ({repo_list})
AND message IS NOT NULL 
AND LENGTH(message) < 1000 
AND LOWER(SUBSTR(message, 1, 5)) NOT IN ('merge', 'updat', 'test')
"""

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['commits', 'contents', 'files'], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json'}

exec(code, env_args)
