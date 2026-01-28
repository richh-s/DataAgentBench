code = """import json
import pandas as pd
# load package_database query result from file
path = var_call_XxJ8SGjcMYmSsXtBIWsn1AFH
with open(path, 'r') as f:
    data = json.load(f)
# create DataFrame
df = pd.DataFrame(data)
# parse VersionInfo
import ast

def parse_vi(x):
    try:
        return json.loads(x)
    except Exception:
        try:
            return ast.literal_eval(x)
        except Exception:
            return {}

vi = df['VersionInfo'].apply(parse_vi)
df['IsRelease'] = vi.apply(lambda v: v.get('IsRelease'))
# convert UpstreamPublishedAt to float (some missing)
def to_float(x):
    try:
        return float(x)
    except Exception:
        return 0.0

if 'UpstreamPublishedAt' in df.columns:
    df['UpstreamPublishedAt_f'] = df['UpstreamPublishedAt'].apply(to_float)
else:
    df['UpstreamPublishedAt_f'] = 0.0

# filter for NPM and IsRelease==True
df_npm = df[df['System']=='NPM']
df_npm_rel = df_npm[df_npm['IsRelease']==True]
# group by Name and pick row with max UpstreamPublishedAt_f
idx = df_npm_rel.groupby('Name')['UpstreamPublishedAt_f'].idxmax()
latest = df_npm_rel.loc[idx, ['System','Name','Version','UpstreamPublishedAt_f']].copy()
# convert to list of dicts
result = latest.sort_values(['UpstreamPublishedAt_f','Name'], ascending=[False, True])
rows = result.to_dict(orient='records')
out = [{'System':r['System'],'Name':r['Name'],'Version':r['Version']} for r in rows]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ZavR4KAD7P83vUADhRGZZ7qG': ['packageinfo'], 'var_call_XEqbxJQII5dfDpX4g7sgLJI7': ['project_info', 'project_packageversion'], 'var_call_XxJ8SGjcMYmSsXtBIWsn1AFH': 'file_storage/call_XxJ8SGjcMYmSsXtBIWsn1AFH.json'}

exec(code, env_args)
