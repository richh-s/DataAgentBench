code = """import json, re, pandas as pd

# load latest NPM releases
path_latest = var_call_g1G2lIqEz26TSK8pTVKfOvA2
with open(path_latest) as f:
    latest = pd.DataFrame(json.load(f))

# load project_packageversion for NPM
path_pp = var_call_whJh4DlklF8Dbphwe2meg2nz
with open(path_pp) as f:
    pp = pd.DataFrame(json.load(f))
pp = pp[pp['System'] == 'NPM']

# join latest with project_packageversion
merged = latest.merge(pp, on=['System','Name','Version'], how='inner')

# load project_info
path_pi = var_call_ZypVxjjyEN8cKNMgfjQzpLco
with open(path_pi) as f:
    pi = pd.DataFrame(json.load(f))

# extract repo name and stars from Project_Information
repo_names = []
stars_list = []
for info in pi['Project_Information']:
    m_repo = re.search(r"project ([^/]+/[^ ]+)", info)
    if not m_repo:
        m_repo = re.search(r"named ([^/]+/[^ ]+)", info)
    repo_names.append(m_repo.group(1) if m_repo else None)
    m_stars = re.search(r"(\d[,\d]*) stars", info)
    if m_stars:
        stars = int(m_stars.group(1).replace(',', ''))
    else:
        stars = None
    stars_list.append(stars)
pi['ProjectName'] = repo_names
pi['Stars'] = stars_list

# join merged with pi on ProjectName
full = merged.merge(pi[['ProjectName','Stars']], on='ProjectName', how='left')

# aggregate max stars per package latest version
agg = full.groupby(['Name','Version'], as_index=False)['Stars'].max()

# top 5 by Stars
top5 = agg.dropna(subset=['Stars']).sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_esQgIkJbYcAetGMFXKGRQ5oe': 'file_storage/call_esQgIkJbYcAetGMFXKGRQ5oe.json', 'var_call_wOSiEy2orHHEz4hM5q3hw7lH': ['project_info', 'project_packageversion'], 'var_call_whJh4DlklF8Dbphwe2meg2nz': 'file_storage/call_whJh4DlklF8Dbphwe2meg2nz.json', 'var_call_ZypVxjjyEN8cKNMgfjQzpLco': 'file_storage/call_ZypVxjjyEN8cKNMgfjQzpLco.json', 'var_call_g1G2lIqEz26TSK8pTVKfOvA2': 'file_storage/call_g1G2lIqEz26TSK8pTVKfOvA2.json'}

exec(code, env_args)
