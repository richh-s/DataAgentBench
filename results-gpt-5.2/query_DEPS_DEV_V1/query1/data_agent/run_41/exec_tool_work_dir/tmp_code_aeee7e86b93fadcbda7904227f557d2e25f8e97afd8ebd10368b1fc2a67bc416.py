code = """import json, re, pandas as pd

# Load large results

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

ppv = load_records(var_call_LajdCAPb2uSJ0SAz2kAU0WNQ)
pi = load_records(var_call_1wT6UAnDXOxcDNXdx6YiPsiG)

ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per package from packageinfo using VersionInfo.IsRelease and highest Ordinal
rows = []
for r in pi_df.to_dict('records'):
    vi = r.get('VersionInfo')
    isrel = False
    ordv = None
    if isinstance(vi, str):
        try:
            o = json.loads(vi)
            isrel = bool(o.get('IsRelease'))
            ordv = o.get('Ordinal')
        except Exception:
            isrel = False
            ordv = None
    rows.append((r.get('System'), r.get('Name'), r.get('Version'), isrel, ordv))
rel_df = pd.DataFrame(rows, columns=['System','Name','Version','IsRelease','Ordinal'])
rel_df = rel_df[(rel_df['System']=='NPM') & (rel_df['IsRelease']==True) & (rel_df['Ordinal'].notna())].copy()
rel_df['Ordinal'] = pd.to_numeric(rel_df['Ordinal'], errors='coerce')
rel_df = rel_df.dropna(subset=['Ordinal'])

latest = rel_df.sort_values(['Name','Ordinal'], ascending=[True, False]).drop_duplicates(['System','Name'], keep='first')

# join to project_packageversion to get github repo for that exact version
join_df = latest.merge(ppv_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# parse stars from Project_Information text

def parse_owner_repo(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', text)
    return m.group(1) if m else None

def parse_stars(text):
    if not isinstance(text, str):
        return None
    # common patterns: "Stars: 123", "stars 123", "stargazers: 123"
    patterns = [
        r'(?:Stars|Star)\s*[:=]\s*([0-9][0-9,]*)',
        r'(?:stars|star)\s*[:=]?\s*([0-9][0-9,]*)',
        r'(?:stargazers)\s*[:=]\s*([0-9][0-9,]*)'
    ]
    for p in patterns:
        m = re.search(p, text, flags=re.IGNORECASE)
        if m:
            return int(m.group(1).replace(',',''))
    # sometimes like "★ 123"
    m = re.search(r'★\s*([0-9][0-9,]*)', text)
    if m:
        return int(m.group(1).replace(',',''))
    return None

pi_df2 = pi_df.copy()
pi_df2['Repo'] = pi_df2['Project_Information'].apply(parse_owner_repo)
pi_df2['Stars'] = pi_df2['Project_Information'].apply(parse_stars)

repo_stars = pi_df2[['Repo','Stars']].dropna(subset=['Repo']).drop_duplicates('Repo')

join_df = join_df.copy()
join_df['Repo'] = join_df['ProjectName']

final = join_df.merge(repo_stars, on='Repo', how='left')
final = final.dropna(subset=['Stars'])
final['Stars'] = pd.to_numeric(final['Stars'], errors='coerce')
final = final.dropna(subset=['Stars'])

# top 5 by stars
out = final.sort_values('Stars', ascending=False).head(5)
res = out[['Name','Version','Repo','Stars']].to_dict('records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_LajdCAPb2uSJ0SAz2kAU0WNQ': 'file_storage/call_LajdCAPb2uSJ0SAz2kAU0WNQ.json', 'var_call_1wT6UAnDXOxcDNXdx6YiPsiG': 'file_storage/call_1wT6UAnDXOxcDNXdx6YiPsiG.json'}

exec(code, env_args)
