code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg_releases = load_records(var_call_EPocINBgCKN1BQehDDZzkOEJ)
ppv = load_records(var_call_pDDLEeieCeF1jaLWUkrIZvoD)
proj_info = load_records(var_call_ruP8xnprggLqrXV6OLTmViB1)

# latest release per package: max Ordinal (fallback UpstreamPublishedAt)
df_pkg = pd.DataFrame(pkg_releases)
for c in ['Ordinal','UpstreamPublishedAt']:
    if c in df_pkg.columns:
        df_pkg[c] = pd.to_numeric(df_pkg[c], errors='coerce')

df_pkg = df_pkg.sort_values(['Name','Ordinal','UpstreamPublishedAt'], ascending=[True, False, False])
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name','Version']]

# join to github project mapping
ppv_df = pd.DataFrame(ppv)
latest_ppv = df_latest.merge(ppv_df, on=['Name','Version'], how='inner')
# if multiple projects per package-version, keep one (arbitrary) but prefer non-null
latest_ppv = latest_ppv.dropna(subset=['ProjectName']).drop_duplicates(subset=['Name','Version','ProjectName'])

# parse stars from Project_Information and extract repo
pat = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?\b([0-9][0-9,]*)\s+stars\b", re.IGNORECASE)
rows=[]
for rec in proj_info:
    s = rec.get('Project_Information')
    if not s:
        continue
    m = pat.search(s)
    if m:
        repo = m.group(1)
        stars = int(m.group(2).replace(',',''))
        rows.append({'ProjectName': repo, 'Stars': stars})
proj_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'], keep='first')

merged = latest_ppv.merge(proj_df, on='ProjectName', how='inner')
# pick max stars per package (in case multiple repos)
merged = merged.sort_values(['Name','Stars'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')

top5 = merged.sort_values('Stars', ascending=False).head(5)[['Name','Version','ProjectName','Stars']]
result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EPocINBgCKN1BQehDDZzkOEJ': 'file_storage/call_EPocINBgCKN1BQehDDZzkOEJ.json', 'var_call_pDDLEeieCeF1jaLWUkrIZvoD': 'file_storage/call_pDDLEeieCeF1jaLWUkrIZvoD.json', 'var_call_ruP8xnprggLqrXV6OLTmViB1': 'file_storage/call_ruP8xnprggLqrXV6OLTmViB1.json', 'var_call_LTRPk7jr9qve3s0u6ewJik8V': ['project_info', 'project_packageversion']}

exec(code, env_args)
