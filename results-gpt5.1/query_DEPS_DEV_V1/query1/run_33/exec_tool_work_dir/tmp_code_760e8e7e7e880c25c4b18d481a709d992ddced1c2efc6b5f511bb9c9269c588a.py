code = """import json, re, pandas as pd

pkg_path = var_call_41ARvSCBpqYIkQbUbG6Iqtwe
ppv_path = var_call_TwXAm3IF77a59fy9bftzvy26
pi_path = var_call_Ndo3lxyXmab2Sx1JDSoHcQKj

with open(pkg_path) as f:
    pkg = json.load(f)
with open(ppv_path) as f:
    ppv = json.load(f)
with open(pi_path) as f:
    pi = json.load(f)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

# keep only versions that exist in packageinfo (safety)
ppv_df = ppv_df.merge(pkg_df, on=['System','Name','Version'], how='inner')

# latest version per (System, Name) using VersionInfo not available here, approximate by Version sort as string
# but better: use packageinfo UpstreamPublishedAt if present; reload minimal cols including timestamp

# build df with timestamp
pkg_full = pd.DataFrame(pkg)[['System','Name','Version','UpstreamPublishedAt']]
merged = ppv_df.merge(pkg_full, on=['System','Name','Version'], how='left')

latest = merged.sort_values(['System','Name','UpstreamPublishedAt','Version']).groupby(['System','Name','ProjectName'], as_index=False).tail(1)

# parse stars from Project_Information
pi_df = pd.DataFrame(pi)

def parse_repo(info):
    m = re.search(r"project ([^\s/]+/[^\s]+)", info)
    if not m:
        m = re.search(r"named ([^\s/]+/[^\s]+)", info)
    return m.group(1) if m else None

def parse_stars(info):
    m = re.search(r"(\d[\d,]*) stars", info)
    if not m:
        return None
    return int(m.group(1).replace(',',''))

pi_df['ProjectName'] = pi_df['Project_Information'].apply(parse_repo)
pi_df['Stars'] = pi_df['Project_Information'].apply(parse_stars)

pi_df = pi_df.dropna(subset=['ProjectName','Stars'])

full = latest.merge(pi_df[['ProjectName','Stars']], on='ProjectName', how='inner')

# top 5 by stars per package (System,Name): since multiple projectnames could map, take max stars per package
agg = full.groupby(['Name','Version'], as_index=False)['Stars'].max()

top5 = agg.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_41ARvSCBpqYIkQbUbG6Iqtwe': 'file_storage/call_41ARvSCBpqYIkQbUbG6Iqtwe.json', 'var_call_TwXAm3IF77a59fy9bftzvy26': 'file_storage/call_TwXAm3IF77a59fy9bftzvy26.json', 'var_call_U4d7DzoeSSUcjuzzDRKhEKCG': ['project_info', 'project_packageversion'], 'var_call_Ndo3lxyXmab2Sx1JDSoHcQKj': 'file_storage/call_Ndo3lxyXmab2Sx1JDSoHcQKj.json'}

exec(code, env_args)
