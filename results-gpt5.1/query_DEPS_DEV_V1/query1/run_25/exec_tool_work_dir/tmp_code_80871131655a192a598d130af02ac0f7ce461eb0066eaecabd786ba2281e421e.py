code = """import json, pandas as pd, re

# load latest npm versions
with open(var_call_w5tAnxgUSh4fx8jXsbXdOOtM) as f:
    latest = pd.DataFrame(json.load(f))

# load project_packageversion
with open(var_call_4RmTHmwxE9PJLBZEfv7goeEU) as f:
    ppv = pd.DataFrame(json.load(f))

ppv_npm = ppv[ppv['System']=='NPM'][['System','Name','Version','ProjectName']].drop_duplicates()

# join latest versions with project mappings
merged = pd.merge(latest, ppv_npm, on=['System','Name','Version'], how='inner')

# load project_info
with open(var_call_CWDmr4kyUGG9LIUixHUAzsIX) as f:
    pinfo = pd.DataFrame(json.load(f))

# extract owner/repo and stars from Project_Information text
def parse_info(text):
    if not isinstance(text,str):
        return None, None
    m = re.search(r'project ([^\s/]+/[^\s]+)', text)
    repo = m.group(1) if m else None
    m2 = re.search(r'(?:has|count of|of) ([0-9,]+) stars', text)
    stars = int(m2.group(1).replace(',','')) if m2 else None
    return repo, stars

pinfo[['Repo','Stars']] = pinfo['Project_Information'].apply(lambda t: pd.Series(parse_info(t)))

# join merged with project_info on repo name
merged2 = pd.merge(merged, pinfo, left_on='ProjectName', right_on='Repo', how='left')

# aggregate to latest per package name, taking max stars
agg = merged2.groupby(['Name']).agg({'Version':'first','Stars':'max'}).reset_index()
agg = agg.dropna(subset=['Stars'])

# top 5 by stars
top5 = agg.sort_values('Stars', ascending=False).head(5)

result = top5[['Name','Version','Stars']].to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_B2DybEJRJEJVmKVztz8A2BIF': 'file_storage/call_B2DybEJRJEJVmKVztz8A2BIF.json', 'var_call_lFVYvaUDRjkxTW2shNUSEEFW': ['project_info', 'project_packageversion'], 'var_call_pAiCfWbstuO55H57wwotWtHR': 'file_storage/call_pAiCfWbstuO55H57wwotWtHR.json', 'var_call_4RmTHmwxE9PJLBZEfv7goeEU': 'file_storage/call_4RmTHmwxE9PJLBZEfv7goeEU.json', 'var_call_CWDmr4kyUGG9LIUixHUAzsIX': 'file_storage/call_CWDmr4kyUGG9LIUixHUAzsIX.json', 'var_call_w5tAnxgUSh4fx8jXsbXdOOtM': 'file_storage/call_w5tAnxgUSh4fx8jXsbXdOOtM.json'}

exec(code, env_args)
