code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

ppv = load_records(var_call_4sFVvXP7fa3N6BF8nvfp3Eji)
pi = load_records(var_call_pdgcPlG5E7P8gnQ7jkQm09OU)
proj = load_records(var_call_ORqVIAXH3SnW8FKzK9v0hkbN)

ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)
proj_df = pd.DataFrame(proj)

# Latest release per (System, Name) based on VersionInfo.IsRelease==true and max UpstreamPublishedAt

def parse_isrelease(s):
    if s is None or (isinstance(s,float) and pd.isna(s)):
        return None
    try:
        return bool(json.loads(s).get('IsRelease'))
    except Exception:
        return None

pi_df['IsRelease'] = pi_df['VersionInfo'].apply(parse_isrelease)
pi_df['UpstreamPublishedAt'] = pd.to_numeric(pi_df['UpstreamPublishedAt'], errors='coerce')

rel = pi_df[pi_df['IsRelease'] == True].copy()
rel = rel.sort_values(['System','Name','UpstreamPublishedAt','Version'], ascending=[True,True,False,False])
latest = rel.drop_duplicates(['System','Name'], keep='first')[['System','Name','Version']]

# Map to github project
m = pd.merge(latest, ppv_df[ppv_df['ProjectType']=='GITHUB'][['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# Extract stars from Project_Information and projectname from string
star_re = re.compile(r"\b([0-9][0-9,]*)\s+stars\b")
name_re = re.compile(r"\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b")

def extract_stars(info):
    if info is None or (isinstance(info,float) and pd.isna(info)):
        return None
    m = star_re.search(info)
    if not m:
        return None
    return int(m.group(1).replace(',',''))

def extract_projectname(info):
    if info is None or (isinstance(info,float) and pd.isna(info)):
        return None
    m = name_re.search(info)
    return m.group(1) if m else None

proj_df['ProjectName'] = proj_df['Project_Information'].apply(extract_projectname)
proj_df['Stars'] = proj_df['Project_Information'].apply(extract_stars)
proj_df = proj_df.dropna(subset=['ProjectName','Stars'])[['ProjectName','Stars']]

# join to get stars
m2 = pd.merge(m, proj_df, on='ProjectName', how='inner')

# If multiple repos per package version, take max stars
m3 = m2.groupby(['System','Name','Version'], as_index=False).agg({'Stars':'max','ProjectName':'first'})

top5 = m3.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
result = top5[['Name','Version','Stars','ProjectName']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_4sFVvXP7fa3N6BF8nvfp3Eji': 'file_storage/call_4sFVvXP7fa3N6BF8nvfp3Eji.json', 'var_call_pdgcPlG5E7P8gnQ7jkQm09OU': 'file_storage/call_pdgcPlG5E7P8gnQ7jkQm09OU.json', 'var_call_ORqVIAXH3SnW8FKzK9v0hkbN': 'file_storage/call_ORqVIAXH3SnW8FKzK9v0hkbN.json'}

exec(code, env_args)
