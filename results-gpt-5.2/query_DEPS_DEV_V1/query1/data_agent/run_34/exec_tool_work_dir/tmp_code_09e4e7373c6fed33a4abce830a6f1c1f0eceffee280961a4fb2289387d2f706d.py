code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_XtmDsVLJKCWM5SMubHerT9Qm)
ppv = load_records(var_call_N48gL9eUU138X9lG1Ebyn1dG)
pi = load_records(var_call_qdvEzx7SZc0RnC7jSHDbzsKI)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest version per package by UpstreamPublishedAt
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
pkg_df = pkg_df.dropna(subset=['UpstreamPublishedAt'])
idx = pkg_df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest_df = pkg_df.loc[idx, ['Name','Version','UpstreamPublishedAt']].copy()

# join to project mapping
m = latest_df.merge(ppv_df[['Name','Version','ProjectName']], on=['Name','Version'], how='inner')
# if multiple projectnames per package version, keep first
m = m.dropna(subset=['ProjectName']).drop_duplicates(subset=['Name','Version'])

# parse stars from Project_Information, build map project->stars
star_re = re.compile(r'\b([0-9][0-9,]*)\s+stars\b', re.IGNORECASE)
proj_re = re.compile(r'\bproject\s+([^\s]+/[^\s]+)\b', re.IGNORECASE)

def parse_info(s):
    if not isinstance(s, str):
        return None, None
    pm = proj_re.search(s)
    sm = star_re.search(s)
    proj = pm.group(1).strip('.,') if pm else None
    stars = int(sm.group(1).replace(',','')) if sm else None
    return proj, stars

parsed = pi_df['Project_Information'].apply(parse_info)
pi_df['ProjectName'] = parsed.apply(lambda x: x[0])
pi_df['Stars'] = parsed.apply(lambda x: x[1])
pi_df = pi_df.dropna(subset=['ProjectName','Stars'])
# keep max stars per projectname if duplicates
pi_df = pi_df.groupby('ProjectName', as_index=False)['Stars'].max()

m2 = m.merge(pi_df, on='ProjectName', how='left')
m2 = m2.dropna(subset=['Stars'])

# top 5 packages by stars
m2 = m2.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
res = m2[['Name','Version','ProjectName','Stars']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_XtmDsVLJKCWM5SMubHerT9Qm': 'file_storage/call_XtmDsVLJKCWM5SMubHerT9Qm.json', 'var_call_N48gL9eUU138X9lG1Ebyn1dG': 'file_storage/call_N48gL9eUU138X9lG1Ebyn1dG.json', 'var_call_qdvEzx7SZc0RnC7jSHDbzsKI': 'file_storage/call_qdvEzx7SZc0RnC7jSHDbzsKI.json'}

exec(code, env_args)
