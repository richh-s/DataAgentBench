code = """import json, re, pandas as pd

def load_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pkg = pd.DataFrame(load_result(var_call_YcoxcIP9WfwVPXXqUaPtSdA4))
ppv = pd.DataFrame(load_result(var_call_ZK9Wmdz44uE6hOsgbcReC7bs))
pi = pd.DataFrame(load_result(var_call_Pcbx7agoMSjyjM9yIhTZ2trW))

# latest version per (System, Name) by UpstreamPublishedAt
pkg['UpstreamPublishedAt'] = pd.to_numeric(pkg['UpstreamPublishedAt'], errors='coerce')
pkg = pkg.dropna(subset=['UpstreamPublishedAt'])
idx = pkg.groupby(['System','Name'])['UpstreamPublishedAt'].idxmax()
latest = pkg.loc[idx, ['System','Name','Version']]

# join to github project mapping
m = latest.merge(ppv, on=['System','Name','Version'], how='inner')

# extract ProjectName from Project_Information
def extract_proj(s):
    if not isinstance(s, str):
        return None
    m1 = re.search(r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', s)
    if m1:
        return m1.group(1)
    m2 = re.search(r'name\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', s)
    if m2:
        return m2.group(1)
    m3 = re.search(r'GitHub\s+under\s+the\s+name\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', s)
    if m3:
        return m3.group(1)
    return None

def extract_stars(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'([0-9][0-9,]*)\s+stars', s)
    if not m:
        return None
    return int(m.group(1).replace(',', ''))

pi['ProjectName'] = pi['Project_Information'].map(extract_proj)
pi['Stars'] = pi['Project_Information'].map(extract_stars)
pi2 = pi.dropna(subset=['ProjectName','Stars'])[['ProjectName','Stars']]
# if duplicates, take max stars
pi2 = pi2.groupby('ProjectName', as_index=False)['Stars'].max()

m2 = m.merge(pi2, on='ProjectName', how='inner')

# If multiple projects per package-version, take max stars
m2 = m2.groupby(['Name','Version'], as_index=False).agg({'Stars':'max','ProjectName':'first'})

top5 = m2.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

out = top5[['Name','Version','Stars','ProjectName']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YcoxcIP9WfwVPXXqUaPtSdA4': 'file_storage/call_YcoxcIP9WfwVPXXqUaPtSdA4.json', 'var_call_ZK9Wmdz44uE6hOsgbcReC7bs': 'file_storage/call_ZK9Wmdz44uE6hOsgbcReC7bs.json', 'var_call_Pcbx7agoMSjyjM9yIhTZ2trW': 'file_storage/call_Pcbx7agoMSjyjM9yIhTZ2trW.json'}

exec(code, env_args)
