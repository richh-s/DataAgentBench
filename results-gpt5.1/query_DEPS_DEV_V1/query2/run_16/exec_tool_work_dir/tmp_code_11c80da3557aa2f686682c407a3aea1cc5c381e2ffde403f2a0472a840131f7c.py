code = """import json, re, pandas as pd
from pathlib import Path

# Load distinct projects from previous result
proj_list_path = Path(var_call_707bk5lUpL9EgVmHi17E8Wls)
with proj_list_path.open() as f:
    proj_list = json.load(f)

project_names = {p['ProjectName'] for p in proj_list}

# Load project_info
info_path = Path(var_call_dwGq98OLfNOt2jnn8bT9NXc4)
with info_path.open() as f:
    info_records = json.load(f)

pattern = re.compile(r"The project ([^ ]+/[^ ]+) .* has .* (\d+) forks", re.IGNORECASE)

results = []
for rec in info_records:
    text = rec.get('Project_Information', '')
    m = pattern.search(text)
    if not m:
        continue
    name, forks = m.group(1), int(m.group(2))
    if name in project_names:
        results.append({'ProjectName': name, 'Forks': forks})

# Deduplicate by project, taking max forks just in case
if results:
    df = pd.DataFrame(results)
    df = df.sort_values(['ProjectName','Forks'])
    df = df.groupby('ProjectName', as_index=False)['Forks'].max()
    top5 = df.sort_values('Forks', ascending=False).head(5)
    out = top5.to_dict(orient='records')
else:
    out = []

result = json.dumps(out)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_5Dv83x6VjQ2kfDKqHzmg9Sjl': 'file_storage/call_5Dv83x6VjQ2kfDKqHzmg9Sjl.json', 'var_call_LxAxqubrX6XJSUn2qjMqxWv6': ['project_info', 'project_packageversion'], 'var_call_ixk5sZyn4YryaSFpzZubGFsR': 'file_storage/call_ixk5sZyn4YryaSFpzZubGFsR.json', 'var_call_707bk5lUpL9EgVmHi17E8Wls': 'file_storage/call_707bk5lUpL9EgVmHi17E8Wls.json', 'var_call_dwGq98OLfNOt2jnn8bT9NXc4': 'file_storage/call_dwGq98OLfNOt2jnn8bT9NXc4.json'}

exec(code, env_args)
