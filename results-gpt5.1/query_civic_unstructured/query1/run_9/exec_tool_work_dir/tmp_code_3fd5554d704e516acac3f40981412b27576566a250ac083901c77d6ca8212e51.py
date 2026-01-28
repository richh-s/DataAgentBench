code = """import json, pandas as pd, os

funding_records = var_call_PtCHFclPSCzAKb50dh3eh65w
funding_df = pd.DataFrame(funding_records)
funding_df['Project_Name_norm'] = funding_df['Project_Name'].str.strip()

civic_source = var_call_VAvR9cqYv8JlSU9becDNKVPQ
if isinstance(civic_source, str):
    with open(civic_source, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_source

texts = [d.get('text', '') for d in civic_docs]
full_text = '\n'.join(texts)

projects = {}

# Build a set once
funding_names = set(funding_df['Project_Name_norm'])

for raw_line in full_text.split('\n'):
    l = raw_line.strip()
    if not l:
        continue
    if len(l) < 4 or len(l) > 120:
        continue
    if any(h in l for h in ['Agenda Item', 'Public Works Commission', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Updates:', 'Project Description', 'Project Schedule', 'Estimated Schedule']):
        continue
    if l in funding_names:
        projects.setdefault(l, {'status': None, 'type': 'capital'})

status_map = {}
current_section = None
for raw_line in full_text.split('\n'):
    l = raw_line.strip()
    if not l:
        continue
    low = l.lower()
    if 'capital improvement projects (design)' in low:
        current_section = 'design'
        continue
    if 'capital improvement projects (construction)' in low:
        current_section = 'completed'
        continue
    if 'capital improvement projects (not started)' in low:
        current_section = 'not started'
        continue
    if current_section and not any(k in low for k in ['updates:', 'project description', 'project schedule', 'estimated schedule', 'agenda item', 'public works commission']):
        name = l
        if name in funding_names:
            status_map[name] = current_section

for name, status in status_map.items():
    projects.setdefault(name, {'type': 'capital', 'status': status})
    projects[name]['status'] = status

proj_rows = []
for name, info in projects.items():
    proj_rows.append({'Project_Name_norm': name, 'status': info.get('status'), 'type': info.get('type')})

proj_df = pd.DataFrame(proj_rows)

merged = funding_df.merge(proj_df, on='Project_Name_norm', how='inner')
merged['Amount_num'] = pd.to_numeric(merged['Amount'])
mask = (merged['type'] == 'capital') & (merged['status'] == 'design') & (merged['Amount_num'] > 50000)
count = int(mask.sum())

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_PtCHFclPSCzAKb50dh3eh65w': 'file_storage/call_PtCHFclPSCzAKb50dh3eh65w.json', 'var_call_VAvR9cqYv8JlSU9becDNKVPQ': 'file_storage/call_VAvR9cqYv8JlSU9becDNKVPQ.json'}

exec(code, env_args)
