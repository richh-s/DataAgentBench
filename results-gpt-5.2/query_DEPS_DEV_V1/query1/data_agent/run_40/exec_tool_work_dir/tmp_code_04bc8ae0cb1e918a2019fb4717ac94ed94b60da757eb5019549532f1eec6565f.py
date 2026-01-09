code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = pd.DataFrame(load_records(var_call_h5U6zzY2EpQzluXpgNAQ5awi))
ppv = pd.DataFrame(load_records(var_call_I1SyWPKFnBgSRrmXCjWd62fy))
pi = pd.DataFrame(load_records(var_call_PMTaI6d5Nl07hh1gzIV3ZASW))

# latest version per package by max UpstreamPublishedAt
pkg['UpstreamPublishedAt'] = pd.to_numeric(pkg['UpstreamPublishedAt'], errors='coerce')
pkg = pkg.dropna(subset=['UpstreamPublishedAt'])
idx = pkg.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest = pkg.loc[idx, ['Name','Version','UpstreamPublishedAt']].copy()

# join to project mapping
m = latest.merge(ppv[['Name','Version','ProjectName']], on=['Name','Version'], how='inner')

# parse project name and stars from Project_Information
pat = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?([0-9,]+)\s+stars", re.IGNORECASE)
proj_rows = []
for s in pi['Project_Information'].dropna().astype(str):
    mt = pat.search(s)
    if mt:
        proj = mt.group(1)
        stars = int(mt.group(2).replace(',',''))
        proj_rows.append((proj, stars))
proj = pd.DataFrame(proj_rows, columns=['ProjectName','Stars']).drop_duplicates(subset=['ProjectName'], keep='last')

m2 = m.merge(proj, on='ProjectName', how='inner')

# If multiple ProjectName per package latest version, take max stars
m2 = m2.sort_values(['Name','Stars'], ascending=[True, False])
m2 = m2.drop_duplicates(subset=['Name'], keep='first')

out = m2.sort_values('Stars', ascending=False).head(5)[['Name','Version','ProjectName','Stars']]
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_h5U6zzY2EpQzluXpgNAQ5awi': 'file_storage/call_h5U6zzY2EpQzluXpgNAQ5awi.json', 'var_call_I1SyWPKFnBgSRrmXCjWd62fy': 'file_storage/call_I1SyWPKFnBgSRrmXCjWd62fy.json', 'var_call_PMTaI6d5Nl07hh1gzIV3ZASW': 'file_storage/call_PMTaI6d5Nl07hh1gzIV3ZASW.json'}

exec(code, env_args)
