code = """import re, json, pandas as pd

path_docs = var_call_lUjKkYUvnw5QmqGxnS0dfDbB
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_Sig9nD9Ha3fUy4O9U22gjlZf)
funding['Amount'] = funding['Amount'].astype(int)

texts = ' '.join(d['text'] for d in civic_docs)

projects = {}
for line in texts.split('\n'):
    line_stripped = line.strip()
    if not line_stripped:
        continue
    if any(k in line_stripped for k in ['Park', 'park', 'Playground', 'playground']):
        name = line_stripped
        if len(name.split()) < 2 or len(name) > 120:
            continue
        if name not in projects:
            projects[name] = {"Project_Name": name, "topic": [], "status": None, "et": None}

current_name = None
for line in texts.split('\n'):
    s = line.strip()
    if s in projects:
        current_name = s
        continue
    if not current_name:
        continue
    lower = s.lower()
    if 'construction was completed' in lower:
        m = re.search(r'(20\d{2})', s)
        year = m.group(1) if m else None
        projects[current_name]['status'] = 'completed'
        projects[current_name]['et'] = year
    elif 'notice of completion filed' in lower:
        m = re.search(r'(20\d{2})', s)
        year = m.group(1) if m else None
        if not projects[current_name]['status']:
            projects[current_name]['status'] = 'completed'
        if not projects[current_name]['et']:
            projects[current_name]['et'] = year

proj_df = pd.DataFrame(projects.values())
if proj_df.empty:
    total_funding = 0
    detail = []
else:
    proj_df['is_park'] = proj_df['Project_Name'].str.contains('Park', case=False, na=False)
    mask_2022 = (proj_df['status'] == 'completed') & (proj_df['et'] == '2022')
    proj_2022_park = proj_df[mask_2022 & proj_df['is_park']]
    merged = funding.merge(proj_2022_park[['Project_Name']], on='Project_Name', how='inner')
    total_funding = int(merged['Amount'].sum()) if not merged.empty else 0
    detail = merged[['Project_Name','Amount']].to_dict(orient='records')

result = {"total_funding_park_completed_2022": total_funding, "projects": detail}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lUjKkYUvnw5QmqGxnS0dfDbB': 'file_storage/call_lUjKkYUvnw5QmqGxnS0dfDbB.json', 'var_call_Sig9nD9Ha3fUy4O9U22gjlZf': 'file_storage/call_Sig9nD9Ha3fUy4O9U22gjlZf.json'}

exec(code, env_args)
