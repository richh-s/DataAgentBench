code = """import json

# Load the repository list from the file
repo_data_path = var_functions.query_db:0
with open(repo_data_path, 'r') as f:
    repo_data = json.load(f)

repo_names = [item['repo_name'] for item in repo_data]
print(f"Total repositories found: {len(repo_names)}")

# Prepare the SQL query for commits
if len(repo_names) > 0:
    # Build the IN clause with placeholders
    placeholders = ', '.join([f"'{name}'" for name in repo_names[:400]])  # Limit to avoid query too long
    
    # The query will filter for:
    # - repos in our list with Shell and Apache-2.0
    # - subject exists (IS NOT NULL and not empty)
    # - subject length < 1000
    # - subject not starting with merge, update, or test (case-insensitive)
    sql_query = f"""
    SELECT COUNT(*) as commit_count
    FROM commits 
    WHERE repo_name IN ({placeholders})
    AND subject IS NOT NULL 
    AND subject != ''
    AND LENGTH(subject) < 1000
    AND LOWER(subject) NOT LIKE 'merge%'
    AND LOWER(subject) NOT LIKE 'update%'
    AND LOWER(subject) NOT LIKE 'test%'
    """
    
    print('__RESULT__:')
    print(json.dumps(sql_query))
else:
    print('__RESULT__:')
    print(json.dumps("No repositories found"))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
