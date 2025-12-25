code = """import pandas as pd
import json

swift_repos_path = locals()['var_function-call-17635814528114507331']
with open(swift_repos_path, 'r') as f:
    swift_repo_names = json.load(f)

# Prepare the repo names for SQL IN clause without extra quotes
repo_names_str = ', '.join([f"'{name}'" for name in swift_repo_names])

# Construct the SQL query
query = f"""SELECT id, sample_repo_name FROM contents WHERE sample_repo_name IN ({repo_names_str}) AND repo_data_description NOT LIKE '%binary%' AND sample_path LIKE '%.swift';"""

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-2687622922007764891': 'file_storage/function-call-2687622922007764891.json', 'var_function-call-17635814528114507331': 'file_storage/function-call-17635814528114507331.json'}

exec(code, env_args)
