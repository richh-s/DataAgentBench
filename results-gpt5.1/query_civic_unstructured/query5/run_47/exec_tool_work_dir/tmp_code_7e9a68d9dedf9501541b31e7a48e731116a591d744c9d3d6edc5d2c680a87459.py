code = """import re, json, pandas as pd

# Load full funding data
path = var_call_moMpq9elWdA7rcb8Kiy51Xid
with open(path, 'r') as f:
    funding = json.load(f)

# Disaster-related projects: names containing FEMA, CalOES, or CalJPIA
rows = []
for row in funding:
    name = row['Project_Name']
    if re.search(r'(FEMA|CalOES|CalJPIA)', name, re.IGNORECASE):
        rows.append(row)

# For these, determine which started in 2022 using civic docs text heuristics
path_docs = var_call_yB3fYNwD5EaeqVH7te7rNXbK
with open(path_docs, 'r') as f:
    docs = json.load(f)

text_all = ' '.join(d['text'] for d in docs).lower()

# Heuristic: if the project name appears near a 2022 date in docs text, treat as started 2022
projects_2022 = set()
for row in rows:
    name = row['Project_Name']
    # use a simplified key fragment (first 5 words)
    key = ' '.join(name.lower().split()[:5])
    if not key:
        continue
    idx = text_all.find(key)
    if idx == -1:
        continue
    window = text_all[max(0, idx-150): idx+150]
    if '2022' in window:
        projects_2022.add(name)

# Sum funding for those projects
total = 0
for row in rows:
    if row['Project_Name'] in projects_2022:
        try:
            total += int(row['Amount'])
        except Exception:
            pass

result = {"total_funding_disaster_2022": total, "projects": sorted(list(projects_2022))}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_yB3fYNwD5EaeqVH7te7rNXbK': 'file_storage/call_yB3fYNwD5EaeqVH7te7rNXbK.json', 'var_call_moMpq9elWdA7rcb8Kiy51Xid': 'file_storage/call_moMpq9elWdA7rcb8Kiy51Xid.json'}

exec(code, env_args)
