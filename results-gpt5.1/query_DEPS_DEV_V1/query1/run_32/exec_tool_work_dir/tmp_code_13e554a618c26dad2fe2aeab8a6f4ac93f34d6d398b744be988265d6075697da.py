code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_BLO3otV1V4rivqXAX3pRi87F)
records = json.loads(path.read_text())

df = pd.DataFrame(records)
vi = df['VersionInfo'].apply(json.loads)
df['IsRelease'] = vi.apply(lambda x: x.get('IsRelease'))
df['Ordinal'] = vi.apply(lambda x: x.get('Ordinal'))

df_rel = df[df['IsRelease']].copy()
latest = df_rel.sort_values('Ordinal').groupby(['System','Name'], as_index=False).tail(1)
res = latest[['System','Name','Version']].to_json(orient='records')

print("__RESULT__:")
print(res)"""

env_args = {'var_call_BLO3otV1V4rivqXAX3pRi87F': 'file_storage/call_BLO3otV1V4rivqXAX3pRi87F.json', 'var_call_z4WiL7Eo82c6RCXVlGW8h51n': ['project_info', 'project_packageversion']}

exec(code, env_args)
