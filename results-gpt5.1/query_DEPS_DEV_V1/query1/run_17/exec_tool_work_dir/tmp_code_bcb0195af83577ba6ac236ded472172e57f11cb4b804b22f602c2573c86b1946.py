code = """import json, re, pandas as pd

# Load full data from files
with open(var_call_xHpIOd1m4speHDjnhcYXJTjC, 'r') as f:
    npm_packages = json.load(f)
with open(var_call_lRpGpdOLEkZ8M22n15TPBu9x, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_k57fTO9WTv2Z4JQ65KeFCjJU, 'r') as f:
    proj_info = json.load(f)

# Convert to DataFrames
df_packages = pd.DataFrame(npm_packages)[['Name','Version']]
df_proj_pkg = pd.DataFrame(proj_pkg)[['Name','Version','ProjectName']]
df_proj_info = pd.DataFrame(proj_info)[['Project_Information']]

# Extract owner/repo and stars from Project_Information
proj_pattern = re.compile(r"project ([^\s/]+/[^\s ]+) .*? (?:has|currently has|is hosted on GitHub and currently has).*? (?:a )?stars? count of (\d+)|project ([^\s/]+/[^\s ]+) on GitHub .*? (\d+) stars|named ([^\s/]+/[^\s ]+) .*? (\d+) stars|under the name ([^\s/]+/[^\s ]+), .*? (\d+) stars|The project ([^\s/]+/[^\s ]+) on GitHub .*? (\d+) stars|The project ([^\s/]+/[^\s ]+) is hosted on GitHub and currently has .*? (\d+) stars|The project ([^\s/]+/[^\s ]+) is hosted on GITHUB and currently has .*? (\d+) stars|The project on GitHub, named ([^\s/]+/[^\s ]+), currently has .*? (\d+) stars|The project is a GitHub repository named ([^\s/]+/[^\s ]+), which currently has .*? (\d+) stars|The project is hosted on GitHub under the name ([^\s/]+/[^\s ]+), and it currently has .*? (\d+) stars|The GitHub project ([^\s/]+/[^\s ]+) currently has .*? (\d+) stars|The GitHub project named ([^\s/]+/[^\s ]+) has .*? (\d+) stars|The GitHub project named ([^\s/]+/[^\s ]+) currently has .*? (\d+) stars")

repos = []
for row in df_proj_info['Project_Information']:
    text = row
    m = proj_pattern.search(text)
    repo = None
    stars = None
    if m:
        groups = m.groups()
        # pairs of (repo, stars)
        for i in range(0, len(groups), 2):
            repo_g = groups[i]
            star_g = groups[i+1]
            if repo_g and star_g is not None:
                repo = repo_g
                stars = int(star_g)
                break
    if repo and stars is not None:
        repos.append({'ProjectName': repo, 'Stars': stars})

df_repos = pd.DataFrame(repos).drop_duplicates('ProjectName')

# Determine latest version per NPM package from packageinfo (lexicographically as proxy)
idx = df_packages.groupby('Name')['Version'].transform(max) == df_packages['Version']
latest_packages = df_packages[idx].drop_duplicates(['Name','Version'])

# Join latest packages with project_packageversion on Name & Version
merged = latest_packages.merge(df_proj_pkg, on=['Name','Version'], how='inner')

# Join with repo stars
merged = merged.merge(df_repos, on='ProjectName', how='inner')

# For each package (Name), keep max stars across projects
pkg_stars = merged.groupby(['Name','Version'])['Stars'].max().reset_index()

# Top 5 by stars
top5 = pkg_stars.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xHpIOd1m4speHDjnhcYXJTjC': 'file_storage/call_xHpIOd1m4speHDjnhcYXJTjC.json', 'var_call_lRpGpdOLEkZ8M22n15TPBu9x': 'file_storage/call_lRpGpdOLEkZ8M22n15TPBu9x.json', 'var_call_k57fTO9WTv2Z4JQ65KeFCjJU': 'file_storage/call_k57fTO9WTv2Z4JQ65KeFCjJU.json'}

exec(code, env_args)
