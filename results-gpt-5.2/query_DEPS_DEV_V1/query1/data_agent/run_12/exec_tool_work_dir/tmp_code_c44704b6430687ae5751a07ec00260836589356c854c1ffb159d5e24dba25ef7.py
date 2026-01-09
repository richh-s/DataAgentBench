code = """import json, re, pandas as pd

# Load possibly large JSON lists

def load_records(v):
    if isinstance(v, str):
        # file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_mktWV3QvNi0JQtEZM3MccB3e)
ppv = load_records(var_call_AvoH7pPXDYZfOJ9o1ALG0HO7)
pi = load_records(var_call_Cgug1ltwB0X0jklD1DVnRum3)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per package (Name) using VersionInfo.IsRelease == true and max Ordinal

def is_release(vinfo):
    try:
        o = json.loads(vinfo)
        return bool(o.get('IsRelease'))
    except Exception:
        return False

def ordinal(vinfo):
    try:
        o = json.loads(vinfo)
        return o.get('Ordinal')
    except Exception:
        return None

pkg_df['IsRelease'] = pkg_df['VersionInfo'].map(is_release)
pkg_df['Ordinal'] = pkg_df['VersionInfo'].map(ordinal)

rel = pkg_df[pkg_df['IsRelease'] == True].copy()
rel['Ordinal'] = pd.to_numeric(rel['Ordinal'], errors='coerce')
# if Ordinal missing, fallback to UpstreamPublishedAt
rel['UpstreamPublishedAt_num'] = pd.to_numeric(rel['UpstreamPublishedAt'], errors='coerce')

# pick latest by Ordinal then time
rel = rel.sort_values(['Name','Ordinal','UpstreamPublishedAt_num'], ascending=[True, False, False])
latest = rel.drop_duplicates(['Name'], keep='first')[['Name','Version']]
latest['System'] = 'NPM'

# join to project_packageversion
m = pd.merge(latest, ppv_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
# if multiple project names per package latest version, keep first distinct project
m = m.dropna(subset=['ProjectName']).drop_duplicates(['Name','Version','ProjectName'])

# Extract repo full name and stars from Project_Information
pat_repo = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
pat_stars = re.compile(r"([0-9][0-9,]*)\s+stars")

def parse_repo(s):
    if not isinstance(s, str):
        return None
    m = pat_repo.search(s)
    return m.group(1) if m else None

def parse_stars(s):
    if not isinstance(s, str):
        return None
    m = pat_stars.search(s)
    if not m:
        return None
    return int(m.group(1).replace(',',''))

pi_df['ProjectName'] = pi_df['Project_Information'].map(parse_repo)
pi_df['Stars'] = pi_df['Project_Information'].map(parse_stars)
pi_df = pi_df.dropna(subset=['ProjectName'])

# join stars
m2 = pd.merge(m, pi_df[['ProjectName','Stars']], on='ProjectName', how='left')
# For each package, choose project with max stars
m2['Stars'] = pd.to_numeric(m2['Stars'], errors='coerce')
m2 = m2.sort_values(['Name','Stars'], ascending=[True, False])
best_proj = m2.drop_duplicates(['Name'], keep='first')

# top 5 by stars
best_proj = best_proj.dropna(subset=['Stars'])
top5 = best_proj.sort_values('Stars', ascending=False).head(5)

out = top5[['Name','Version','ProjectName','Stars']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mktWV3QvNi0JQtEZM3MccB3e': 'file_storage/call_mktWV3QvNi0JQtEZM3MccB3e.json', 'var_call_AvoH7pPXDYZfOJ9o1ALG0HO7': 'file_storage/call_AvoH7pPXDYZfOJ9o1ALG0HO7.json', 'var_call_Cgug1ltwB0X0jklD1DVnRum3': 'file_storage/call_Cgug1ltwB0X0jklD1DVnRum3.json'}

exec(code, env_args)
