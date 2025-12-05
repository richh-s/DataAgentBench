code = """import json, pandas as pd

# Load latest NPM versions
with open(var_call_ny3BPopkgZnMQLuZTDOGHObI, 'r') as f:
    latest = pd.DataFrame(json.load(f))

# Load project_packageversion
with open(var_call_t384OxWhOtZRuhFhjjgARl5b, 'r') as f:
    ppv = pd.DataFrame(json.load(f))

# Join to get ProjectName per latest package version
merged = latest.merge(ppv, on=['System','Name','Version'], how='inner')

# Extract owner/repo from Project_Information text later via join key constructed from it

with open(var_call_8OJgnSP2JgTUlZdBOJH6xaEW, 'r') as f:
    pinfo = pd.DataFrame(json.load(f))

# Derive repo from text like "The project leaflet/leaflet on GitHub..."
import re

def extract_repo(text):
    m = re.search(r"project ([^\s]+/[^\s]+)", text)
    return m.group(1) if m else None

def extract_stars(text):
    m = re.search(r"(\d[\d,]*) stars", text)
    if not m:
        return None
    return int(m.group(1).replace(',', ''))

pinfo['ProjectName'] = pinfo['Project_Information'].apply(extract_repo)
pinfo['Stars'] = pinfo['Project_Information'].apply(extract_stars)

# Join merged with pinfo on ProjectName
merged2 = merged.merge(pinfo[['ProjectName','Stars']], on='ProjectName', how='left')

# Get top 5 by Stars
top5 = merged2.sort_values('Stars', ascending=False).dropna(subset=['Stars']).head(5)
result = top5[['Name','Version','Stars']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_ZAXQnJ11ek3Dr9ZVmxkYYfpk': ['project_info', 'project_packageversion'], 'var_call_EBghXUfxuevY0EQecjRpUC10': 'file_storage/call_EBghXUfxuevY0EQecjRpUC10.json', 'var_call_ny3BPopkgZnMQLuZTDOGHObI': 'file_storage/call_ny3BPopkgZnMQLuZTDOGHObI.json', 'var_call_t384OxWhOtZRuhFhjjgARl5b': 'file_storage/call_t384OxWhOtZRuhFhjjgARl5b.json', 'var_call_8OJgnSP2JgTUlZdBOJH6xaEW': 'file_storage/call_8OJgnSP2JgTUlZdBOJH6xaEW.json'}

exec(code, env_args)
