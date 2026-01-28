code = """import json
import os

# Read the full result from the query
result_file = var_functions.query_db:8
print(f"Result file path: {result_file}")

# Open and read the JSON file
with open(result_file, 'r') as f:
    repo_data = json.load(f)

# Extract repo_names
repo_names = [item['repo_name'] for item in repo_data]
print(f"Number of repos: {len(repo_names)}")
print(f"First 10 repos: {repo_names[:10]}")

# Create the SQL query
repo_list_str = ', '.join([f"'{name}'" for name in repo_names])
query = f"""
SELECT COUNT(*) as commit_count 
FROM commits 
WHERE repo_name IN ({repo_list_str})
  AND message IS NOT NULL 
  AND LENGTH(message) < 1000 
  AND LOWER(message) NOT LIKE 'merge%' 
  AND LOWER(message) NOT LIKE 'update%' 
  AND LOWER(message) NOT LIKE 'test%'
"""

print(f"Generated query length: {len(query)} characters")
print("Query preview:", query[:500] + "...")

# Store query for next step
result = {
    'repo_count': len(repo_names),
    'repos_sample': repo_names[:10],
    'query': query
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': [{'commit_count': '15016'}], 'var_functions.query_db:7': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
