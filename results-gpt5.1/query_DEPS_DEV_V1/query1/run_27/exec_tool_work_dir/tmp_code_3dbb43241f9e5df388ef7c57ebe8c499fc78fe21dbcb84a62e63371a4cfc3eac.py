code = """import json, re, pandas as pd

# load full tables
pkg_path = var_call_Hbey6xNOqMjaSZ1IVysH5JaU
projpkg_path = var_call_eZWUAUoRnlsdMSQHJozG19dk
projinfo_path = var_call_LUw1h1Su5h6sxcUq1gRNdq2z

with open(pkg_path) as f:
    pkg = json.load(f)
with open(projpkg_path) as f:
    projpkg = json.load(f)
with open(projinfo_path) as f:
    projinfo = json.load(f)

pkg_df = pd.DataFrame(pkg)
projpkg_df = pd.DataFrame(projpkg)
projinfo_df = pd.DataFrame(projinfo)

# filter NPM
pkg_df = pkg_df[pkg_df['System']=='NPM']
projpkg_df = projpkg_df[projpkg_df['System']=='NPM']

# latest version per (Name) using UpstreamPublishedAt if present else max Version
if 'UpstreamPublishedAt' in pkg_df.columns:
    pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
    pkg_df_sorted = pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'], ascending=[True, False, False])
else:
    pkg_df_sorted = pkg_df.sort_values(['Name','Version'], ascending=[True, False])
latest_pkg = pkg_df_sorted.drop_duplicates(subset=['Name'], keep='first')[['Name','Version']]

# join with projpkg to get ProjectName for those versions
merged = latest_pkg.merge(projpkg_df, on=['Name','Version'], how='inner')

# parse stars from Project_Information
stars = []
for info in projinfo_df['Project_Information']:
    m = re.search(r"(\d[\d,]*) stars", info)
    if m:
        stars.append(int(m.group(1).replace(',','')))
    else:
        stars.append(None)
projinfo_df['Stars'] = stars

# need project name in projinfo; parse "project owner/repo" or "named owner/repo" patterns
project_names = []
for info in projinfo_df['Project_Information']:
    m = re.search(r"project ([^\s/]+/[^\s, ]+)", info)
    if not m:
        m = re.search(r"named ([^\s/]+/[^\s, ]+)", info)
    if not m:
        m = re.search(r"repository named ([^\s/]+/[^\s, ]+)", info)
    project_names.append(m.group(1) if m else None)
projinfo_df['ProjectName'] = project_names

# join merged with projinfo on ProjectName
merged2 = merged.merge(projinfo_df[['ProjectName','Stars']], on='ProjectName', how='left')

# get top 5 by Stars
merged2 = merged2.dropna(subset=['Stars'])
merged2 = merged2.sort_values('Stars', ascending=False)
top5 = merged2[['Name','Version','ProjectName','Stars']].drop_duplicates(subset=['Name']).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Hbey6xNOqMjaSZ1IVysH5JaU': 'file_storage/call_Hbey6xNOqMjaSZ1IVysH5JaU.json', 'var_call_MdpyJgu8fAkYLLBHUPFCaQCZ': ['project_info', 'project_packageversion'], 'var_call_eZWUAUoRnlsdMSQHJozG19dk': 'file_storage/call_eZWUAUoRnlsdMSQHJozG19dk.json', 'var_call_7OhoaPgW1C5dLeaD6ZqMNMA8': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0'}], 'var_call_LUw1h1Su5h6sxcUq1gRNdq2z': 'file_storage/call_LUw1h1Su5h6sxcUq1gRNdq2z.json'}

exec(code, env_args)
