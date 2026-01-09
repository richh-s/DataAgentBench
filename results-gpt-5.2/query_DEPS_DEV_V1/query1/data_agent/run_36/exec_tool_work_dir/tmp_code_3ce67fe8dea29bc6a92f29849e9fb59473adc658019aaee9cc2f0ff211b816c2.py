code = """import json, re
import pandas as pd

# Load packageinfo NPM rows
pkg_path = var_call_nwul7SxGsQj1p0DU5T24Vrc3
ppv_path = var_call_n9pbPwxWlan7dEMo5IC2GCAO
pi_path = var_call_HJNGNv4LrVj73Xmw0mk3Gn51

with open(pkg_path, 'r', encoding='utf-8') as f:
    pkg = json.load(f)
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppv = json.load(f)
with open(pi_path, 'r', encoding='utf-8') as f:
    pi = json.load(f)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# Latest release per package: use max UpstreamPublishedAt
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
idx = pkg_df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest = pkg_df.loc[idx, ['Name','Version','UpstreamPublishedAt']].copy()

# join to github project mapping
m = latest.merge(ppv_df, on=['Name','Version'], how='inner')

# parse project name from Project_Information and stars
# Example: "The project lodash/lodash on GitHub ... 57779 stars"
name_pat = re.compile(r"(?:The project|The GitHub project named|The project is hosted on GitHub under the name|The project named)\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
stars_pat = re.compile(r"([0-9][0-9,]*)\s+stars")

def extract(row):
    s = row.get('Project_Information') or ''
    m1 = name_pat.search(s)
    proj = m1.group(1) if m1 else None
    m2 = stars_pat.search(s)
    stars = int(m2.group(1).replace(',','')) if m2 else None
    return pd.Series({'ProjectName': proj, 'Stars': stars})

pi_ex = pi_df.apply(extract, axis=1)
pi2 = pd.concat([pi_df, pi_ex], axis=1)
pi2 = pi2.dropna(subset=['ProjectName'])
# if duplicates, keep max stars
pi2['Stars'] = pd.to_numeric(pi2['Stars'], errors='coerce')
pi2 = pi2.groupby('ProjectName', as_index=False)['Stars'].max()

# attach stars to packages via projectname
m2 = m.merge(pi2, on='ProjectName', how='left')

# Some packages may map to multiple ProjectName; take max stars per package/version
m2 = m2.groupby(['Name','Version'], as_index=False)['Stars'].max()

# top 5 by stars
m2 = m2.dropna(subset=['Stars']).sort_values(['Stars','Name'], ascending=[False, True]).head(5)

result = m2.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_nwul7SxGsQj1p0DU5T24Vrc3': 'file_storage/call_nwul7SxGsQj1p0DU5T24Vrc3.json', 'var_call_n9pbPwxWlan7dEMo5IC2GCAO': 'file_storage/call_n9pbPwxWlan7dEMo5IC2GCAO.json', 'var_call_HJNGNv4LrVj73Xmw0mk3Gn51': 'file_storage/call_HJNGNv4LrVj73Xmw0mk3Gn51.json'}

exec(code, env_args)
