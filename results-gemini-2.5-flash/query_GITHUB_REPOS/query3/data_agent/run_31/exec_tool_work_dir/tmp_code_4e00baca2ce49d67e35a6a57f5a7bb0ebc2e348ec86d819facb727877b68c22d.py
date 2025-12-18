code = """import pandas as pd
import json

# Load the full results from the JSON files
with open(locals()['var_function-call-12146580514075222178'], 'r') as f:
    shell_repos = json.load(f)
with open(locals()['var_function-call-5488780473616493227'], 'r') as f:
    apache_repos = json.load(f)

df_shell = pd.DataFrame(shell_repos)
df_apache = pd.DataFrame(apache_repos)

common_repos_df = pd.merge(df_shell, df_apache, on='repo_name', how='inner')
common_repo_names = common_repos_df['repo_name'].tolist()

print("__RESULT__:")
print(json.dumps(common_repo_names))"""

env_args = {'var_function-call-12146580514075222178': 'file_storage/function-call-12146580514075222178.json', 'var_function-call-5488780473616493227': 'file_storage/function-call-5488780473616493227.json'}

exec(code, env_args)
