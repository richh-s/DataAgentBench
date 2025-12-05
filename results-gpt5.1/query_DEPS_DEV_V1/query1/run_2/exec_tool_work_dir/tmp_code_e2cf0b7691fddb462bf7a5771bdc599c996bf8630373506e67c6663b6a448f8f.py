code = """import json, pandas as pd
import os

path = var_call_w5xqkEyAMi5WiuWIVZbUVzUA
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
vi = df['VersionInfo'].apply(json.loads)
vi = pd.json_normalize(vi)
vi.columns = ['IsRelease','Ordinal']

df = pd.concat([df.drop(columns=['VersionInfo']), vi], axis=1)

release_df = df[df['IsRelease'] == True].copy()
idx = release_df.groupby(['System','Name'])['Ordinal'].idxmax()
latest = release_df.loc[idx, ['System','Name','Version']]

result = latest.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_w5xqkEyAMi5WiuWIVZbUVzUA': 'file_storage/call_w5xqkEyAMi5WiuWIVZbUVzUA.json', 'var_call_NiBgBWvvZdahlakMJaoDerGu': ['project_info', 'project_packageversion'], 'var_call_QAP3JGPOdTPVpKt6NGMpTvFp': 'file_storage/call_QAP3JGPOdTPVpKt6NGMpTvFp.json'}

exec(code, env_args)
