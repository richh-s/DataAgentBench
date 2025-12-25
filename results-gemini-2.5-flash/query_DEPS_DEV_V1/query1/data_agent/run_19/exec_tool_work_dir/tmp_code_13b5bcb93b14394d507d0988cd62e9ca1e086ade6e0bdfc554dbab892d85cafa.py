code = """import pandas as pd
import json

with open(locals()['var_function-call-8301244417866651882'], 'r') as f:
    package_releases = json.load(f)

with open(locals()['var_function-call-6535708252134003815'], 'r') as f:
    project_packageversion = json.load(f)

df_releases = pd.DataFrame(package_releases)

def parse_version_info(version_info_str):
    try:
        info = json.loads(version_info_str)
        return info.get('IsRelease', False), info.get('Ordinal', -1)
    except json.JSONDecodeError:
        return False, -1

df_releases[['IsRelease', 'Ordinal']] = df_releases['VersionInfo'].apply(lambda x: pd.Series(parse_version_info(x)))

latest_releases_df = df_releases[df_releases['IsRelease'] == True].loc[df_releases.groupby('Name')['Ordinal'].idxmax()]

df_project_packageversion = pd.DataFrame(project_packageversion)

merged_df = pd.merge(latest_releases_df, df_project_packageversion, on=['System', 'Name', 'Version'], how='inner')

project_names = merged_df['ProjectName'].unique().tolist()

query_parts = []
for name in project_names:
    query_parts.append(f"ProjectName = '{name.replace("'", "''")}'") # Escape single quotes for SQL

query_string = "SELECT ProjectName, Project_Information FROM project_info WHERE " + " OR ".join(query_parts)

print("__RESULT__:")
print(json.dumps({'query_string': query_string, 'merged_df': merged_df.to_json(orient='records')}))"""

env_args = {'var_function-call-7743465443656875948': 'file_storage/function-call-7743465443656875948.json', 'var_function-call-16213359666957576947': 'file_storage/function-call-16213359666957576947.json', 'var_function-call-6535708252134003815': 'file_storage/function-call-6535708252134003815.json', 'var_function-call-14881230905375770520': 'file_storage/function-call-14881230905375770520.json', 'var_function-call-8301244417866651882': 'file_storage/function-call-8301244417866651882.json'}

exec(code, env_args)
