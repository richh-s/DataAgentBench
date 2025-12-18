code = """import pandas as pd
import json

def escape_sql_string(s):
    return s.replace("'", "''")

file_path = locals()['var_function-call-500665788515197131']
with open(file_path, 'r') as f:
    swift_repos_raw = json.load(f)

swift_repos_df = pd.DataFrame(swift_repos_raw)
swift_repo_names = swift_repos_df['repo_name'].tolist()

# Escape each repo name before joining them into the SQL IN clause
escaped_repo_names = [f"'{escape_sql_string(repo)}'" for repo in swift_repo_names]
repo_names_str = ", ".join(escaped_repo_names)

query = f"SELECT id, sample_repo_name, repo_data_description FROM contents WHERE repo_data_description NOT LIKE '%binary%' AND sample_repo_name IN ({repo_names_str});"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-500665788515197131': 'file_storage/function-call-500665788515197131.json', 'var_function-call-14167399783899636559': 'file_storage/function-call-14167399783899636559.json', 'var_function-call-5026939649369331721': 'file_storage/function-call-5026939649369331721.json'}

exec(code, env_args)
