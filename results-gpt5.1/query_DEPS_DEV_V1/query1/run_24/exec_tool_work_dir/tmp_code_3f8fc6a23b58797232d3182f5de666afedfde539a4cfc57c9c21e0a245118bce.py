code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_AvSKkB0AkBvYPLQDVEPSFI9G, 'r') as f:
    npm_packages = json.load(f)
with open(var_call_72NPNBqIjENdnfSyFSyH9jjY, 'r') as f:
    project_pkg = json.load(f)
with open(var_call_unl9owdgJpXiQrM3ZuExOsc9, 'r') as f:
    project_info = json.load(f)

# DataFrames
pkg_df = pd.DataFrame(npm_packages)[['System','Name','Version']].drop_duplicates()
proj_pkg_df = pd.DataFrame(project_pkg)[['System','Name','Version','ProjectName']].drop_duplicates()
proj_info_df = pd.DataFrame(project_info)[['rowid','Project_Information']]

# Determine latest version per package (lexicographically, as no better info)
latest_df = pkg_df.sort_values('Version').groupby(['System','Name'], as_index=False).tail(1)

# Join with project_packageversion to get ProjectName
merged = latest_df.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

# Extract owner/repo from Project_Information text using pattern 'The project X on GitHub' or 'hosted on GitHub under the name X'
def extract_repo(info):
    m = re.search(r'The project ([^ ]+/[^ ]+) on GitHub', info)
    if m:
        return m.group(1)
    m = re.search(r'hosted on GitHub under the name ([^ ,]+)', info)
    if m:
        return m.group(1)
    m = re.search(r'named ([^ ]+/[^ ]+) on GitHub', info)
    if m:
        return m.group(1)
    return None

# Extract stars
def extract_stars(info):
    m = re.search(r'(?:a |has |, )([0-9,]+) stars', info)
    if m:
        return int(m.group(1).replace(',', ''))
    return None

proj_info_df['Repo'] = proj_info_df['Project_Information'].apply(extract_repo)
proj_info_df['Stars'] = proj_info_df['Project_Information'].apply(extract_stars)

# Map repo -> max stars (in case of duplicates)
repo_stars = proj_info_df.dropna(subset=['Repo','Stars']).groupby('Repo')['Stars'].max().reset_index()

# merged ProjectName is owner/repo already, match exactly
merged2 = merged.merge(repo_stars, left_on='ProjectName', right_on='Repo', how='left')

# Keep rows with stars
merged2 = merged2.dropna(subset=['Stars'])

# For each package name, keep the one with highest stars (though should be unique)
pkg_pop = merged2.sort_values('Stars', ascending=False).groupby('Name', as_index=False).head(1)

# Top 5
top5 = pkg_pop.sort_values('Stars', ascending=False).head(5)[['Name','Version','Stars']]

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AvSKkB0AkBvYPLQDVEPSFI9G': 'file_storage/call_AvSKkB0AkBvYPLQDVEPSFI9G.json', 'var_call_72NPNBqIjENdnfSyFSyH9jjY': 'file_storage/call_72NPNBqIjENdnfSyFSyH9jjY.json', 'var_call_zE2vCphE0zSPKttOdVVhF2f0': ['project_info', 'project_packageversion'], 'var_call_unl9owdgJpXiQrM3ZuExOsc9': 'file_storage/call_unl9owdgJpXiQrM3ZuExOsc9.json'}

exec(code, env_args)
