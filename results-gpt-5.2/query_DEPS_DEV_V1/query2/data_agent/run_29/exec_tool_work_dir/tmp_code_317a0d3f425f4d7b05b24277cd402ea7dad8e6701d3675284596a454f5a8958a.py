code = """import json, re, pandas as pd
from pathlib import Path

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        return json.loads(Path(v).read_text())
    return v

ppv = load_records(var_call_kDIC4Owc7GAyEtjuKRXGaU7L)
pkgs = load_records(var_call_2FLFBVEmylG0RP5gXkPFxTRP)
projinfo = load_records(var_call_CSZZfALJ2iRdYKrTO0xsrbtw)

ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']]
pkgs_df = pd.DataFrame(pkgs)

# filter MIT + IsRelease true

def is_mit(lic):
    try:
        arr = json.loads(lic)
        return any(str(x).strip().upper() == 'MIT' for x in arr)
    except Exception:
        return False

def is_release(vinfo):
    try:
        obj = json.loads(vinfo)
        return bool(obj.get('IsRelease'))
    except Exception:
        return False

pkgs_df = pkgs_df[pkgs_df['Licenses'].apply(is_mit) & pkgs_df['VersionInfo'].apply(is_release)]

merged = pkgs_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# parse project_info strings to extract owner/repo and forks
pattern = re.compile(r"project\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?([0-9][0-9,]*)\s+fork", re.IGNORECASE)

rows = []
for rec in projinfo:
    s = rec.get('Project_Information') or ''
    m = pattern.search(s)
    if m:
        proj = m.group(1)
        forks = int(m.group(2).replace(',',''))
        rows.append({'ProjectName': proj, 'Forks': forks, 'Project_Information': s})
proj_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

merged2 = merged.merge(proj_df[['ProjectName','Forks']], on='ProjectName', how='inner')

# select top 5 unique projects by forks
out = (merged2.groupby('ProjectName', as_index=False)
       .agg(Forks=('Forks','max'), ExamplePackage=('Name','first'))
       .sort_values(['Forks','ProjectName'], ascending=[False, True])
       .head(5))

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kDIC4Owc7GAyEtjuKRXGaU7L': 'file_storage/call_kDIC4Owc7GAyEtjuKRXGaU7L.json', 'var_call_2FLFBVEmylG0RP5gXkPFxTRP': 'file_storage/call_2FLFBVEmylG0RP5gXkPFxTRP.json', 'var_call_CSZZfALJ2iRdYKrTO0xsrbtw': 'file_storage/call_CSZZfALJ2iRdYKrTO0xsrbtw.json'}

exec(code, env_args)
