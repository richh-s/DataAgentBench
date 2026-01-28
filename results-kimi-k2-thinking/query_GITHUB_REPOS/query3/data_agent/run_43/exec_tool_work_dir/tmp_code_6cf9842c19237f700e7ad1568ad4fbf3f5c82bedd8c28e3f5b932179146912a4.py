code = """import json

# Load limited repository list from file
repo_data_path = var_functions.query_db:8
with open(repo_data_path, 'r') as f:
    repo_data = json.load(f)

repo_names = [item['repo_name'] for item in repo_data]
print(f"Total repositories found: {len(repo_names)}")

# Build list of repos for IN clause (limit to avoid query too long)
if len(repo_names) > 0:
    repo_list_str = ""  
    for i, repo in enumerate(repo_names[:200]):
        if i > 0:
            repo_list_str += ", "
        repo_list_str += "'" + repo + "'"
    
    sql_query = "SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN (" + repo_list_str + ") AND subject IS NOT NULL AND subject != '' AND LENGTH(subject) < 1000 AND LOWER(subject) NOT LIKE 'merge%' AND LOWER(subject) NOT LIKE 'update%' AND LOWER(subject) NOT LIKE 'test%'"
    
    print('__RESULT__:')
    print(json.dumps(sql_query))
else:
    print('__RESULT__:')
    print(json.dumps("No repositories found"))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
