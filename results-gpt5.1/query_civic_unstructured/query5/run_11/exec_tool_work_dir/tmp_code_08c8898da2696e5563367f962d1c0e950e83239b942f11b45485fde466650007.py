code = """import re, json, pandas as pd

path = var_call_NM0ZyMu9Tei19S2JtBRoTSMN
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = '\n'.join(d.get('text','') for d in civic_docs)
lines = [l.strip() for l in texts.split('\n') if l.strip()]
projects = []
for l in lines:
    if re.search(r'\b20(19|20|21|22|23|24)\b', l):
        disaster = bool(re.search(r'FEMA|CalOES|CalJPIA|disaster|fire', l, re.I))
        if disaster:
            projects.append(l)

proj_2022 = [p for p in projects if '2022' in p]
cleaned = []
for p in proj_2022:
    c = re.split(r'  | - ', p)[0].strip(' :')
    cleaned.append(c)
unique_projects_2022 = sorted(set(cleaned))

funding_path = var_call_kmbgxlRh9ZXbDRoMUktU6ExY
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

fdf = pd.DataFrame(funding_records)
fdf['Amount'] = fdf['Amount'].astype(int)
mask_disaster = fdf['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, regex=True)
if unique_projects_2022:
    name_mask = fdf['Project_Name'].isin(unique_projects_2022)
    mask_disaster = mask_disaster | name_mask
mask_2022 = fdf['Project_Name'].str.contains('2022')

target = fdf[mask_disaster & mask_2022]

total_funding = int(target['Amount'].sum())
result = {"total_funding_disaster_started_2022": total_funding,
          "matched_project_names": target['Project_Name'].tolist()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NM0ZyMu9Tei19S2JtBRoTSMN': 'file_storage/call_NM0ZyMu9Tei19S2JtBRoTSMN.json', 'var_call_kmbgxlRh9ZXbDRoMUktU6ExY': 'file_storage/call_kmbgxlRh9ZXbDRoMUktU6ExY.json'}

exec(code, env_args)
