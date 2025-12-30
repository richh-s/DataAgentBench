code = """import json, re
from pathlib import Path

# Load full civic docs
with open(var_call_8UMUKMkElbruAtdNH4D5shE5, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Very heuristic extraction: treat each line that looks like a project name as a project
projects = {}
for line in full_text.split('\n'):
    s = line.strip()
    if not s:
        continue
    # skip headings
    if any(h in s.lower() for h in ['agenda', 'report', 'project description', 'updates', 'project schedule', 'estimated schedule']):
        continue
    # simple heuristic: lines with 'Project' or capitalized phrases
    if 'Project' in s or 'project' in s or re.search(r'[A-Z].+ [A-Z]', s):
        name = s
        if name not in projects:
            projects[name] = {'Project_Name': name, 'type': None, 'st': None}

# Determine type: disaster if contains FEMA/CalOES/CalJPIA or 'Disaster Recovery'
for p in projects.values():
    name = p['Project_Name']
    lname = name.lower()
    if any(k in lname for k in ['fema', 'caloes', 'caljpia', 'disaster']):
        p['type'] = 'disaster'
    else:
        p['type'] = 'capital'

# Try to find start dates by searching around first mention lines containing the project name
lines = full_text.split('\n')
for p in projects.values():
    name = p['Project_Name']
    for i, line in enumerate(lines):
        if name in line:
            window = '\n'.join(lines[max(0, i-3):i+4])
            m = re.search(r'(Begin Construction|Start|st)[: ]+([0-9]{4}[^\n]*)', window)
            if m:
                p['st'] = m.group(2).strip()
            break

# Filter disaster projects with start date containing 2022
disaster_2022_projects = {p['Project_Name'] for p in projects.values() if p['type']=='disaster' and p['st'] and '2022' in p['st']}

result = json.dumps(sorted(list(disaster_2022_projects)))
print("__RESULT__:")
print(result)"""

env_args = {'var_call_8UMUKMkElbruAtdNH4D5shE5': 'file_storage/call_8UMUKMkElbruAtdNH4D5shE5.json', 'var_call_x4qaPKvSclUXV3W5LhjymyhK': 'file_storage/call_x4qaPKvSclUXV3W5LhjymyhK.json'}

exec(code, env_args)
