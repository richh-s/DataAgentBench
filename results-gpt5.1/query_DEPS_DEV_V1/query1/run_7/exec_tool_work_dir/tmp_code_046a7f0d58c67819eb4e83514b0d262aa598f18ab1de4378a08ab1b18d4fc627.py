code = """import pandas as pd, json, re

# Load full project_packageversion and project_info
with open(var_call_4DklVgFjNvduTbppym443oOc, 'r') as f:
    pp_rows = json.load(f)
with open(var_call_QaAMedsQtcFkDP9W52BRQOuz, 'r') as f:
    pi_rows = json.load(f)

pp = pd.DataFrame(pp_rows)
pi = pd.DataFrame(pi_rows)

# Keep only NPM system
pp = pp[pp['System'] == 'NPM']

# For each (Name), keep row with max Version lexicographically as approximation of latest
pp_latest = pp.sort_values(['Name','Version']).groupby('Name', as_index=False).tail(1)

# Parse stars from Project_Information using regex "(\d[\d,]*) stars"
pi['Stars'] = pi['Project_Information'].str.extract(r'(\d[\d,]*) stars')[0]
pi['Stars'] = pi['Stars'].str.replace(',', '').astype(float)

# Need mapping from ProjectName to Project_Information; but project_info lacks explicit ProjectName.
# Try to infer owner/repo from text: pattern "project ([^\s/]+/[^\s]+)" or "named ([^\s/]+/[^\s]+)" or "on GitHub, named ([^\s/]+/[^\s]+)" etc.
patterns = [
    r'project ([^\s/]+/[^\s,]+)',
    r'project named ([^\s/]+/[^\s,]+)',
    r'named ([^\s/]+/[^\s,]+)',
    r'GitHub, ([^\s/]+/[^\s,]+)'
]

def extract_repo(text):
    if not isinstance(text, str):
        return None
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            return m.group(1)
    return None

pi['ProjectName'] = pi['Project_Information'].apply(extract_repo)

pi_valid = pi.dropna(subset=['ProjectName','Stars'])

# Join latest package versions with project info via ProjectName
merged = pd.merge(pp_latest, pi_valid, on='ProjectName', how='inner')

# Now for each package Name, we already limited to latest version in pp_latest; select top 5 by Stars
merged_top = merged.sort_values('Stars', ascending=False).head(5)

result = merged_top[['Name','Version','ProjectName','Stars']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_nyrbYaNUMrfMgO7qvjkRDmMK': 'file_storage/call_nyrbYaNUMrfMgO7qvjkRDmMK.json', 'var_call_TjSktaNgsJRC5SF2Yh2OGJ33': ['project_info', 'project_packageversion'], 'var_call_4DklVgFjNvduTbppym443oOc': 'file_storage/call_4DklVgFjNvduTbppym443oOc.json', 'var_call_QaAMedsQtcFkDP9W52BRQOuz': 'file_storage/call_QaAMedsQtcFkDP9W52BRQOuz.json', 'var_call_tYIbdugeDVMCuaakp7bI7qN0': 'file_storage/call_tYIbdugeDVMCuaakp7bI7qN0.json'}

exec(code, env_args)
