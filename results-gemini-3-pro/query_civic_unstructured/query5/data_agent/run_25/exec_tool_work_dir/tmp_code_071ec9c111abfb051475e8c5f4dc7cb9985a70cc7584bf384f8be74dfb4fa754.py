code = """import json
import re

path_fund = locals()['var_function-call-10469334728230477233']
path_civic = locals()['var_function-call-2938925832300121320']

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + chr(10)

lines = full_text.split(chr(10))
projects = {}
current_name = None
current_text = []

def is_bullet(l):
    l = l.strip()
    return l.startswith("(cid:") or l.startswith("•") or l.startswith("-")

for i in range(len(lines)):
    line = lines[i].strip()
    if not line: continue
    
    is_header = False
    if not is_bullet(line) and line[0].isupper():
        # Check lookahead
        has_bullet_next = False
        for j in range(i+1, min(i+5, len(lines))):
            nl = lines[j].strip()
            if not nl: continue
            if is_bullet(nl) or nl.startswith("Updates:") or nl.startswith("Project Description:"):
                has_bullet_next = True
            break
        
        if has_bullet_next:
            is_header = True
            
    # filter known skips
    if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line: is_header = False
    if "Agenda" in line: is_header = False
    
    if is_header:
        if current_name:
            projects[current_name] = chr(10).join(current_text)
        current_name = line
        current_text = []
    else:
        if current_name:
            current_text.append(line)

if current_name:
    projects[current_name] = chr(10).join(current_text)

norm_projects = {k.strip().lower(): v for k, v in projects.items()}

# Diagnostics
diag = {}
targets = ["malibu road slope repairs", "trancas canyon park planting and irrigation repairs"]

for k, v in norm_projects.items():
    for t in targets:
        if t in k:
            diag[k] = v[:500] # snippet

print("__RESULT__:")
print(json.dumps(diag))"""

env_args = {'var_function-call-10469334728230477233': 'file_storage/function-call-10469334728230477233.json', 'var_function-call-10469334728230474172': 'file_storage/function-call-10469334728230474172.json', 'var_function-call-2938925832300121320': 'file_storage/function-call-2938925832300121320.json', 'var_function-call-12502361018328116741': {'total': 87000.0, 'matches': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'parsed_titles': ['Agenda Report', '03-22-23', 'Jorge Rubalcava, Senior Civil Engineer', 'Date prepared: March 15, 2023', 'Meeting date: March 22, 2023']}, 'var_function-call-6275733380898896556': {'total': 87000.0, 'matches': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'parsed_sample': ['2022 morning view resurfacing & storm drain improvements', 'project and will submit to the county for review.', 'pch median improvements project', 'and rejected all bids due to a budget shortfall', 'or phasing out the project']}}

exec(code, env_args)
