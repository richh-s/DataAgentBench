code = """import re, json, pandas as pd

# Load funding data
funding_records = var_call_PtCHFclPSCzAKb50dh3eh65w
funding_df = pd.DataFrame(funding_records)

# Normalize project names from funding
funding_df['Project_Name_norm'] = funding_df['Project_Name'].str.strip()

# Load civic docs text
civic_source = var_call_VAvR9cqYv8JlSU9becDNKVPQ

# civic_source may be a path (string) or a list; handle both
if isinstance(civic_source, str):
    import os, json as js
    with open(civic_source, 'r') as f:
        civic_docs = js.load(f)
else:
    civic_docs = civic_source

texts = [d.get('text','') for d in civic_docs]
full_text = '\n'.join(texts)

# Heuristic extraction: look for section "Capital Improvement Projects" and statuses
projects = {}

# Simple pattern: lines that look like project titles (no colon, not too long) near keywords
for line in full_text.split('\n'):
    l = line.strip()
    if not l:
        continue
    # Skip generic headers
    if len(l) < 4 or len(l) > 120:
        continue
    if any(h in l for h in ['Agenda Item', 'Public Works Commission', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Updates:', 'Project Description', 'Project Schedule', 'Estimated Schedule']):
        continue
    # We know some capital project names directly from hint/funding; collect those that appear in funding
    if l in set(funding_df['Project_Name_norm']):
        # Determine status heuristically from surrounding text
        projects.setdefault(l, {'status': None, 'type': 'capital'})

# More structured extraction using known labeled sections
status_map = {}
current_section = None
for line in full_text.split('\n'):
    l = line.strip()
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
    # Project lines within a capital section until blank or other major header
    if current_section and not any(k in low for k in ['updates:', 'project description', 'project schedule', 'estimated schedule', 'agenda item', 'public works commission']):
        # treat this as a potential project name
        name = l
        if name in set(funding_df['Project_Name_norm']):
            status_map[name] = current_section

# Apply statuses
for name, status in status_map.items():
    projects.setdefault(name, {'type': 'capital', 'status': status})
    projects[name]['status'] = status

# Build dataframe of extracted projects
proj_rows = []
for name, info in projects.items():
    proj_rows.append({'Project_Name_norm': name, 'status': info.get('status'), 'type': info.get('type')})
proj_df = pd.DataFrame(proj_rows)

# Join with funding on normalized name
merged = funding_df.merge(proj_df, on='Project_Name_norm', how='inner')

# Filter for type capital, status design, and Amount > 50000
merged['Amount_num'] = pd.to_numeric(merged['Amount'])
mask = (merged['type'] == 'capital') & (merged['status'] == 'design') & (merged['Amount_num'] > 50000)
count = int(mask.sum())

result = json.dumps({'count_design_capital_over_50000': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_PtCHFclPSCzAKb50dh3eh65w': 'file_storage/call_PtCHFclPSCzAKb50dh3eh65w.json', 'var_call_VAvR9cqYv8JlSU9becDNKVPQ': 'file_storage/call_VAvR9cqYv8JlSU9becDNKVPQ.json'}

exec(code, env_args)
