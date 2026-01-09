code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

latest = load_records(var_call_zH1d8mzee4hpuyBLFxGFl8EJ)
ppv = load_records(var_call_3hWScvf0cKbGraKBWSVIHLSN)
pi = load_records(var_call_ShLliJW5oQ5lhl87iCJobdtH)

latest_df = pd.DataFrame(latest)
ppv_df = pd.DataFrame(ppv)

# join to keep only latest package versions that have github mapping
m = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# project_info only has Project_Information text; parse owner/repo and stars
pi_df = pd.DataFrame(pi)

def parse_info(s):
    if s is None:
        return (None, None)
    mname = re.search(r'project\s+([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)', s)
    pname = mname.group(1) if mname else None
    mstars = re.search(r'(\d[\d,]*)\s+stars', s)
    stars = int(mstars.group(1).replace(',','')) if mstars else None
    return (pname, stars)

parsed = pi_df['Project_Information'].apply(parse_info)
pi_df['ProjectName'] = parsed.apply(lambda x: x[0])
pi_df['Stars'] = parsed.apply(lambda x: x[1])

# remove nulls and deduplicate projectnames (keep max stars if duplicates)
pi_df = pi_df.dropna(subset=['ProjectName'])
pi_df = pi_df.sort_values('Stars', ascending=False).drop_duplicates('ProjectName', keep='first')

m2 = m.merge(pi_df[['ProjectName','Stars']], on='ProjectName', how='left')

# for each package, take max stars across possible multiple projects
pkg = (m2.dropna(subset=['Stars'])
       .groupby(['Name','Version'], as_index=False)['Stars'].max())

pkg = pkg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
res = pkg.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_zH1d8mzee4hpuyBLFxGFl8EJ': 'file_storage/call_zH1d8mzee4hpuyBLFxGFl8EJ.json', 'var_call_3hWScvf0cKbGraKBWSVIHLSN': 'file_storage/call_3hWScvf0cKbGraKBWSVIHLSN.json', 'var_call_ShLliJW5oQ5lhl87iCJobdtH': 'file_storage/call_ShLliJW5oQ5lhl87iCJobdtH.json'}

exec(code, env_args)
