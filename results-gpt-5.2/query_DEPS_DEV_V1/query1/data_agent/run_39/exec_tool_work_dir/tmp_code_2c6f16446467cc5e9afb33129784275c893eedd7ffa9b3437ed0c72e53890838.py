code = """import json, re, pandas as pd

# load large results
import os

def load_records(v):
    if isinstance(v, str) and v.endswith('.json') and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

ppv = load_records(var_call_hnvbAbYrbsB6JjveQbxe9lMi)
pi_pkg = load_records(var_call_rxbx0hvi3jPv3cuaY4h4wIHx)
proj_info = load_records(var_call_FXqfY4CHy7z8wmCEDqiSz3S8)

ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()
pkg_df = pd.DataFrame(pi_pkg)[['System','Name','Version','UpstreamPublishedAt','VersionInfo']]

# keep release versions only

def is_release(vi):
    if vi is None:
        return False
    if isinstance(vi, (dict, list)):
        try:
            return bool(vi.get('IsRelease'))
        except Exception:
            return False
    s = str(vi)
    m = re.search(r'"IsRelease"\s*:\s*(true|false)', s, re.IGNORECASE)
    if not m:
        return False
    return m.group(1).lower()=='true'

pkg_df['IsRelease'] = pkg_df['VersionInfo'].apply(is_release)
pkg_rel = pkg_df[pkg_df['IsRelease']].copy()

# latest release per package by UpstreamPublishedAt then (fallback) VersionInfo Ordinal

def extract_ordinal(vi):
    if vi is None:
        return None
    if isinstance(vi, dict):
        return vi.get('Ordinal')
    s = str(vi)
    m = re.search(r'"Ordinal"\s*:\s*(\d+)', s)
    return int(m.group(1)) if m else None

pkg_rel['Ordinal'] = pkg_rel['VersionInfo'].apply(extract_ordinal)
pkg_rel['UpstreamPublishedAt'] = pd.to_numeric(pkg_rel['UpstreamPublishedAt'], errors='coerce')

pkg_rel = pkg_rel.sort_values(['Name','UpstreamPublishedAt','Ordinal','Version'], ascending=[True,False,False,False])
latest = pkg_rel.groupby(['System','Name'], as_index=False).head(1)

# join to project mapping to get github repo for that version
latest_ppv = latest.merge(ppv_df, on=['System','Name','Version'], how='inner')

# parse project_info to extract repo and stars
proj_df = pd.DataFrame(proj_info)

repo_re = re.compile(r'project\s+([^\s]+/[^\s]+)')
stars_re = re.compile(r'(\d[\d,]*)\s+stars')

def parse_repo(text):
    if text is None:
        return None
    m = repo_re.search(str(text))
    return m.group(1) if m else None

def parse_stars(text):
    if text is None:
        return None
    m = stars_re.search(str(text))
    if not m:
        return None
    return int(m.group(1).replace(',',''))

proj_df['Repo'] = proj_df['Project_Information'].apply(parse_repo)
proj_df['Stars'] = proj_df['Project_Information'].apply(parse_stars)
proj_df = proj_df[['Repo','Stars']].dropna(subset=['Repo'])
proj_df = proj_df.sort_values(['Repo','Stars'], ascending=[True,False]).drop_duplicates('Repo')

latest_ppv['Repo'] = latest_ppv['ProjectName']
joined = latest_ppv.merge(proj_df, on='Repo', how='left')
joined = joined.dropna(subset=['Stars'])

# If multiple repos per package/version, take max stars
joined2 = joined.groupby(['System','Name','Version'], as_index=False).agg({'Stars':'max','Repo':'first'})

top5 = joined2.sort_values(['Stars','Name'], ascending=[False,True]).head(5)

result = top5[['Name','Version','Stars','Repo']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hnvbAbYrbsB6JjveQbxe9lMi': 'file_storage/call_hnvbAbYrbsB6JjveQbxe9lMi.json', 'var_call_rxbx0hvi3jPv3cuaY4h4wIHx': 'file_storage/call_rxbx0hvi3jPv3cuaY4h4wIHx.json', 'var_call_FXqfY4CHy7z8wmCEDqiSz3S8': 'file_storage/call_FXqfY4CHy7z8wmCEDqiSz3S8.json'}

exec(code, env_args)
