code = """import json, re, pandas as pd

# Load full funding data
with open(var_call_XXmVHMJJ9dXlckLqQ90I5Twn, 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)
# Disaster projects contain FEMA, CalOES, or CalJPIA in the name
mask_disaster = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, regex=True)
disaster_funding = funding_df[mask_disaster].copy()

# We need projects that STARTED in 2022. Use civic docs text to infer start dates.
with open(var_call_d074K1pp4cC1REprkZSjYz1l, 'r') as f:
    docs = json.load(f)

texts = ' '.join(d['text'] for d in docs)

# Heuristic: if a project name appears near a 2022 date phrase, assume it started in 2022
# Build dict of project_name -> started_2022 bool
started_2022 = {}
for name in disaster_funding['Project_Name']:
    pattern = re.escape(name[:40].split('(')[0].strip())
    if not pattern:
        started_2022[name] = False
        continue
    regex = re.compile(pattern + r".{0,80}2022", re.IGNORECASE)
    started_2022[name] = bool(regex.search(texts))

disaster_funding['Started_2022'] = disaster_funding['Project_Name'].map(started_2022)

selected = disaster_funding[disaster_funding['Started_2022']]

# Amounts are strings; convert to int
selected['Amount'] = selected['Amount'].astype(int)

total = int(selected['Amount'].sum())

result = {"total_funding_2022_disaster_projects": total, "projects": selected[['Project_Name','Amount']].to_dict(orient='records')}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_d074K1pp4cC1REprkZSjYz1l': 'file_storage/call_d074K1pp4cC1REprkZSjYz1l.json', 'var_call_XXmVHMJJ9dXlckLqQ90I5Twn': 'file_storage/call_XXmVHMJJ9dXlckLqQ90I5Twn.json'}

exec(code, env_args)
