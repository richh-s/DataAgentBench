code = """import json, pandas as pd

# load latest npm releases
with open(var_call_dQlxNlD1h6yTjLGPdDz7rep7, 'r') as f:
    latest = pd.DataFrame(json.load(f))

# load npm github mappings
with open(var_call_QAP3JGPOdTPVpKt6NGMpTvFp, 'r') as f:
    mappings = pd.DataFrame(json.load(f))

# inner join on System, Name, Version
merged = latest.merge(mappings, on=['System','Name','Version'], how='inner')

# load project_info
with open(var_call_xgVTL389iq68LTespddwbepz, 'r') as f:
    pinfo = pd.DataFrame(json.load(f))

# extract ProjectName and stars from Project_Information
import re

# ProjectName pattern: 'project owner/repo' or 'named owner/repo'; capture owner/repo
name_pattern = re.compile(r"project(?: named)? ([^\s,]+/[^"]+?) ")
# stars pattern: 'X stars'
stars_pattern = re.compile(r"(\d[\d,]*) stars")

pinfo['ProjectName'] = pinfo['Project_Information'].apply(lambda s: name_pattern.search(s).group(1) if isinstance(s,str) and name_pattern.search(s) else None)

def get_stars(s):
    if not isinstance(s,str):
        return None
    m = stars_pattern.search(s)
    if not m:
        return None
    return int(m.group(1).replace(',',''))

pinfo['Stars'] = pinfo['Project_Information'].apply(get_stars)

# merge to get stars per package
merged2 = merged.merge(pinfo[['ProjectName','Stars']], on='ProjectName', how='left')

# for packages that map to multiple projects, take max stars
agg = merged2.groupby(['Name','Version'], as_index=False)['Stars'].max()

# top 5 by stars
top5 = agg.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_w5xqkEyAMi5WiuWIVZbUVzUA': 'file_storage/call_w5xqkEyAMi5WiuWIVZbUVzUA.json', 'var_call_NiBgBWvvZdahlakMJaoDerGu': ['project_info', 'project_packageversion'], 'var_call_QAP3JGPOdTPVpKt6NGMpTvFp': 'file_storage/call_QAP3JGPOdTPVpKt6NGMpTvFp.json', 'var_call_dQlxNlD1h6yTjLGPdDz7rep7': 'file_storage/call_dQlxNlD1h6yTjLGPdDz7rep7.json', 'var_call_xgVTL389iq68LTespddwbepz': 'file_storage/call_xgVTL389iq68LTespddwbepz.json'}

exec(code, env_args)
