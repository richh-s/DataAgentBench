code = """import json, re
from collections import defaultdict

with open(var_call_TOBEben6wKuNQVLE3xRB5Eea, 'r') as f:
    funding = json.load(f)

funding_names = {rec['Project_Name'] for rec in funding}

with open(var_call_sgtTIIAAuXdUS7RgpZGOd1zD, 'r') as f:
    docs = json.load(f)

text = '\n'.join(doc['text'] for doc in docs)

projects = {}
current_status = None

for line in text.split('\n'):
    line = line.strip()
    if not line:
        continue
    if line.startswith('Capital Improvement Projects (Design)'):
        current_status = 'design'
        continue
    if line.startswith('Capital Improvement Projects (Construction)'):
        current_status = 'completed'
        continue
    if line.startswith('Capital Improvement Projects (Not Started)'):
        current_status = 'not started'
        continue
    skip_prefixes = (
        '(',
        'Page ',
        'Agenda Item',
        'RECOMMENDED ACTION',
        'DISCUSSION:',
        'Subject:',
        'To:',
        'Prepared by:',
        'Approved by:',
        'Date prepared:',
        'Meeting date:',
        'Capital Improvement Projects',
        'Disaster Recovery Projects',
        'Project Description:',
        'Project Updates:',
        'Estimated Schedule',
        'Project Schedule',
        'Updates:'
    )
    if current_status and not line.startswith(skip_prefixes):
        if not line.endswith(':') and len(line) < 120:
            projects[line] = {'status': current_status, 'type': 'capital'}

count = 0
for name, info in projects.items():
    if info['status'] == 'design' and info['type'] == 'capital' and name in funding_names:
        count += 1

out = json.dumps(count)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TOBEben6wKuNQVLE3xRB5Eea': 'file_storage/call_TOBEben6wKuNQVLE3xRB5Eea.json', 'var_call_sgtTIIAAuXdUS7RgpZGOd1zD': 'file_storage/call_sgtTIIAAuXdUS7RgpZGOd1zD.json'}

exec(code, env_args)
