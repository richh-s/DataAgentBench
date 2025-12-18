code = """import pandas as pd
import json

swift_repos_raw = json.loads(locals()['var_function-call-500665788515197131'])
swift_repos_df = pd.DataFrame(swift_repos_raw)
swift_repo_names = swift_repos_df['repo_name'].tolist()

repo_names_str = ", ".join(f"'{repo}'" for repo in swift_repo_names)

query = f"SELECT id, sample_repo_name, repo_data_description FROM contents WHERE repo_data_description NOT LIKE '%binary%' AND sample_repo_name IN ({repo_names_str});"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-500665788515197131': 'file_storage/function-call-500665788515197131.json'}

exec(code, env_args)
