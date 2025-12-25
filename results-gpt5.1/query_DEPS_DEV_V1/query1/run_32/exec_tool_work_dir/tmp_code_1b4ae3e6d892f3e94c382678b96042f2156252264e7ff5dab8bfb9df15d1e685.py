code = """import json, re, pandas as pd
from pathlib import Path

latest_path = Path(var_call_NBqjhDFE9p5vZE5ckuWFvSGb)
latest = json.loads(latest_path.read_text())
latest_df = pd.DataFrame(latest)

ppv_path = Path(var_call_KYJd5J0sFbw5Z5RLz7HxYxqW)
ppv = json.loads(ppv_path.read_text())
ppv_df = pd.DataFrame(ppv)

merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

pi_path = Path(var_call_SdoXT8brIhttkDXh9GwMZYw4)
pi = json.loads(pi_path.read_text())
pi_df = pd.DataFrame(pi)

pattern = re.compile(r"The project (.*?) .*? has .*? (\d+) stars")
proj_rows = []
for s in pi_df['Project_Information']:
    m = pattern.search(s)
    if m:
        proj_rows.append({'ProjectName': m.group(1), 'Stars': int(m.group(2))})

stars_df = pd.DataFrame(proj_rows).drop_duplicates('ProjectName')

merged2 = merged.merge(stars_df, on='ProjectName', how='inner')

agg = merged2.groupby(['Name','Version'], as_index=False)['Stars'].max()

top5 = agg.sort_values('Stars', ascending=False).head(5)

res = top5.to_dict(orient='records')

out = json.dumps(res)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_BLO3otV1V4rivqXAX3pRi87F': 'file_storage/call_BLO3otV1V4rivqXAX3pRi87F.json', 'var_call_z4WiL7Eo82c6RCXVlGW8h51n': ['project_info', 'project_packageversion'], 'var_call_NBqjhDFE9p5vZE5ckuWFvSGb': 'file_storage/call_NBqjhDFE9p5vZE5ckuWFvSGb.json', 'var_call_KYJd5J0sFbw5Z5RLz7HxYxqW': 'file_storage/call_KYJd5J0sFbw5Z5RLz7HxYxqW.json', 'var_call_SdoXT8brIhttkDXh9GwMZYw4': 'file_storage/call_SdoXT8brIhttkDXh9GwMZYw4.json'}

exec(code, env_args)
