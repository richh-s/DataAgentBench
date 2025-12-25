code = """import json, pandas as pd
import re

# load latest npm releases
with open(var_call_dQlxNlD1h6yTjLGPdDz7rep7, 'r') as f:
    latest_data = json.load(f)
latest = pd.DataFrame(latest_data)

# load npm github mappings
with open(var_call_QAP3JGPOdTPVpKt6NGMpTvFp, 'r') as f:
    mappings_data = json.load(f)
mappings = pd.DataFrame(mappings_data)

# inner join on System, Name, Version
merged = latest.merge(mappings, on=['System','Name','Version'], how='inner')

# load project_info
with open(var_call_xgVTL389iq68LTespddwbepz, 'r') as f:
    pinfo_data = json.load(f)
pinfo = pd.DataFrame(pinfo_data)

# regex patterns
name_pattern = re.compile(r"project(?: named)? ([^\s,]+/[^\s,]+)")
stars_pattern = re.compile(r"(\d[\d,]*) stars")

# extract ProjectName
def extract_name(text):
    if not isinstance(text, str):
        return None
    m = name_pattern.search(text)
    return m.group(1) if m else None

# extract stars
def extract_stars(text):
    if not isinstance(text, str):
        return None
    m = stars_pattern.search(text)
    if not m:
        return None
    return int(m.group(1).replace(',', ''))

pinfo['ProjectName'] = pinfo['Project_Information'].apply(extract_name)
pinfo['Stars'] = pinfo['Project_Information'].apply(extract_stars)

# merge to get stars per package version
merged2 = merged.merge(pinfo[['ProjectName','Stars']], on='ProjectName', how='left')

# aggregate max stars per package latest version
agg = merged2.groupby(['Name','Version'], as_index=False)['Stars'].max()

# sort and get top 5
agg_sorted = agg.sort_values(['Stars','Name'], ascending=[False, True])

top5 = agg_sorted.head(5).to_dict(orient='records')

out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_w5xqkEyAMi5WiuWIVZbUVzUA': 'file_storage/call_w5xqkEyAMi5WiuWIVZbUVzUA.json', 'var_call_NiBgBWvvZdahlakMJaoDerGu': ['project_info', 'project_packageversion'], 'var_call_QAP3JGPOdTPVpKt6NGMpTvFp': 'file_storage/call_QAP3JGPOdTPVpKt6NGMpTvFp.json', 'var_call_dQlxNlD1h6yTjLGPdDz7rep7': 'file_storage/call_dQlxNlD1h6yTjLGPdDz7rep7.json', 'var_call_xgVTL389iq68LTespddwbepz': 'file_storage/call_xgVTL389iq68LTespddwbepz.json'}

exec(code, env_args)
