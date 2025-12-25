code = """import pandas as pd
import json

with open(locals()['var_function-call-16213359666957576947'], 'r') as f:
    latest_releases = json.load(f)

with open(locals()['var_function-call-6535708252134003815'], 'r') as f:
    project_packageversion = json.load(f)

df_releases = pd.DataFrame(latest_releases)
df_project_packageversion = pd.DataFrame(project_packageversion)

merged_df = pd.merge(df_releases, df_project_packageversion, on=['Name', 'Version', 'System'], how='inner')

project_names = merged_df['ProjectName'].unique().tolist()

query_parts = []
for name in project_names:
    query_parts.append(f"ProjectName = '{name}'")

query_string = "SELECT ProjectName, Project_Information FROM project_info WHERE " + " OR ".join(query_parts)

print("__RESULT__:")
print(json.dumps({'query_string': query_string, 'merged_df': merged_df.to_json(orient='records')}))"""

env_args = {'var_function-call-7743465443656875948': 'file_storage/function-call-7743465443656875948.json', 'var_function-call-16213359666957576947': 'file_storage/function-call-16213359666957576947.json', 'var_function-call-6535708252134003815': 'file_storage/function-call-6535708252134003815.json'}

exec(code, env_args)
