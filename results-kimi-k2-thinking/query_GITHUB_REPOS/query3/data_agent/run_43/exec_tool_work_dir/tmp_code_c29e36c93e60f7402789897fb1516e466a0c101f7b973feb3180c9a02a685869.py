code = """import json

# Get the file path from storage
repo_data_file = locals()['var_functions.query_db:8']

# Read the repository data
with open(repo_data_file, 'r') as f:
    repo_data = json.load(f)

print(f"Total repositories loaded: {len(repo_data)}")

# Extract repo names
repo_names = [item['repo_name'] for item in repo_data]

# Build SQL query with first 200 repos to avoid query size limits
if len(repo_names) > 0:
    repo_list = repo_names[:200]
    # Create the IN list manually to avoid f-string issues
    placeholders = ''
    for i, name in enumerate(repo_list):
        if i > 0:
            placeholders = placeholders + ', '
        placeholders = placeholders + "'" + name + "'"
    
    sql_parts = [
        'SELECT COUNT(*) as commit_count FROM commits',
        'WHERE repo_name IN (',
        placeholders,
        ') AND subject IS NOT NULL AND subject != \"\" AND LENGTH(subject) < 1000',
        "AND LOWER(subject) NOT LIKE 'merge%'",
        "AND LOWER(subject) NOT LIKE 'update%'", 
        "AND LOWER(subject) NOT LIKE 'test%'"
    ]
    
    sql_query = ' '.join(sql_parts)
    
    print('__RESULT__:')
    print(sql_query)
else:
    print('__RESULT__:')
    print('No repositories found')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
