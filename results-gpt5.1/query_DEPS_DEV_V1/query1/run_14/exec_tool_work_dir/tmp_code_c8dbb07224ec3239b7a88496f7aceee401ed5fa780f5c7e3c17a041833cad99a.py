code = """import json, re, pandas as pd

# Load all project_info records
with open(var_call_qDuAfzPXc0Wj4YkXXV3VNIiq, 'r') as f:
    proj_info = json.load(f)

# Extract repo name and stars from Project_Information text
rows = []
for rec in proj_info:
    text = rec.get('Project_Information','')
    m_repo = re.search(r'project\s+([^\s]+/[^\s]+)', text)
    m_stars = re.search(r'(?:has|with|a)\s+total of\s+([0-9,]+)\s+stars|stars count of\s+([0-9,]+)|([0-9,]+)\s+stars', text)
    if not m_repo or not m_stars:
        continue
    repo = m_repo.group(1)
    stars = None
    for g in m_stars.groups():
        if g:
            stars = int(g.replace(',', ''))
            break
    if stars is None:
        continue
    rows.append({'ProjectName': repo, 'Stars': stars})

proj_stars_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

# Load previous join result sample to infer linking, but we need full latest_with_proj; can't access from here, so recompute minimal join again using stored files
with open(var_call_jNPi455iwHeYaYsZeY57uqs1, 'r') as f:
    pkginfo = json.load(f)
with open(var_call_uJDcnvkWsqG4krz2tKwObVwE, 'r') as f:
    proj_pkg = json.load(f)

pkg_df = pd.DataFrame(pkginfo)[['System','Name','Version']]
proj_pkg_df = pd.DataFrame(proj_pkg)[['System','Name','Version','ProjectName']]

pkg_df = pkg_df[pkg_df['System']=='NPM']
proj_pkg_df = proj_pkg_df[proj_pkg_df['System']=='NPM']

latest_versions = pkg_df.groupby('Name')['Version'].max().reset_index().rename(columns={'Version':'LatestVersion'})
latest_pkg = pd.merge(latest_versions, pkg_df, left_on=['Name','LatestVersion'], right_on=['Name','Version'], how='inner')
latest_with_proj = pd.merge(latest_pkg[['Name','Version']], proj_pkg_df, on=['Name','Version'], how='inner')

# Join latest_with_proj with proj_stars_df on ProjectName
latest_with_stars = pd.merge(latest_with_proj, proj_stars_df, on='ProjectName', how='inner')

# For each package Name, keep max Stars (some packages may map to multiple repos, rare)
pkg_star = latest_with_stars.groupby(['Name','Version'])['Stars'].max().reset_index()

# Top 5 by Stars
top5 = pkg_star.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jNPi455iwHeYaYsZeY57uqs1': 'file_storage/call_jNPi455iwHeYaYsZeY57uqs1.json', 'var_call_uJDcnvkWsqG4krz2tKwObVwE': 'file_storage/call_uJDcnvkWsqG4krz2tKwObVwE.json', 'var_call_qgsCTVFvapIHh1x30M51GPOL': [{'Name': '@discordx/music', 'Version': '6.0.2', 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '4.0.0-dev.1670073642.4821b1ea', 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '4.0.0-dev.1670073642.4821b1ea', 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '4.0.0-dev.1670073642.4821b1ea', 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '4.0.0-dev.1670073642.4821b1ea', 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/utilities', 'Version': '6.0.0-dev.1674756406.d6dc0b9d', 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/utilities', 'Version': '6.0.0-dev.1674756406.d6dc0b9d', 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}], 'var_call_qDuAfzPXc0Wj4YkXXV3VNIiq': 'file_storage/call_qDuAfzPXc0Wj4YkXXV3VNIiq.json'}

exec(code, env_args)
