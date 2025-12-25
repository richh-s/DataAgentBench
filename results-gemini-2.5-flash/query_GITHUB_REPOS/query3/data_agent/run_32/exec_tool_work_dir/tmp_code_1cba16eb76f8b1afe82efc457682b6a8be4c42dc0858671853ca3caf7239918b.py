code = """import json
with open(locals()['var_function-call-17512995714229407507'], 'r') as f:
    repo_names_data = json.load(f)
repo_names = [repo['repo_name'] for repo in repo_names_data]

# Escape single quotes in repo_names and wrap each in single quotes for the IN clause
# This will create a string like "'repo1', 'repo2', 'repo3'"
repo_names_in_clause = ", ".join([f"'{name.replace("'", "''")}'" for name in repo_names])

# Construct the SQL query using string formatting, not f-string for the main query structure
# This avoids potential issues with nested f-strings or very long f-string literals.
sql_query = """
SELECT COUNT(*)
FROM commits
WHERE repo_name IN ({repo_names_in_clause})
  AND message IS NOT NULL
  AND LENGTH(message) < 1000
  AND LOWER(message) NOT LIKE 'merge%'
  AND LOWER(message) NOT LIKE 'update%'
  AND LOWER(message) NOT LIKE 'test%';
""".format(repo_names_in_clause=repo_names_in_clause)

print("__RESULT__:")
print(json.dumps(sql_query))"""

env_args = {'var_function-call-17512995714229407507': 'file_storage/function-call-17512995714229407507.json'}

exec(code, env_args)
