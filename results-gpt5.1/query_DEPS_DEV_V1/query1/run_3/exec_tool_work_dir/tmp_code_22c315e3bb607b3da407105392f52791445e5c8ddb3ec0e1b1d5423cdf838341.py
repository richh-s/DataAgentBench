code = """import json, re, pandas as pd

# Load latest NPM package versions
latest_file = var_call_uwmdauWmUiDvUO7f04I2IDrU
with open(latest_file, 'r') as f:
    latest = json.load(f)
latest_df = pd.DataFrame(latest)

# Load project_packageversion
ppv_file = var_call_3BqG0mb5aUcX1QbK0fDxNUVo
with open(ppv_file, 'r') as f:
    ppv = json.load(f)
ppv_df = pd.DataFrame(ppv)

# Keep only NPM system and join to latest versions
ppv_df = ppv_df[ppv_df['System'] == 'NPM']
merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# Now load project_info and parse project names and stars from Project_Information
pi_file = var_call_jyjGfGGym5irqXx5hZ3LHc0p
with open(pi_file, 'r') as f:
    pi = json.load(f)
pi_df = pd.DataFrame(pi)

# Extract ProjectName (owner/repo) and stars count from text
name_pattern = re.compile(r'project ([^\s]+/[^\s]+)')
stars_pattern = re.compile(r'(?:has|with|,|currently has|, currently has[^,]*,|currently has an open issues count of [0-9]+, a stars count of) ([0-9,]+) stars')

project_rows = []
for _, row in pi_df.iterrows():
    text = row['Project_Information']
    name_match = name_pattern.search(text)
    if not name_match:
        continue
    name = name_match.group(1)
    stars_match = re.search(r'([0-9,]+) stars', text)
    if not stars_match:
        continue
    stars = int(stars_match.group(1).replace(',', ''))
    project_rows.append({'ProjectName': name, 'Stars': stars})

proj_df = pd.DataFrame(project_rows).drop_duplicates(subset=['ProjectName'])

# Join merged with proj_df on ProjectName
full = merged.merge(proj_df, on='ProjectName', how='inner')

# For each package (Name) keep max Stars (in case multiple projects) and associated version
idx = full.groupby('Name')['Stars'].idxmax()
top_packages = full.loc[idx, ['Name','Version','Stars']]

# Get top 5 by Stars
top5 = top_packages.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9eeFg4DvN4LPmUFHSsZcmrdg': 'file_storage/call_9eeFg4DvN4LPmUFHSsZcmrdg.json', 'var_call_NFjIoKmOhFgffSzw4MH8k63g': ['project_info', 'project_packageversion'], 'var_call_uwmdauWmUiDvUO7f04I2IDrU': 'file_storage/call_uwmdauWmUiDvUO7f04I2IDrU.json', 'var_call_3BqG0mb5aUcX1QbK0fDxNUVo': 'file_storage/call_3BqG0mb5aUcX1QbK0fDxNUVo.json', 'var_call_kB0Aq7mb70MJYzYC7J53IXnI': ['project_info', 'project_packageversion'], 'var_call_jyjGfGGym5irqXx5hZ3LHc0p': 'file_storage/call_jyjGfGGym5irqXx5hZ3LHc0p.json'}

exec(code, env_args)
