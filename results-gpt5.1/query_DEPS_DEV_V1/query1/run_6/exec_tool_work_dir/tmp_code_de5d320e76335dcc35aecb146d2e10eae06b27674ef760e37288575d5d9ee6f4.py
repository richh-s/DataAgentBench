code = """import json, pandas as pd

# Load full NPM packageinfo
path_pkg = var_call_kXC3MmKJrhuof6JiMG3WIFOn
with open(path_pkg, 'r') as f:
    pkg_records = json.load(f)

# Convert to DataFrame and determine latest version per (System, Name)
pkg_df = pd.DataFrame(pkg_records)

# Keep only NPM
pkg_df = pkg_df[pkg_df['System'] == 'NPM'][['System','Name','Version']]

# To approximate "latest" version, use VersionInfo Ordinal if available; but we don't have it loaded.
# Instead, take the max Version string per Name as a heuristic.
latest_pkg = pkg_df.sort_values('Version').groupby(['System','Name'], as_index=False).tail(1)

# Load NPM project_packageversion
path_ppv = var_call_DDK4u41Q7AwDxRkNEwH0RNCf
with open(path_ppv, 'r') as f:
    ppv_records = json.load(f)
ppv_df = pd.DataFrame(ppv_records)
ppv_df = ppv_df[ppv_df['System']=='NPM']

# Join latest packages to project_packageversion on System, Name, Version
merged = latest_pkg.merge(ppv_df, on=['System','Name','Version'], how='inner')

# Extract ProjectName
projects = merged[['ProjectName']].drop_duplicates()

# Load project_info and extract stars from Project_Information
path_pinfo = var_call_vJjwraSPry5HGBc2TrrtctWx
with open(path_pinfo, 'r') as f:
    pinfo_records = json.load(f)

pinfo_df = pd.DataFrame(pinfo_records)

# Extract repo name from Project_Information by parsing the pattern 'project <owner>/<repo>' or 'named <owner>/<repo>'
import re

def extract_repo(info):
    m = re.search(r'project ([^\s/]+/[^\s]+)', info)
    if not m:
        m = re.search(r'named ([^\s/]+/[^\s]+)', info)
    if not m:
        m = re.search(r'name[d]? ([^\s/]+/[^\s]+)', info)
    return m.group(1) if m else None

pinfo_df['Repo'] = pinfo_df['Project_Information'].apply(extract_repo)

# Extract stars count: pattern like 'has X stars' or 'stars, and'

def extract_stars(info):
    m = re.search(r'(?:has|with) ([0-9,]+) stars', info)
    if not m:
        m = re.search(r'stars count of ([0-9,]+)', info)
    if not m:
        m = re.search(r'a total of ([0-9,]+) stars', info)
    if not m:
        m = re.search(r'([0-9,]+) stars', info)
    if not m:
        return None
    return int(m.group(1).replace(',', ''))

pinfo_df['Stars'] = pinfo_df['Project_Information'].apply(extract_stars)

# Map ProjectName (owner/repo) to stars
proj_stars = pinfo_df.dropna(subset=['Repo','Stars'])[['Repo','Stars']].drop_duplicates(subset=['Repo'])

merged2 = merged.merge(proj_stars, left_on='ProjectName', right_on='Repo', how='inner')

# Now we have latest package versions with associated repo stars. Find top 5 by Stars.
merged2 = merged2.sort_values('Stars', ascending=False)

# Select distinct package Name with its Version and Stars for top 5
top = merged2.groupby('Name', as_index=False).first().sort_values('Stars', ascending=False).head(5)

result = top[['Name','Version','Stars']].to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_kXC3MmKJrhuof6JiMG3WIFOn': 'file_storage/call_kXC3MmKJrhuof6JiMG3WIFOn.json', 'var_call_vZI5oB1oENzkVAOzNGTJiqZQ': ['project_info', 'project_packageversion'], 'var_call_DDK4u41Q7AwDxRkNEwH0RNCf': 'file_storage/call_DDK4u41Q7AwDxRkNEwH0RNCf.json', 'var_call_vJjwraSPry5HGBc2TrrtctWx': 'file_storage/call_vJjwraSPry5HGBc2TrrtctWx.json'}

exec(code, env_args)
