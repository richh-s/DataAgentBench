code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

ppv = load_records(var_call_DKl81sspUKbmzBc8YTvHtC0o)
pi = load_records(var_call_sVh6GFHDFj4tUMqGqbmB05Y9)
pack = load_records(var_call_MUW77lbT387LN56RmEQPdxxG)

ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()
pack_df = pd.DataFrame(pack)[['System','Name','Version','UpstreamPublishedAt','VersionInfo']].drop_duplicates()

# keep only release versions

def is_release(vi):
    try:
        d = json.loads(vi) if isinstance(vi, str) else (vi or {})
        return bool(d.get('IsRelease'))
    except Exception:
        return False

pack_df['IsRelease'] = pack_df['VersionInfo'].map(is_release)
pack_rel = pack_df[pack_df['IsRelease']].copy()

# latest release per package by UpstreamPublishedAt, tie-break by ordinal if present

def ordinal(vi):
    try:
        d = json.loads(vi) if isinstance(vi, str) else (vi or {})
        o = d.get('Ordinal')
        return int(o) if o is not None else None
    except Exception:
        return None

pack_rel['Ordinal'] = pack_rel['VersionInfo'].map(ordinal)
pack_rel['UpstreamPublishedAt'] = pd.to_numeric(pack_rel['UpstreamPublishedAt'], errors='coerce')

# sort so first row is latest
pack_rel_sorted = pack_rel.sort_values(['Name','UpstreamPublishedAt','Ordinal','Version'], ascending=[True,False,False,False])
latest = pack_rel_sorted.groupby(['System','Name'], as_index=False).head(1).copy()

# join to github project mapping for that exact version
latest_map = latest.merge(ppv_df, on=['System','Name','Version'], how='inner')

# parse stars from Project_Information
pi_df = pd.DataFrame(pi)

def project_name_from_info(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', s)
    return m.group(1) if m else None

def stars_from_info(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(?:\b|\s)([0-9,]+)\s+stars\b', s)
    return int(m.group(1).replace(',','')) if m else None

pi_df['ProjectName'] = pi_df['Project_Information'].map(project_name_from_info)
pi_df['Stars'] = pi_df['Project_Information'].map(stars_from_info)
pi_df = pi_df[['ProjectName','Stars']].dropna(subset=['ProjectName']).drop_duplicates(subset=['ProjectName'])

joined = latest_map.merge(pi_df, on='ProjectName', how='left')
joined = joined.dropna(subset=['Stars'])

# if multiple repos per package version, take max stars
agg = joined.groupby(['Name','Version'], as_index=False).agg({'Stars':'max'})

top5 = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
result = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DKl81sspUKbmzBc8YTvHtC0o': 'file_storage/call_DKl81sspUKbmzBc8YTvHtC0o.json', 'var_call_MUW77lbT387LN56RmEQPdxxG': 'file_storage/call_MUW77lbT387LN56RmEQPdxxG.json', 'var_call_sVh6GFHDFj4tUMqGqbmB05Y9': 'file_storage/call_sVh6GFHDFj4tUMqGqbmB05Y9.json'}

exec(code, env_args)
