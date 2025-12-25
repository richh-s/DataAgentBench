code = """import json, re, pandas as pd
from pathlib import Path

# Load latest NPM package versions
latest_path = Path(var_call_7IXuSFd4L86vn5ULujnDQz9L)
with open(latest_path, 'r') as f:
    latest = pd.read_json(f)

# Load NPM project-package mappings
map_path = Path(var_call_7JbkFJJtQJ3w70a8vTT8kd3d)
with open(map_path, 'r') as f:
    mappings = pd.read_json(f)

# Join to keep only latest versions with a mapped GitHub project
merged = latest.merge(mappings, on=['System','Name','Version'], how='inner')

# Load project info and extract project name + stars
info_path = Path(var_call_zLT1f3v5FtlrfgRbuF4o1FQ1)
with open(info_path, 'r') as f:
    info_raw = json.load(f)

rows = []
for row in info_raw:
    text = row.get('Project_Information','')
    m = re.search(r"The project (.+?) on GitHub", text)
    if not m:
        m = re.search(r"The project is hosted on GitHub under the name (.+?),", text)
    if not m:
        m = re.search(r"hosted on GitHub and currently has", text)
        if m:
            # preceding word sequence ending with owner/repo
            m2 = re.search(r"project ([^ ]+/[^ ]+) is hosted on GitHub", text)
            if m2:
                proj = m2.group(1)
            else:
                continue
        else:
            continue
    else:
        proj = m.group(1)
    ms = re.search(r"(\d+[\d,]*) stars", text)
    if not ms:
        continue
    stars = int(ms.group(1).replace(',',''))
    rows.append({'ProjectName': proj, 'Stars': stars})

proj_stars = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

# Attach stars to merged NPM latest versions via ProjectName
merged_starred = merged.merge(proj_stars, on='ProjectName', how='inner')

# For each NPM package name, keep the record with max stars (in case multiple projects)
idx = merged_starred.groupby('Name')['Stars'].idxmax()
per_pkg = merged_starred.loc[idx, ['Name','Version','Stars']]

# Top 5 by stars
top5 = per_pkg.sort_values('Stars', ascending=False).head(5)
result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uzzi04eQU6KQ9xvQeXimAnma': ['project_info', 'project_packageversion'], 'var_call_GgQrM9b3Aqk0QLhFEnYu4Z2h': 'file_storage/call_GgQrM9b3Aqk0QLhFEnYu4Z2h.json', 'var_call_7IXuSFd4L86vn5ULujnDQz9L': 'file_storage/call_7IXuSFd4L86vn5ULujnDQz9L.json', 'var_call_7JbkFJJtQJ3w70a8vTT8kd3d': 'file_storage/call_7JbkFJJtQJ3w70a8vTT8kd3d.json', 'var_call_zLT1f3v5FtlrfgRbuF4o1FQ1': 'file_storage/call_zLT1f3v5FtlrfgRbuF4o1FQ1.json'}

exec(code, env_args)
