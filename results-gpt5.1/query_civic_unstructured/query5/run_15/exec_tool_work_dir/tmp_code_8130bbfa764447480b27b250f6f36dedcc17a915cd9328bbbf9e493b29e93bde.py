code = """import json, re
from pathlib import Path

with open(var_call_8UMUKMkElbruAtdNH4D5shE5, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

projects = {}
for line in full_text.split('\n'):
    s = line.strip()
    if not s:
        continue
    if any(h in s.lower() for h in ['agenda', 'report', 'project description', 'updates', 'project schedule', 'estimated schedule']):
        continue
    if 'Project' in s or 'project' in s or re.search(r'[A-Z].+ [A-Z]', s):
        name = s
        if name not in projects:
            projects[name] = {'Project_Name': name, 'type': None, 'st': None}

for p in projects.values():
    name = p['Project_Name']
    lname = name.lower()
    if any(k in lname for k in ['fema', 'caloes', 'caljpia', 'disaster']):
        p['type'] = 'disaster'
    else:
        p['type'] = 'capital'

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

# collect all disaster projects regardless of year since year extraction is unreliable
result = json.dumps([p for p in projects.values() if p['type']=='disaster'])
print("__RESULT__:")
print(result)"""

env_args = {'var_call_8UMUKMkElbruAtdNH4D5shE5': 'file_storage/call_8UMUKMkElbruAtdNH4D5shE5.json', 'var_call_x4qaPKvSclUXV3W5LhjymyhK': 'file_storage/call_x4qaPKvSclUXV3W5LhjymyhK.json'}

exec(code, env_args)
