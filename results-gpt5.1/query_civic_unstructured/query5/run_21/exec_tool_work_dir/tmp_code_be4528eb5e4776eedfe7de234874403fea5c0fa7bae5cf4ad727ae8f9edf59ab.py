code = """import re, json, pandas as pd

path_docs = var_call_Dg5uzapwP1ujVhYYgJQvMc5t
with open(path_docs, 'r') as f:
    docs = json.load(f)

texts = ' '.join(d['text'] for d in docs)
lines = [l.strip() for l in texts.split('\n') if l.strip()]

projects = []
current_project = None
for line in lines:
    if (('Project' in line or 'project' in line) and len(line) < 120 and not line.endswith(':')):
        current_project = {'Project_Name': line, 'st': None, 'et': None}
        projects.append(current_project)
    elif current_project:
        m = re.search(r'(20\d{2}[^,;\)]{0,15})', line)
        if m and current_project['st'] is None:
            current_project['st'] = m.group(1).strip()

projects_2022 = [p for p in projects if p['st'] and '2022' in p['st']]
for p in projects_2022:
    name = p['Project_Name']
    p['type'] = 'disaster' if any(k in name for k in ['FEMA', 'CalOES', 'CalJPIA', 'Disaster']) else 'capital'

projects_2022_disaster = [p for p in projects_2022 if p['type']=='disaster']

path_funding = var_call_aHaYOMsn0aY193WahCq4OnFC
with open(path_funding, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

proj_df = pd.DataFrame(projects_2022_disaster)

if proj_df.empty:
    total = 0
else:
    merged = fund_df.merge(proj_df, on='Project_Name', how='inner')
    total = int(merged['Amount'].sum()) if not merged.empty else 0

print('__RESULT__:')
print(json.dumps(total))"""

env_args = {'var_call_Dg5uzapwP1ujVhYYgJQvMc5t': 'file_storage/call_Dg5uzapwP1ujVhYYgJQvMc5t.json', 'var_call_aHaYOMsn0aY193WahCq4OnFC': 'file_storage/call_aHaYOMsn0aY193WahCq4OnFC.json'}

exec(code, env_args)
