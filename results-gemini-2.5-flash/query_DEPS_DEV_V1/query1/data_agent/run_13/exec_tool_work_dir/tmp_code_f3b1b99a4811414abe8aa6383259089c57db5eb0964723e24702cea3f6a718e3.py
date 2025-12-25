code = """import json
import pandas as pd

with open(locals()['var_function-call-14123670748196616046'], 'r') as f:
    packageinfo_data = json.load(f)

df_packageinfo = pd.DataFrame(packageinfo_data)

df_releases = df_packageinfo[df_packageinfo['VersionInfo'].apply(lambda x: json.loads(x).get('IsRelease', False))]

df_releases['Ordinal'] = df_releases['VersionInfo'].apply(lambda x: json.loads(x).get('Ordinal'))
df_releases['Ordinal'] = pd.to_numeric(df_releases['Ordinal'], errors='coerce')

df_releases = df_releases.dropna(subset=['Ordinal'])

latest_releases = df_releases.loc[df_releases.groupby('Name')['Ordinal'].idxmax()]

latest_releases = latest_releases[['Name', 'Version']]

print('__RESULT__:')
print(latest_releases.to_json(orient='records'))"""

env_args = {'var_function-call-14123670748196616046': 'file_storage/function-call-14123670748196616046.json'}

exec(code, env_args)
