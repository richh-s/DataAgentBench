code = """import json, re, pandas as pd

# load latest NPM packages
path_latest = var_call_jpIxLfVidqhNDayxHy3uOUeQ
with open(path_latest, 'r') as f:
    latest = pd.DataFrame(json.load(f))

# load NPM GitHub mappings
path_map = var_call_SIb6qL46UP70DZFfFGqS3byq
with open(path_map, 'r') as f:
    map_df = pd.DataFrame(json.load(f))

# keep only mappings for latest versions
merged = pd.merge(map_df, latest, how='inner', left_on=['Name','Version'], right_on=['Name','Version'])

# parse project_info to extract stars
path_info = var_call_Qsa6zFoF0VMWagjdzYhCafVk
with open(path_info, 'r') as f:
    info_df = pd.DataFrame(json.load(f))

# extract project name and stars from Project_Information text
proj_name = []
stars = []
for text in info_df['Project_Information']:
    m_name = re.search(r"project ([^ ]+/[^ ]+)", text)
    proj_name.append(m_name.group(1) if m_name else None)
    m_stars = re.search(r"(\d[\d,]*) stars", text)
    if m_stars:
        s = int(m_stars.group(1).replace(',',''))
    else:
        s = None
    stars.append(s)
info_df['ProjectName'] = proj_name
info_df['Stars'] = stars

# join with merged by ProjectName
merged2 = pd.merge(merged, info_df[['ProjectName','Stars']], on='ProjectName', how='left')

# drop missing stars and get top 5 by stars
merged2 = merged2.dropna(subset=['Stars'])
merged2 = merged2.sort_values('Stars', ascending=False)
top5 = merged2[['Name','Version','ProjectName','Stars']].drop_duplicates(subset=['Name']).head(5)

result = top5.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ihWrHeK6Dx4zWUpc34rvCaiX': 'file_storage/call_ihWrHeK6Dx4zWUpc34rvCaiX.json', 'var_call_EG9snxTVWGRTx2lcll9tAiWt': ['project_info', 'project_packageversion'], 'var_call_SIb6qL46UP70DZFfFGqS3byq': 'file_storage/call_SIb6qL46UP70DZFfFGqS3byq.json', 'var_call_jpIxLfVidqhNDayxHy3uOUeQ': 'file_storage/call_jpIxLfVidqhNDayxHy3uOUeQ.json', 'var_call_Qsa6zFoF0VMWagjdzYhCafVk': 'file_storage/call_Qsa6zFoF0VMWagjdzYhCafVk.json'}

exec(code, env_args)
