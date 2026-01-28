code = """import json, pandas as pd, re

# Load the JSON results from the stored file paths
with open(var_call_r04VcrGqvfZ0QMtfHEQrVRuB, 'r') as f:
    latest_records = json.load(f)
with open(var_call_OSlYN3fUEm9xBk7srvxCkpH4, 'r') as f:
    projver_records = json.load(f)
with open(var_call_rbjtOrzGIRLURSYjtgNNd6bA, 'r') as f:
    projinfo_records = json.load(f)

# Create DataFrames
df_latest = pd.DataFrame(latest_records)
df_projver = pd.DataFrame(projver_records)
df_projinfo = pd.DataFrame(projinfo_records)

# Keep only relevant columns
if 'Name' not in df_latest.columns or 'Version' not in df_latest.columns:
    raise SystemExit('Expected Name and Version in latest package records')

# Merge latest package versions with project_packageversion to get ProjectName(s)
df_map = pd.merge(df_latest, df_projver[['System','Name','Version','ProjectName']], on=['Name','Version'], how='inner')

# Prepare a mapping from ProjectName -> stars by searching Project_Information
proj_stars = {}

patterns = [
    re.compile(r"([0-9][0-9,]*)\s+stars", re.IGNORECASE),
    re.compile(r"stars count of\s*([0-9][0-9,]*)", re.IGNORECASE),
    re.compile(r"total of\s*([0-9][0-9,]*)\s+stars", re.IGNORECASE),
    re.compile(r"has garnered.*?([0-9][0-9,]*)\s+stars", re.IGNORECASE),
]

for pn in df_map['ProjectName'].dropna().unique():
    pn_str = str(pn)
    # find rows in projinfo where Project_Information contains the project name
    matches = df_projinfo[df_projinfo['Project_Information'].astype(str).str.contains(pn_str, na=False)]
    best = 0
    if not matches.empty:
        for text in matches['Project_Information'].astype(str):
            found = False
            for pat in patterns:
                m = pat.search(text)
                if m:
                    num = int(m.group(1).replace(',', ''))
                    if num > best:
                        best = num
                    found = True
            # also try a generic fallback: look for digits before 'stars' with possible punctuation
            if not found:
                m2 = re.search(r"([0-9][0-9,]*)[^\n\r]{0,20}?stars", text, re.IGNORECASE)
                if m2:
                    num = int(m2.group(1).replace(',', ''))
                    if num > best:
                        best = num
    # If no matches found in project_info, leave as 0
    proj_stars[pn_str] = best

# For each package (Name,Version) compute the max stars among its associated projects
results = []
for (name, version), group in df_map.groupby(['Name','Version']):
    project_names = group['ProjectName'].dropna().astype(str).unique()
    max_stars = 0
    for pn in project_names:
        max_stars = max(max_stars, proj_stars.get(pn, 0))
    results.append({'Name': name, 'Version': version, 'Stars': int(max_stars)})

# Sort and take top 5
results_sorted = sorted(results, key=lambda x: x['Stars'], reverse=True)
top5 = results_sorted[:5]

# Output as JSON string
out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4YhPTB6U6nz5GrDAJSdpl10Y': ['packageinfo'], 'var_call_WPlwlWeUDwtz9xUlXTPFhb3U': ['project_info', 'project_packageversion'], 'var_call_r04VcrGqvfZ0QMtfHEQrVRuB': 'file_storage/call_r04VcrGqvfZ0QMtfHEQrVRuB.json', 'var_call_OSlYN3fUEm9xBk7srvxCkpH4': 'file_storage/call_OSlYN3fUEm9xBk7srvxCkpH4.json', 'var_call_rbjtOrzGIRLURSYjtgNNd6bA': 'file_storage/call_rbjtOrzGIRLURSYjtgNNd6bA.json'}

exec(code, env_args)
