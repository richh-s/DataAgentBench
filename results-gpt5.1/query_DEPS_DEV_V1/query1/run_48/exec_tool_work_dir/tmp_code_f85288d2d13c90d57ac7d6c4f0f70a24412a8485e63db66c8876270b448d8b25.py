code = """import json, re, pandas as pd, os

# load latest package versions
with open(var_call_IWLyNJC29Vr42TNhBPk1ozP6) as f:
    latest = pd.DataFrame(json.load(f))

# load project_packageversion
with open(var_call_xieQDn2cv26fcaAtXJusINOD) as f:
    ppv = pd.DataFrame(json.load(f))

# join to get project names for latest versions
merged = latest.merge(ppv, on=['System','Name','Version'], how='inner')

# extract project name and stars from project_info
with open(var_call_kNX9wZ5U0yF8zdwklGcIUwGs) as f:
    pi_raw = json.load(f)

proj_rows = []
pat = re.compile(r'The project (.*?) (?:is hosted on GitHub|on GitHub|is hosted on GITHUB|is hosted on GITHUB and|is hosted on GitHub and|is hosted on GITHUB and currently|is hosted on GitHub and currently|is a GitHub repository named|is hosted on GitHub under the name|on GitHub, named|is hosted on GitHub under the name)')
stars_pat = re.compile(r'(\d[\d,]*) stars')
for row in pi_raw:
    text = row['Project_Information']
    m = pat.search(text)
    if not m:
        continue
    name = m.group(1).strip().rstrip(',')
    sm = stars_pat.search(text)
    if not sm:
        continue
    stars = int(sm.group(1).replace(',',''))
    proj_rows.append({'ProjectName': name, 'Stars': stars})

proj_df = pd.DataFrame(proj_rows).drop_duplicates('ProjectName')

# merged ProjectName vs proj_df ProjectName must match exactly
full = merged.merge(proj_df, on='ProjectName', how='inner')

# get top 5 by stars
full_top = full.sort_values('Stars', ascending=False).drop_duplicates('Name').head(5)

result = full_top[['Name','Version','Stars']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_B9rXac9rbbvyCqKvbr6prM7O': ['project_info', 'project_packageversion'], 'var_call_yjHuHL7V1r8J8XtV3HY1WvEV': 'file_storage/call_yjHuHL7V1r8J8XtV3HY1WvEV.json', 'var_call_IWLyNJC29Vr42TNhBPk1ozP6': 'file_storage/call_IWLyNJC29Vr42TNhBPk1ozP6.json', 'var_call_xieQDn2cv26fcaAtXJusINOD': 'file_storage/call_xieQDn2cv26fcaAtXJusINOD.json', 'var_call_kNX9wZ5U0yF8zdwklGcIUwGs': 'file_storage/call_kNX9wZ5U0yF8zdwklGcIUwGs.json'}

exec(code, env_args)
