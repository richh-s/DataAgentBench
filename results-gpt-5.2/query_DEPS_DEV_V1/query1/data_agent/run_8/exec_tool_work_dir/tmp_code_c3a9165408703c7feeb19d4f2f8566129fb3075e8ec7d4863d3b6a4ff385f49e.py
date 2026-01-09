code = """import json, re, pandas as pd

# Load packageinfo (may be file path)
pkg_src = var_call_cChouquCbHI7DM3qfR6kcK2c
if isinstance(pkg_src, str):
    with open(pkg_src, 'r', encoding='utf-8') as f:
        pkg = json.load(f)
else:
    pkg = pkg_src

ppv_src = var_call_sDdOb6cbO7p7XR0C9NcN9EMK
if isinstance(ppv_src, str):
    with open(ppv_src, 'r', encoding='utf-8') as f:
        ppv = json.load(f)
else:
    ppv = ppv_src

pi_src = var_call_yVWWyszG35i8HR6Mz1h7tSR4
if isinstance(pi_src, str):
    with open(pi_src, 'r', encoding='utf-8') as f:
        pi = json.load(f)
else:
    pi = pi_src

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# Latest release per package based on max UpstreamPublishedAt
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest = (pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'])
          .groupby(['System','Name'], as_index=False)
          .tail(1))
latest = latest[['System','Name','Version','UpstreamPublishedAt']]

# Join to github project mapping for that exact version
m = pd.merge(latest, ppv_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# Parse stars from Project_Information and extract owner/repo
text = pi_df['Project_Information'].dropna().astype(str)
proj = text.str.extract(r'project\s+(?P<ProjectName>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
stars = text.str.extract(r'(?P<Stars>[0-9,]+)\s+stars')
pi_parsed = pd.concat([proj, stars], axis=1).dropna(subset=['ProjectName'])
pi_parsed['Stars'] = pi_parsed['Stars'].str.replace(',','', regex=False).astype('int64', errors='ignore')
# Some lines might not have stars; coerce
pi_parsed['Stars'] = pd.to_numeric(pi_parsed['Stars'], errors='coerce')
pi_parsed = pi_parsed.dropna(subset=['Stars'])
# Keep max stars per projectname if duplicates
pi_parsed = pi_parsed.groupby('ProjectName', as_index=False)['Stars'].max()

m2 = pd.merge(m, pi_parsed, on='ProjectName', how='inner')

# For packages that map to multiple repos, keep highest stars
m2_best = (m2.sort_values(['System','Name','Stars'], ascending=[True, True, False])
           .groupby(['System','Name'], as_index=False)
           .head(1))

# Top 5 by stars
out = (m2_best.sort_values('Stars', ascending=False)
       .head(5)
       [['Name','Version','ProjectName','Stars']])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cChouquCbHI7DM3qfR6kcK2c': 'file_storage/call_cChouquCbHI7DM3qfR6kcK2c.json', 'var_call_sDdOb6cbO7p7XR0C9NcN9EMK': 'file_storage/call_sDdOb6cbO7p7XR0C9NcN9EMK.json', 'var_call_yVWWyszG35i8HR6Mz1h7tSR4': 'file_storage/call_yVWWyszG35i8HR6Mz1h7tSR4.json'}

exec(code, env_args)
