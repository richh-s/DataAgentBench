code = """import json

# Load the repository names from the file
with open(locals()['var_function-call-7933397945210555376'], 'r') as f:
    repo_names_data = json.load(f)

# Extract repo_name values into a list
repo_names = [repo['repo_name'] for repo in repo_names_data]

# Create a SQL IN clause string
# Escape single quotes in repo names if any, though unlikely for GitHub repo names
escaped_repo_names = [name.replace("'", "''") for name in repo_names]
repo_names_in_clause = ", ".join(f"'{name}'" for name in escaped_repo_names)

# Construct the SQL query for DuckDB
# DuckDB uses standard SQL, so string length and LIKE are standard.
# Note: In DuckDB, LENGTH() counts characters not bytes.
sql_query = f"""
SELECT
    COUNT(message)
FROM
    commits
WHERE
    repo_name IN ({repo_names_in_clause}) AND
    message IS NOT NULL AND
    LENGTH(message) < 1000 AND
    NOT (LOWER(SUBSTRING(message, 1, 5)) = 'merge' OR
         LOWER(SUBSTRING(message, 1, 6)) = 'update' OR
         LOWER(SUBSTRING(message, 1, 4)) = 'test');
"""

print("__RESULT__:")
print(json.dumps(sql_query))"""

env_args = {'var_function-call-7933397945210555376': 'file_storage/function-call-7933397945210555376.json'}

exec(code, env_args)
