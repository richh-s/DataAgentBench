code = """import json

# Read the repo names from the file
with open(locals()['var_functions.execute_python:20'], 'r') as f:
    repo_names = json.load(f)

# Let's try a different approach - directly query the commits table
# with a join to the metadata database tables

query = """
SELECT COUNT(*) as commit_count 
FROM commits c
INNER JOIN (
  SELECT l.repo_name 
  FROM metadata_database.languages l 
  INNER JOIN metadata_database.licenses lic ON l.repo_name = lic.repo_name 
  WHERE l.language_description LIKE '%Shell%' 
  AND lic.license = 'apache-2.0'
) r ON c.repo_name = r.repo_name
WHERE c.message IS NOT NULL 
AND LENGTH(c.message) < 1000 
AND LOWER(SUBSTR(c.message, 1, 5)) NOT IN ('merge', 'updat', 'test')
"""

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['commits', 'contents', 'files'], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:26': 114972}

exec(code, env_args)
