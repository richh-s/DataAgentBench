code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg_releases = load_records(var_call_EPocINBgCKN1BQehDDZzkOEJ)
ppv = load_records(var_call_pDDLEeieCeF1jaLWUkrIZvoD)
proj_info = load_records(var_call_ruP8xnprggLqrXV6OLTmViB1)

df_pkg = pd.DataFrame(pkg_releases)
for c in ['Ordinal','UpstreamPublishedAt']:
    if c in df_pkg.columns:
        df_pkg[c] = pd.to_numeric(df_pkg[c], errors='coerce')

df_pkg = df_pkg.sort_values(['Name','Ordinal','UpstreamPublishedAt'], ascending=[True, False, False])
df_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')[['Name','Version']]

ppv_df = pd.DataFrame(ppv)
# ensure columns present
if 'ProjectName' not in ppv_df.columns:
    # nothing to join
    out=[]
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

latest_ppv = df_latest.merge(ppv_df[['Name','Version','ProjectName']], on=['Name','Version'], how='inner')
latest_ppv = latest_ppv.dropna(subset=['ProjectName']).drop_duplicates(subset=['Name','Version','ProjectName'])

pat = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?\b([0-9][0-9,]*)\s+stars\b", re.IGNORECASE)
rows=[]
for rec in proj_info:
    s = rec.get('Project_Information')
    if not s:
        continue
    m = pat.search(s)
    if m:
        rows.append({'ProjectName': m.group(1), 'Stars': int(m.group(2).replace(',',''))})
proj_df = pd.DataFrame(rows)
if proj_df.empty:
    out=[]
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit
proj_df = proj_df.drop_duplicates(subset=['ProjectName'], keep='first')

merged = latest_ppv.merge(proj_df, on='ProjectName', how='inner')
merged = merged.sort_values(['Name','Stars'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')

top5 = merged.sort_values('Stars', ascending=False).head(5)[['Name','Version','ProjectName','Stars']]
print('__RESULT__:')
print(json.dumps(top5.to_dict(orient='records')))"""

env_args = {'var_call_EPocINBgCKN1BQehDDZzkOEJ': 'file_storage/call_EPocINBgCKN1BQehDDZzkOEJ.json', 'var_call_pDDLEeieCeF1jaLWUkrIZvoD': 'file_storage/call_pDDLEeieCeF1jaLWUkrIZvoD.json', 'var_call_ruP8xnprggLqrXV6OLTmViB1': 'file_storage/call_ruP8xnprggLqrXV6OLTmViB1.json', 'var_call_LTRPk7jr9qve3s0u6ewJik8V': ['project_info', 'project_packageversion']}

exec(code, env_args)
