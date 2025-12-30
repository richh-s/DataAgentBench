code = """import re, json
from pathlib import Path

funding_path = var_call_GAvKGmUFAmCZsvRhq2EmJkUI
with open(funding_path, 'r') as f:
    funding = json.load(f)

civic_path = var_call_3kNhrN7lBetdmsVLKRc8P7uz
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

project_status = {}

status_keywords = {
    'design': ['design phase', 'complete design', 'finalize the design', 'preliminary design'],
    'completed': ['construction was completed', 'complete construction', 'notice of completion filed'],
    'not started': ['not started', 'project will include', 'project was identified']
}

for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    current_project = None
    for line in lines:
        if re.match(r'^[A-Z0-9].{5,80}$', line) and not line.endswith('.'):
            current_project = line.strip()
        if current_project:
            lt = line.lower()
            if ('emergency' in lt) or ('fema' in lt):
                proj_rec = project_status.setdefault(current_project, {'status': 'unknown', 'emergency_related': True})
            for st, kws in status_keywords.items():
                if any(k in lt for k in kws):
                    proj_rec = project_status.setdefault(current_project, {'status': 'unknown', 'emergency_related': False})
                    proj_rec['status'] = st

emergency_funding = []
for row in funding:
    name = row['Project_Name']
    ln = name.lower()
    if ('fema' in ln) or ('emergency' in ln) or ('warning' in ln):
        status = project_status.get(name, {}).get('status', 'unknown')
        emergency_funding.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']),
            'Status': status
        })

emergency_funding.sort(key=lambda x: x['Project_Name'])

result = json.dumps(emergency_funding)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_GAvKGmUFAmCZsvRhq2EmJkUI': 'file_storage/call_GAvKGmUFAmCZsvRhq2EmJkUI.json', 'var_call_3kNhrN7lBetdmsVLKRc8P7uz': 'file_storage/call_3kNhrN7lBetdmsVLKRc8P7uz.json'}

exec(code, env_args)
