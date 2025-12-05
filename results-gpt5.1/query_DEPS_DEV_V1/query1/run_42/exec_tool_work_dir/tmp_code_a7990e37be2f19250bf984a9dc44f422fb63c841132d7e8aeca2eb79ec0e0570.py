code = """import json, re, pandas as pd, os

# load mappings latest NPM -> GitHub project
path_map = var_call_YfWesYFBlu3rJXAtkt5wrsUo
with open(path_map, 'r') as f:
    map_rec = json.load(f)
map_df = pd.DataFrame(map_rec)

# load project info text
path_info = var_call_MGdXsDQuB4BKRXazXFyJvx0J
with open(path_info, 'r') as f:
    info_rec = json.load(f)
info_df = pd.DataFrame(info_rec)

# extract project name and stars from text
name_pat = re.compile(r"project ([^/\s]+/[^\s]+)")
stars_pat = re.compile(r"(\d[\d,]*) stars")

projects = []
for txt in info_df['Project_Information']:
    name_m = name_pat.search(txt)
    stars_m = stars_pat.search(txt)
    if not name_m or not stars_m:
        continue
    name = name_m.group(1)
    stars = int(stars_m.group(1).replace(',', ''))
    projects.append({'ProjectName': name, 'Stars': stars})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['ProjectName'])

merged = map_df.merge(proj_df, on='ProjectName', how='inner')

# For each package Name, keep the row with max stars (though there should be one latest version per Name)
idx = merged.groupby('Name')['Stars'].idxmax()
per_pkg = merged.loc[idx]

# top 5 by stars
top5 = per_pkg.sort_values('Stars', ascending=False).head(5)
result = top5[['Name','Version','Stars','ProjectName']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_4gV01X4T1kO0s1Eot49lGyhD': 'file_storage/call_4gV01X4T1kO0s1Eot49lGyhD.json', 'var_call_dok3dxMAkcsJR1MjJzyJPhSN': ['project_info', 'project_packageversion'], 'var_call_rMAa4eGug5bj0B0mAOwjzPA0': 'file_storage/call_rMAa4eGug5bj0B0mAOwjzPA0.json', 'var_call_8vSmLIS9rGnkF249dKccWpnx': 'file_storage/call_8vSmLIS9rGnkF249dKccWpnx.json', 'var_call_YfWesYFBlu3rJXAtkt5wrsUo': 'file_storage/call_YfWesYFBlu3rJXAtkt5wrsUo.json', 'var_call_MGdXsDQuB4BKRXazXFyJvx0J': 'file_storage/call_MGdXsDQuB4BKRXazXFyJvx0J.json'}

exec(code, env_args)
