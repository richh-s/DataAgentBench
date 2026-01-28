code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load(var_call_EksUhU1xiPQrFqfdLOVJVIbg)
ppv = load(var_call_b0aW5QJqLdpcS6Osu14vkirC)
pi = load(var_call_NjLXcy3XFwhltqubXOvRhPGY)

pkg_df = pd.DataFrame(pkg)
if pkg_df.empty:
    out = []
else:
    pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
    pkg_df = pkg_df.dropna(subset=['UpstreamPublishedAt'])
    # latest release per package by max published time; tie-break by max version string
    pkg_df = pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'], ascending=[True, False, False])
    latest = pkg_df.drop_duplicates(subset=['Name'], keep='first')[['Name','Version']]

    ppv_df = pd.DataFrame(ppv)
    if not ppv_df.empty:
        ppv_df = ppv_df[['Name','Version','ProjectName']].dropna()
    else:
        ppv_df = pd.DataFrame(columns=['Name','Version','ProjectName'])

    # parse project_info Project_Information into ProjectName and stars
    rows = []
    star_re = re.compile(r'(?:^|\s)([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)\b')
    stars_re = re.compile(r'(\d+[\d,]*)\s+stars')
    for rec in pi:
        s = rec.get('Project_Information') if isinstance(rec, dict) else None
        if not s:
            continue
        mname = star_re.search(s)
        mstars = stars_re.search(s)
        if mname and mstars:
            project = mname.group(1)
            stars = int(mstars.group(1).replace(',',''))
            rows.append({'ProjectName': project, 'Stars': stars})
    proj_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'], keep='first')

    merged = latest.merge(ppv_df, on=['Name','Version'], how='inner')
    merged = merged.merge(proj_df, on='ProjectName', how='inner')
    merged = merged.sort_values(['Stars','Name'], ascending=[False, True])

    # if multiple repos per package/version, keep max stars
    merged = merged.sort_values(['Name','Version','Stars'], ascending=[True, True, False]).drop_duplicates(subset=['Name','Version'], keep='first')

    top5 = merged.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
    out = top5[['Name','Version','Stars','ProjectName']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6uggoPVDtK2VSjqJ1z9HzbHl': ['packageinfo'], 'var_call_hSF0CM4usTrZKTgQznJUgOim': ['project_info', 'project_packageversion'], 'var_call_EksUhU1xiPQrFqfdLOVJVIbg': 'file_storage/call_EksUhU1xiPQrFqfdLOVJVIbg.json', 'var_call_b0aW5QJqLdpcS6Osu14vkirC': 'file_storage/call_b0aW5QJqLdpcS6Osu14vkirC.json', 'var_call_NjLXcy3XFwhltqubXOvRhPGY': 'file_storage/call_NjLXcy3XFwhltqubXOvRhPGY.json'}

exec(code, env_args)
