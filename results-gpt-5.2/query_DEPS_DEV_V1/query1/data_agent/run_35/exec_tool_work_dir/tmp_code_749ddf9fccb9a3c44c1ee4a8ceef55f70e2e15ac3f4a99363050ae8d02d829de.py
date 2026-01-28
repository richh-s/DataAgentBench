code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load_records(var_call_bB9mfeUWVmw72h4lMuMQj2Vm)
ppv = load_records(var_call_aBdqqjsd6JGfr6JDO8HcPUMK)
pi = load_records(var_call_NvSvKRY7ekxsQO58jVq6N2Qf)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# normalize types
for c in ['IsRelease','Ordinal','UpstreamPublishedAt']:
    if c in pkg_df.columns:
        pkg_df[c] = pd.to_numeric(pkg_df[c], errors='coerce')

# latest release per package (prefer IsRelease==1; use max Ordinal; tie-breaker max UpstreamPublishedAt)
rel = pkg_df[pkg_df['IsRelease']==1].copy()
# if some packages have no release flag, fallback later

rel = rel.sort_values(['System','Name','Ordinal','UpstreamPublishedAt'], ascending=[True,True,False,False])
latest_rel = rel.drop_duplicates(['System','Name'], keep='first')[['System','Name','Version']]

# map to github project by exact system/name/version
merged = latest_rel.merge(ppv_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# parse project name and stars from Project_Information
star_re = re.compile(r"\b(\d{1,3}(?:,\d{3})*)\s+stars\b", re.IGNORECASE)
proj_re = re.compile(r"\bproject\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

def parse_info(s):
    if not isinstance(s, str):
        return None, None
    mproj = proj_re.search(s)
    proj = mproj.group(1) if mproj else None
    m = star_re.search(s)
    stars = int(m.group(1).replace(',','')) if m else None
    return proj, stars

pi_df[['ProjectName','Stars']] = pi_df['Project_Information'].apply(lambda s: pd.Series(parse_info(s)))
pi_df = pi_df.dropna(subset=['ProjectName'])

merged2 = merged.merge(pi_df[['ProjectName','Stars']], on='ProjectName', how='left')
merged2 = merged2.dropna(subset=['Stars'])

# for packages that map to multiple repos (rare), use max stars
agg = merged2.groupby(['Name','Version'], as_index=False).agg({'Stars':'max'})

top5 = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bB9mfeUWVmw72h4lMuMQj2Vm': 'file_storage/call_bB9mfeUWVmw72h4lMuMQj2Vm.json', 'var_call_aBdqqjsd6JGfr6JDO8HcPUMK': 'file_storage/call_aBdqqjsd6JGfr6JDO8HcPUMK.json', 'var_call_NvSvKRY7ekxsQO58jVq6N2Qf': 'file_storage/call_NvSvKRY7ekxsQO58jVq6N2Qf.json'}

exec(code, env_args)
