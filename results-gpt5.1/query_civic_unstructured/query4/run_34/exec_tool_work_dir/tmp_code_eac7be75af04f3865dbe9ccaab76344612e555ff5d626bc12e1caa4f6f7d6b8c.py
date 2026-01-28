code = """import re, json, pandas as pd

mongo_path = var_call_HcJ4zT6RRMEWGcK3EnzNeC7B
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

projects = []
for doc in mongo_docs:
    text = doc.get('text','')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    current_project = None
    for line in lines:
        if re.match(r'^[A-Z0-9].*(Project|Improvements|Repairs|Study|Facility|Playground|Park|Biofilter|Signals Backup Power)$', line) and 'Agenda' not in line and 'Projects' not in line:
            current_project = line
        if current_project:
            m = re.search(r'(Begin (Construction|Design)|Start|Project Schedule).*?(Spring 2022|2022-Spring)', line, re.IGNORECASE)
            if m:
                projects.append({'Project_Name': current_project, 'st': '2022-Spring'})
                current_project = None

unique_projects = {}
for p in projects:
    unique_projects[p['Project_Name']] = p['st']

spring2022_projects = list(unique_projects.keys())

funding_path = var_call_dCcVq5iK1QCoIyf7avSdYkeE
with open(funding_path, 'r') as f:
    funding = json.load(f)

f_df = pd.DataFrame(funding)
f_df['Amount'] = f_df['Amount'].astype(int)
mask = f_df['Project_Name'].isin(spring2022_projects)
matched = f_df[mask]

result = {
    'spring_2022_project_count': int(mask.sum()),
    'spring_2022_total_funding': int(matched['Amount'].sum()),
    'spring2022_projects': spring2022_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HcJ4zT6RRMEWGcK3EnzNeC7B': 'file_storage/call_HcJ4zT6RRMEWGcK3EnzNeC7B.json', 'var_call_dCcVq5iK1QCoIyf7avSdYkeE': 'file_storage/call_dCcVq5iK1QCoIyf7avSdYkeE.json'}

exec(code, env_args)
