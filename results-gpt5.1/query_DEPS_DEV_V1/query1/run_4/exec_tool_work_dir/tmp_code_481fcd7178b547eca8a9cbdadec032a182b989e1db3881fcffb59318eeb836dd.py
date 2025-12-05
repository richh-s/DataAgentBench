code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_PLEWpdXE2P2hNoYGyqOpbdWP) as f:
    pkginfo = json.load(f)
with open(var_call_MVbcp7r6hgYuabcafnbex7ZX) as f:
    proj_pkg = json.load(f)
with open(var_call_gzssS8Pu3e00PuaLaC93Mh6I) as f:
    proj_info = json.load(f)

# Deduplicate and keep latest release per (System, Name)
df_pkg = pd.DataFrame(pkginfo)
# Order already by Name, Ordinal desc; keep first occurrence per Name
latest_pkg = df_pkg.drop_duplicates(subset=['Name'], keep='first')

# Join with project_packageversion on System, Name, Version
df_proj_pkg = pd.DataFrame(proj_pkg)
merged = latest_pkg.merge(df_proj_pkg, on=['System','Name','Version'], how='inner')

# Extract project name and stars from Project_Information
info_df = pd.DataFrame(proj_info)

project_stars = {}
pattern = re.compile(r"The project (.*?) .*? (?:has|currently has).*? ([0-9,]+) stars")
for row in info_df['Project_Information']:
    m = pattern.search(row)
    if m:
        name = m.group(1).strip()
        stars = int(m.group(2).replace(',', ''))
        project_stars[name] = stars

# Map stars to merged using ProjectName
merged['Stars'] = merged['ProjectName'].map(project_stars)
merged = merged.dropna(subset=['Stars'])

# For each package Name, keep max stars (some may map to same repo multiple times)
agg = merged.sort_values('Stars', ascending=False)
agg = agg.drop_duplicates(subset=['Name'], keep='first')

# Get top 5 by stars
top5 = agg.nlargest(5, 'Stars')[['Name','Version','ProjectName','Stars']]

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PLEWpdXE2P2hNoYGyqOpbdWP': 'file_storage/call_PLEWpdXE2P2hNoYGyqOpbdWP.json', 'var_call_MVbcp7r6hgYuabcafnbex7ZX': 'file_storage/call_MVbcp7r6hgYuabcafnbex7ZX.json', 'var_call_gzssS8Pu3e00PuaLaC93Mh6I': 'file_storage/call_gzssS8Pu3e00PuaLaC93Mh6I.json'}

exec(code, env_args)
