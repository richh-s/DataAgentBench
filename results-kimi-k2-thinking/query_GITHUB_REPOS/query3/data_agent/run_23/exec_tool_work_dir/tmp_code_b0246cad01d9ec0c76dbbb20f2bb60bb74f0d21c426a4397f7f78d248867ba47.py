code = """import json
result_file = locals()['var_functions.execute_python:10']
print(f"Loading repository names from: {result_file}")
with open(result_file, 'r') as f:
    data = json.load(f)

repo_names = data['repo_names']
print(f"Total repositories: {len(repo_names)}")
print(f"First 5 repositories: {repo_names[:5]}")

# Build the query for DuckDB - check if message exists, < 1000 chars, and doesn't start with merge/update/test
query = """
SELECT COUNT(*) as commit_count
FROM artifacts_database.commits
WHERE repo_name IN (
"""

# Add all repo names (we need to batch this if there are too many)
quoted_repos = [f'"{repo}"' for repo in repo_names]
query += ", ".join(quoted_repos)
query += ")"
query += """
AND message IS NOT NULL 
AND LENGTH(message) < 1000
AND LOWER(message) NOT LIKE 'merge%'
AND LOWER(message) NOT LIKE 'update%'
AND LOWER(message) NOT LIKE 'test%'
"""

print("Query built successfully")
result = {
    'query': query,
    'repo_count': len(repo_names)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json'}

exec(code, env_args)
